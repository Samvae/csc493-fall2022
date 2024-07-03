# Test Plan

## Summary of Testing Activities and Overall Approach
This document outlines the test plan for "Star Splitter: Image Partitioning with A* for Astrophotography." The testing activities will focus on verifying that the software meets the functional and non-functional requirements as specified. The overall approach will include both manual and automated testing to ensure comprehensive coverage. Key areas of focus will include the graphical user interface (GUI), image processing functionalities, and the export of segmented images. Usability and performance testing will also be conducted to ensure the software is user-friendly and efficient.

## Key Test Cases

### Test Case 1: GUI Initialization
- **Name and Number:** TC1
- **Requirement:** FR1
- **Preconditions:** None
- **Steps:**
  1. Launch the application.
  2. Verify that the main GUI window appears.
  3. Check for the presence of key GUI components such as the image display area, parameter input fields, and action buttons.
- **Desired Results:** The main GUI window should appear with all key components visible and functional.

### Test Case 2: Image Loading
- **Name and Number:** TC2
- **Requirement:** FR1
- **Preconditions:** TC1 must be executed successfully.
- **Steps:**
  1. Click the "Load Image" button.
  2. Select a valid image file from the file dialog.
  3. Verify that the selected image is displayed in the GUI.
- **Desired Results:** The selected image should be displayed in the GUI without any errors.

### Test Case 3: Segmentation Parameter Customization
- **Name and Number:** TC3
- **Requirement:** FR3
- **Preconditions:** TC2 must be executed successfully.
- **Steps:**
  1. Adjust the brightness threshold slider.
  2. Enter a specific value in the threshold input box.
  3. Add a region of interest marker.
  4. Verify that the parameters are updated and displayed correctly.
- **Desired Results:** The segmentation parameters should be customizable and reflect the user's input accurately.

### Test Case 4: Real-time Visualization
- **Name and Number:** TC4
- **Requirement:** FR4
- **Preconditions:** TC3 must be executed successfully.
- **Steps:**
  1. Click the "Draw" button to start the segmentation process.
  2. Observe the real-time visualization of the segmentation.
- **Desired Results:** The segmentation process should be visualized in real-time, displaying the progress and results as they are computed.

### Test Case 5: Exporting Segmented Images
- **Name and Number:** TC5
- **Requirement:** FR2
- **Preconditions:** TC4 must be executed successfully.
- **Steps:**
  1. Click the "Save Sections" button.
  2. Choose the desired format and location for saving the segmented images.
  3. Verify that the segmented images are saved correctly.
- **Desired Results:** The segmented images should be saved in the chosen format and location without any errors.

### Test Case 6: Cross-Platform Compatibility
- **Name and Number:** TC6
- **Requirement:** NFR1
- **Preconditions:** None
- **Steps:**
  1. Install and run the application on a Windows operating system.
  2. Install and run the application on a macOS operating system.
  3. Verify that the application performs consistently across both platforms.
- **Desired Results:** The application should run smoothly on both Windows and macOS without any platform-specific issues.

### Test Case 7: Usability Testing
- **Name and Number:** TC7
- **Requirement:** NFR2
- **Preconditions:** TC1 through TC5 must be executed successfully.
- **Steps:**
  1. Conduct usability testing with users of varying technical backgrounds.
  2. Observe and record user interactions and feedback.
  3. Identify any usability issues or areas for improvement.
- **Desired Results:** Users should find the software user-friendly and intuitive, with minimal technical expertise required to operate it.

### Test Case 8: Performance Testing
- **Name and Number:** TC8
- **Requirement:** NFR3
- **Preconditions:** TC1 through TC5 must be executed successfully.
- **Steps:**
  1. Measure the processing time for segmenting a small image.
  2. Measure the processing time for segmenting a large image.
  3. Verify that the processing time is within an acceptable range for both cases.
- **Desired Results:** The software should perform image partitioning efficiently, with reasonable processing times for both small and large images.
