# Software Design Document

## Introduction
This document outlines the architectural design of the "Star Splitter: Image Partitioning with A* for Astrophotography" software. The design is organized to meet both functional and non-functional requirements and to provide a clear and simplified description of the system.

## Architectural Model
The software is structured into several key components, each responsible for specific functionalities. The hierarchical presentation of these components ensures a clear understanding of the flow of control and data through the system.

### Major Components
1. **Graphical User Interface (GUI)**
   - **Description:** Provides an interactive interface for users to load images, customize segmentation parameters, visualize results, and export segmented images.
   - **Classes:**
     - `App`
     - `VerticalNavigationToolbar2Tk`

2. **Image Processing**
   - **Description:** Handles image loading, brightness calculation, pathfinding, and image segmentation.
   - **Classes:**
     - `AStarPathfinding`

3. **Event Handlers and Utilities**
   - **Description:** Manages user interactions, including button clicks, checkbox toggles, and input validation.
   - **Methods:**
     - `select_image`
     - `save_image`
     - `run_a_star`
     - `display_animation`
     - `toggle_animate`
     - `toggle_mask`
     - `save_threshold`
     - `save_path`
     - `delete_path`
     - `update_paths_display`
     - `update_current_tab`
     - `update_progressbar_from_slider`
     - `update_threshold_from_slider`
     - `update_placeholder`
     - `open_input_dialog_event`

4. **Visualization**
   - **Description:** Provides real-time visualization of segmentation results using Matplotlib.
   - **Classes:**
     - `FigureCanvasTkAgg`
     - `FuncAnimation`

### Control Flow
1. **User Loads Image**
   - The user selects an image file through the GUI.
   - The `select_image` method loads the image using OpenCV and displays it on the Matplotlib canvas.

2. **User Sets Parameters**
   - The user adjusts the threshold value using the slider or entry box.
   - The user adds paths by specifying offsets and directions.
   - The `save_threshold` and `save_path` methods validate and save these parameters.

3. **User Runs Segmentation**
   - The user clicks the "Draw" button.
   - The `run_a_star` method initializes the `AStarPathfinding` class, loads the image, and performs the A* pathfinding algorithm.
   - If animation is enabled, `display_animation` visualizes the pathfinding process in real-time.

4. **User Exports Segmented Image**
   - The user clicks the "Save Sections" button.
   - The `save_image` method saves the segmented parts of the image.

### Interactions Among Components
- The `App` class acts as the main controller, initializing the GUI and handling user interactions.
- The `AStarPathfinding` class is responsible for image processing tasks and is called by methods within the `App` class.
- Visualization components (`FigureCanvasTkAgg` and `FuncAnimation`) are used to display results within the GUI, interacting with the `App` class for data updates.

### Consistent Conventions
- **Error Handling:** User inputs are validated, and error messages are displayed using `tkinter.messagebox`.
- **Code Organization:** The code is organized into logical sections with clear comments for each method and class.

## Conclusion
This architectural design ensures a simplified and clear understanding of the "Star Splitter" software. It defines the major components, their interactions, and control flow, adhering to consistent conventions. This design will guide the implementation and further development of the software, ensuring it meets the defined functional and non-functional requirements.
