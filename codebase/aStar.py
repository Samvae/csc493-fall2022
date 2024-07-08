import numpy as np
import cv2
import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
from PIL import Image

class AStarPathfinding:
    def __init__(self, image_path):
        self.image_path = image_path
        self.start = None
        self.end = None
        self.image_data = None
        self.timings = {}

    class Cell:
        def __init__(self):
            self.parent_i = 0  # Parent cell's row index
            self.parent_j = 0  # Parent cell's column index
            self.f = float('inf')  # Total cost of the cell (g + h)
            self.g = float('inf')  # Cost from start to this cell
            self.h = 0  # Heuristic cost from this cell to destination

    def load_image(self):
        self.image_data = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        if self.image_data is None:
            raise ValueError("Could not load image.")
        self.image_data = cv2.cvtColor(self.image_data, cv2.COLOR_BGR2RGB)  # Convert to RGB

    def save_timing(self, timing_key: str, start_time) -> None:
        elapsed_time = dt.datetime.now() - start_time
        self.timings[timing_key] = [str(elapsed_time), elapsed_time]

    def is_valid(self, row, col, grid_shape):
        return (row >= 0) and (row < grid_shape[0]) and (col >= 0) and (col < grid_shape[1])

    def is_unblocked(self, grid, row, col, threshold):
        pixel_value = grid[row][col]
        red, green, blue = pixel_value
        intensity = (int(blue) + int(green) + int(red)) / 3
        return intensity < threshold

    def trace_path(self, cell_details, end):
        path = []
        row = end[0]
        col = end[1]

        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        path.append((row, col))
        path.reverse()

        return path

    def a_star_search(self, grid, start, end, threshold):
        start_time = dt.datetime.now()

        if not self.is_valid(start[0], start[1], grid.shape) or not self.is_valid(end[0], end[1], grid.shape):
            print("Start or End points are invalid")
            self.save_timing("a_star_search", start_time)
            return []
        if not self.is_unblocked(grid, start[0], start[1], threshold) or not self.is_unblocked(grid, end[0], end[1],
                                                                                               threshold):
            print("No Valid Path")
            self.save_timing("a_star_search", start_time)
            return []

        closed_list = [[False for _ in range(grid.shape[1])] for _ in range(grid.shape[0])]
        cell_details = [[self.Cell() for _ in range(grid.shape[1])] for _ in range(grid.shape[0])]

        i, j = start
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j

        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        found_end = False

        while len(open_list) > 0:
            p = heapq.heappop(open_list)
            i = p[1]
            j = p[2]
            closed_list[i][j] = True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for direct in directions:
                new_i = i + direct[0]
                new_j = j + direct[1]

                if self.is_valid(new_i, new_j, grid.shape) and self.is_unblocked(grid, new_i, new_j, threshold) \
                        and not closed_list[new_i][new_j]:
                    if (new_i, new_j) == end:
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        path = self.trace_path(cell_details, end)
                        found_end = True
                        self.save_timing("a_star_search", start_time)
                        return path
                    else:
                        g_new = cell_details[i][j].g + 1.0
                        h_new = abs(new_i - end[0]) + abs(new_j - end[1])
                        f_new = g_new + h_new

                        if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                            heapq.heappush(open_list, (f_new, new_i, new_j))
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j
        if not found_end:
            print("Failed to find the End cell")
            self.save_timing("a_star_search", start_time)
            return []

    def view_image(self):
        plt.imshow(self.image_data)
        plt.show()

    def set_start_end(self, grid_shape, offset=0, direction='vertical'):
        if direction == 'vertical':
            start_col = grid_shape[1] // 2 + offset
            end_col = start_col  # Same as start_col for vertical slice
            self.start = (0, start_col)
            self.end = (grid_shape[0] - 1, end_col)
        else:
            start_row = grid_shape[0] // 2 + offset
            end_row = start_row  # Same as start_row for horizontal slice
            self.start = (start_row, 0)
            self.end = (end_row, grid_shape[1] - 1)

    def draw_paths(self, threshold, paths, animate=False, blur=False, iterate=False):

        if iterate:
            original_image = np.copy(self.image_data)
            original_image = cv2.cvtColor(original_image, cv2.IMREAD_COLOR)  # Convert BGR to RGB
            original_image = cv2.copyMakeBorder(original_image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        else:
            image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))
            original_image = np.copy(image)

        if blur:
            original_image = original_image[1:-1, 1:-1]

            # Create a mask of the regions to inpaint (1 where you need inpainting, 0 otherwise)
            mask = np.all(original_image == [0, 0, 0], axis=2).astype(np.uint8) * 255
            # Apply Telea's or Navier-Stokes inpainting method
            inpainted_image = cv2.inpaint(original_image, mask, 3, cv2.INPAINT_NS)

            # Blur
            blurred_image = cv2.GaussianBlur(inpainted_image, (15, 15), 0)
            # blurred_image = cv2.blur(inpainted_image, (3,3))


            # Differential Brightness Masking
            mask = np.zeros_like(original_image)
            for y in range(original_image.shape[0]):
                for x in range(original_image.shape[1]):
                    if np.all(blurred_image[y, x] <= original_image[y, x]):
                        mask[y, x] = [255, 255, 255]  # White for blocked
                    else:
                        mask[y, x] = [0, 0, 0]  # Black for unblocked

            # Add borders back to the images
            mask = cv2.copyMakeBorder(mask, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))
            original_image = cv2.copyMakeBorder(original_image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))

            # # Display the result
            # plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
            # plt.show()
        else:
            mask = np.array(original_image)

        if animate:
            img_size = max(mask.shape)
            interval = max(1, 10000 // img_size)  # Scale speed based on image size

            fig, ax = plt.subplots()
            img_display = ax.imshow(original_image[1:-1, 1:-1])

            all_paths = []

            for offset, direction in paths:
                if direction.lower() == 'vertical':
                    self.set_start_end(mask.shape[:2], offset, direction.lower())
                elif direction.lower() == 'horizontal':
                    self.set_start_end(mask.shape[:2], offset, direction.lower())
                else:
                    raise ValueError("Invalid direction: choose 'Vertical' or 'Horizontal'")

                path = self.a_star_search(mask, self.start, self.end, threshold)
                if path:
                    all_paths.extend(path)

            def update(frame):
                if frame < len(all_paths):
                    pos = all_paths[frame]
                    original_image[pos[0], pos[1]] = [255, 0, 0]  # Red path
                    img_display.set_data(original_image[1:-1, 1:-1])

                return [img_display]

            ani = animation.FuncAnimation(fig, update, frames=len(all_paths), interval=interval, blit=True)
            plt.show()
        else:
            for offset, direction in paths:
                if direction.lower() == 'vertical':
                    self.set_start_end(mask.shape[:2], offset, direction.lower())
                elif direction.lower() == 'horizontal':
                    self.set_start_end(mask.shape[:2], offset, direction.lower())
                else:
                    raise ValueError("Invalid direction: choose 'Vertical' or 'Horizontal'")

                path = self.a_star_search(mask, self.start, self.end, threshold)
                if path:
                    for pos in path:
                        original_image[pos[0], pos[1]] = [255, 0, 0]  # Red path

        self.image_data = original_image[1:-1, 1:-1]

    def save_parts(self, iterate=False, iteration=1, image_index=1):
        if self.image_data is None:
            print("No paths drawn to split the image.")
            return []
        red_bordered_image = cv2.copyMakeBorder(self.image_data, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(255, 0, 0))
        image = cv2.cvtColor(red_bordered_image, cv2.COLOR_BGR2RGB)

        mask = cv2.inRange(image, (0, 0, 255), (0, 0, 255))
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        sections = []
        for i, contour in enumerate(contours[:-1]):
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [contour], -1, (255, 0, 0), -1)
            section = cv2.bitwise_and(image, image, mask=mask)
            section = section[1:-1, 1:-1]

            x, y, w, h = cv2.boundingRect(contour)
            section = section[y:y + h, x:x + w]

            red_pixels = np.all(section == [0, 0, 255], axis=-1)
            section[red_pixels] = [0, 0, 0]
            sections.append(section)

            if iterate:
                section_bgr = cv2.cvtColor(section, cv2.IMREAD_COLOR)
                if int(iteration) % 2 == 0:
                    section_bgr = cv2.cvtColor(section, cv2.COLOR_RGB2BGR)
                cv2.imwrite(f"iteration_{iteration}_section_{image_index}_{i + 1}.png", section_bgr)
                print(f"Saved section {i + 1} as iteration_{iteration}_part_{image_index}_{i + 1}.png")
            else:
                cv2.imwrite(f"section_part_{i + 1}.png", section)
                print(f"Saved section {i + 1} as section_{i + 1}.png")

        return sections

    def get_brightness_mean(self):
        if self.image_data is None:
            self.load_image()
        mean_brightness = np.mean(self.image_data)
        print(mean_brightness)
        return mean_brightness

    def auto_cut(self, animate, blur, iterate=1):
        if self.image_data is None:
            self.load_image()

        current_images = [self.image_data]
        for iter_num in range(1, iterate + 1):
            new_images = []
            for idx, image in enumerate(current_images):
                self.image_data = image
                paths = [(0, 'Vertical'), (0, 'Horizontal')]
                self.draw_paths(self.get_brightness_mean(), paths, animate, blur, True)
                new_images.extend(self.save_parts(True, iter_num, idx + 1))
            current_images = new_images


def main():
    image_path = './images/44x29-test-2011-05Andreo_BigDipper7k.png'
    pathfinding = AStarPathfinding(image_path)
    paths = [(0, 'Vertical'), (0,'Horizontal')]
    mean = pathfinding.get_brightness_mean()

    pathfinding.auto_cut(animate=True, blur=True, iterate=1)

    # pathfinding.draw_paths(mean, paths, False, True)
    # pathfinding.view_image()
    # pathfinding.draw_paths(mean, paths, True, True)
    # On if Animation is Off
    # pathfinding.view_image()
    # pathfinding.save_parts()


if __name__ == "__main__":
    main()
