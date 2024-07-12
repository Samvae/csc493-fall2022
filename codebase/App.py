import tkinter
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import cv2
from aStar import AStarPathfinding
from matplotlib.animation import FuncAnimation

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")


class VerticalNavigationToolbar2Tk(NavigationToolbar2Tk):
    def __init__(self, canvas, window):
        super().__init__(canvas, window, pack_toolbar=False)

    def _Button(self, text, image_file, toggle, command):
        b = super()._Button(text, image_file, toggle, command)
        b.config(width=45, height=90)
        b.pack(side=tkinter.TOP)
        return b

    def _create_frame(self):
        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.TOP, fill=tkinter.X)
        return frame

    def _Spacer(self):
        s = tkinter.Frame(self._create_frame(), width=26, relief=tkinter.RIDGE, padx=2)
        s.pack(side=tkinter.TOP, pady=5)
        return s

    def set_message(self, s):
        pass


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.pathfinding = None
        self.threshold = 0
        self.paths = [(0, 'Vertical')]
        self.image_path = None
        self.animate = False
        self.mask = False
        self.iterate = False
        self.iteration_count = 1

        self.title("Star Splitter : Image Partitioning with A* for Astrophotography")
        self.iconbitmap(False, "star.ico")
        self.geometry(f"{1100}x{580}")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Star Splitter",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.tabview = customtkinter.CTkTabview(self.sidebar_frame, width=250)
        self.tabview.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.tabview.add("Current")
        self.tabview.add("Threshold")
        self.tabview.add("Paths")
        self.tabview.add("Settings")
        self.tabview.tab("Current").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Threshold").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Paths").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Current"))
        self.scrollable_frame.grid(row=1, column=0, padx=0, pady=4, sticky="nsew")

        self.current_threshold_label = customtkinter.CTkLabel(self.scrollable_frame,
                                                              text="Threshold:  " + str(self.threshold))
        self.current_threshold_label.grid(row=0, column=0, padx=(30, 20), pady=(20, 10), sticky="w")

        self.current_paths_label = customtkinter.CTkLabel(self.scrollable_frame, text="Paths:")
        self.current_paths_label.grid(row=1, column=0, padx=30, pady=0, sticky="w")

        self.paths_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.paths_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=0, sticky="nsew")
        self.paths_frame.grid_columnconfigure(0, weight=1)
        self.paths_frame.grid_columnconfigure(1, weight=0)
        self.update_paths_display()

        self.slider = customtkinter.CTkSlider(self.tabview.tab("Threshold"), orientation="vertical", from_=0, to=255,
                                              command=self.update_progressbar_from_slider)
        self.slider.grid(row=0, column=0, rowspan=5, padx=(10, 5), pady=11, sticky="ns")
        self.progressbar = customtkinter.CTkProgressBar(self.tabview.tab("Threshold"), orientation="vertical")
        self.progressbar.grid(row=0, column=1, rowspan=5, padx=(10, 5), pady=(10, 10), sticky="ns")

        self.threshold_label = customtkinter.CTkLabel(self.tabview.tab("Threshold"), text="Enter Threshold Value")
        self.threshold_label.grid(row=0, column=2, padx=20, pady=10)
        self.entry_threshold = customtkinter.CTkEntry(self.tabview.tab("Threshold"), placeholder_text="(0 - 255)")
        self.entry_threshold.grid(row=1, column=2, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.save_threshold_button = customtkinter.CTkButton(self.tabview.tab("Threshold"), fg_color="transparent",
                                                             border_width=2, text="Save",
                                                             text_color=("gray10", "#DCE4EE"),
                                                             command=self.save_threshold)
        self.save_threshold_button.grid(row=2, column=2, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.path_label = customtkinter.CTkLabel(self.tabview.tab("Paths"), text="Enter Path Information")
        self.path_label.grid(row=0, column=0, padx=20, pady=10)
        self.entry_offset = customtkinter.CTkEntry(self.tabview.tab("Paths"), placeholder_text="Offset Starts at 0")
        self.entry_offset.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.option_menu = customtkinter.CTkOptionMenu(self.tabview.tab("Paths"), values=['Vertical', 'Horizontal'],
                                                       command=self.update_placeholder)
        self.option_menu.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.save_path_button = customtkinter.CTkButton(self.tabview.tab("Paths"), fg_color="transparent",
                                                        border_width=2, text="Save", text_color=("gray10", "#DCE4EE"),
                                                        command=self.save_path)
        self.save_path_button.grid(row=3, column=0, padx=(20, 20), pady=24, sticky="nsew")

        self.checkbox_1 = customtkinter.CTkCheckBox(self.tabview.tab("Settings"), text='Animate',
                                                    command=self.toggle_animate)
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=25, sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.tabview.tab("Settings"), text='Mask', command=self.toggle_mask)
        self.checkbox_2.grid(row=0, column=0, padx=20, pady=25, sticky="w")
        self.entry_iterate = customtkinter.CTkEntry(self.tabview.tab("Settings"), placeholder_text="", width=80)
        self.entry_iterate.grid(row=2, column=0, padx=(20, 0), pady=24, sticky="w")
        self.save_iterate_button = customtkinter.CTkButton(self.tabview.tab("Settings"),
                                                           width=80,
                                                           border_width=2, text="Iterate",
                                                           command=self.get_iteration)
        self.save_iterate_button.grid(row=2, column=0, padx=(0, 20), pady=24, sticky='e')

        self.select_image_button = customtkinter.CTkButton(self.sidebar_frame, text='Select Image',
                                                           command=self.select_image)
        self.select_image_button.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.run_button = customtkinter.CTkButton(self.sidebar_frame, text='Draw', width=100, command=self.run_a_star)
        self.run_button.grid(row=4, column=0, padx=30, pady=10, sticky="n")

        self.save_button = customtkinter.CTkButton(self.sidebar_frame, text='Save Sections', command=self.save_image)
        self.save_button.grid(row=4, column=0, padx=20, pady=60, sticky='n')

        self.matplotlib_frame = customtkinter.CTkFrame(self)
        self.matplotlib_frame.grid(row=0, column=2, sticky="nsew")
        self.matplotlib_frame.grid_columnconfigure(0, weight=1)
        self.matplotlib_frame.grid_rowconfigure(0, weight=1)

        self.figure = plt.figure(figsize=(1, 1))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.matplotlib_frame)
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.nav_toolbar = customtkinter.CTkFrame(self)
        self.nav_toolbar.grid(row=0, column=1, sticky="nsew")
        self.nav_toolbar.grid_columnconfigure(0, weight=1)
        self.nav_toolbar.grid_rowconfigure(0, weight=1)

        self.toolbar = VerticalNavigationToolbar2Tk(self.canvas, self.nav_toolbar)
        self.toolbar.update()
        self.toolbar.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.figure.patch.set_facecolor(color='#f0f0f0')

    def update_threshold_from_slider(self, value):
        self.threshold = int(value)
        self.entry_threshold.delete(0, tkinter.END)
        self.entry_threshold.insert(0, str(self.threshold))

    def update_progressbar_from_slider(self, value):
        self.progressbar.set(value / 255)
        self.update_threshold_from_slider(value)

    def save_threshold(self):
        try:
            threshold = int(self.entry_threshold.get())
            if 0 <= threshold <= 255:
                self.threshold = threshold
                self.slider.set(threshold)
                self.progressbar.set(threshold / 255)
                self.update_current_tab()
                tkinter.messagebox.showinfo("Success", f"Threshold set to {self.threshold}")
            else:
                tkinter.messagebox.showerror("Error", "Threshold must be between 0 and 255.")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input. Please enter a number between 0 and 255.")

    def save_path(self):
        try:
            offset = int(self.entry_offset.get())
            direction = self.option_menu.get()
            if direction.lower() in ['vertical', 'horizontal']:
                self.paths.append((offset, direction))
                self.update_current_tab()
                tkinter.messagebox.showinfo("Success", f"Path added: {(offset, direction)}")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid offset. Please enter a number.")

    def update_paths_display(self):
        for widget in self.paths_frame.winfo_children():
            widget.destroy()

        for idx, path in enumerate(self.paths):
            path_label = customtkinter.CTkLabel(self.paths_frame, text=str(path), anchor="w")
            path_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            delete_button = customtkinter.CTkButton(self.paths_frame, text="Delete", width=10,
                                                    command=lambda idx=idx: self.delete_path(idx))
            delete_button.grid(row=idx, column=1, padx=10, pady=5)

    def delete_path(self, idx):
        if 0 <= idx < len(self.paths):
            del self.paths[idx]
            self.update_current_tab()

    def update_current_tab(self):
        self.current_threshold_label.configure(text="Threshold:  " + str(self.threshold))
        self.update_paths_display()

    def display_image(self, image_data):
        if image_data is None:
            tkinter.messagebox.showerror("Error", "No image data to display.")
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.tick_params(colors='black', which='both')
        ax.imshow(cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB))
        ax.axis('on')
        self.canvas.draw()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tif")])
        if not file_path:
            return

        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if image is None:
            tkinter.messagebox.showerror("Error", "Failed to load the image.")
            return

        self.mean_brightness(image)
        self.update_current_tab()
        self.image_path = file_path
        self.display_image(image)
        self.entry_offset.configure(
            placeholder_text="Min: " + str(0 - (image.shape[1] // 2)) + " | Max: " + str(image.shape[1] // 2))

    def save_image(self):
        if self.image_path is not None:
            self.pathfinding.save_parts(False)
        else:
            tkinter.messagebox.showerror("Error", "No pathfinding data to save. Click draw before saving.")

    def toggle_animate(self):
        self.animate = self.checkbox_1.get() == 1

    def toggle_mask(self):
        self.mask = self.checkbox_2.get() == 1

    def run_a_star(self):
        if not self.image_path:
            tkinter.messagebox.showerror("Error", "No image path provided.")
            return

        self.pathfinding = AStarPathfinding(self.image_path)
        self.pathfinding.load_image()

        try:
            if self.iterate:
                self.pathfinding.auto_cut(self.animate, self.mask, self.iteration_count)
            elif self.animate:
                self.display_animation()
            else:
                self.pathfinding.draw_paths(self.threshold, self.paths, animate=False, blur=self.mask)
                image = cv2.cvtColor(self.pathfinding.image_data, cv2.COLOR_BGR2RGB)
                self.display_image(image)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to process image: {e}")

    def display_animation(self):
        image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        original_image = np.copy(image)

        if self.mask:
            mask = np.all(original_image == [0, 0, 0], axis=2).astype(np.uint8) * 255
            inpainted_image = cv2.inpaint(original_image, mask, 3, cv2.INPAINT_NS)
            blurred_image = cv2.GaussianBlur(inpainted_image, (15, 15), 0)

            mask = np.zeros_like(original_image, dtype=np.uint8)
            for y in range(original_image.shape[0]):
                for x in range(original_image.shape[1]):
                    if np.all(blurred_image[y, x] <= original_image[y, x]):
                        mask[y, x] = [255, 255, 255]
                    else:
                        mask[y, x] = [0, 0, 0]
        else:
            mask = np.array(original_image)

        all_paths = []
        for offset, direction in self.paths:
            if direction.lower() == 'vertical':
                self.pathfinding.set_start_end(mask.shape[:2], offset, direction.lower())
            elif direction.lower() == 'horizontal':
                self.pathfinding.set_start_end(mask.shape[:2], offset, direction.lower())
            else:
                raise ValueError("Invalid direction: choose 'Vertical' or 'Horizontal'")

            path = self.pathfinding.a_star_search(mask, self.pathfinding.start, self.pathfinding.end, self.threshold)
            if path:
                all_paths.extend(path)
            else:
                tkinter.messagebox.showerror("Error",
                                             f"No valid path found for direction {direction} and offset {offset}.")
                return

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.tick_params(colors='black', which='both')
        img_size = max(mask.shape)
        interval = max(1, 1000 // img_size)
        img_display = ax.imshow(image[1:-1, 1:-1])

        def update(frame):
            pos = all_paths[frame]
            original_image[pos[0]][pos[1]] = [255, 0, 0]
            img_display.set_data(original_image[1:-1, 1:-1])
            return [img_display]

        ani = FuncAnimation(self.figure, update, frames=len(all_paths), interval=interval, blit=True)
        self.canvas.draw()
        self.toolbar.update()
        self.pathfinding.image_data = original_image[1:-1, 1:-1]

    def mean_brightness(self, image):
        mean_brightness = np.mean(image)
        self.threshold = int(mean_brightness)

    def update_placeholder(self, value):
        if self.image_path:
            image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
            if image is not None:
                if value == 'Vertical':
                    self.entry_offset.configure(
                        placeholder_text="Min: " + str(0 - (image.shape[1] // 2)) + " | Max: " + str(
                            image.shape[1] // 2))
                elif value == 'Horizontal':
                    self.entry_offset.configure(
                        placeholder_text="Min: " + str(0 - (image.shape[0] // 2)) + " | Max: " + str(
                            image.shape[0] // 2))

    def get_iteration(self):
        iteration_input = self.entry_iterate.get()
        try:
            iteration_count = int(iteration_input)
            if iteration_count > 0:
                self.iteration_count = iteration_count
                self.iterate = True
            else:
                tkinter.messagebox.showerror("Error", "Iteration count must be a positive integer.")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
