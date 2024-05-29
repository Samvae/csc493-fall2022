# Functional Requirements

## Number: FR1
- **Statement:** The software must provide a graphical user interface (GUI) for interactive image partitioning.
- **Evaluation Method:** Verify the presence and functionality of the GUI during testing.
- **Dependency:** None
- **Priority:** Essential
- **Requirement Revision History:** [Initial creation: 2024-05-28]

## Number: FR2
- **Statement:** The software must allow users to customize segmentation parameters, such as brightness thresholds and region of interest markers.
- **Evaluation Method:** Test the customization options in the GUI with different input parameters.
- **Dependency:** FR1
- **Priority:** High
- **Requirement Revision History:** [Initial creation: 2024-05-28]

## Number: FR3
- **Statement:** The software must provide real-time visualization of segmentation results.
- **Evaluation Method:** Check the display of real-time updates during image partitioning.
- **Dependency:** FR1
- **Priority:** High
- **Requirement Revision History:** [Initial creation: 2024-05-28]

## Number: FR4
- **Statement:** The software must allow users to export segmented images.
- **Evaluation Method:** Verify the export functionality by saving segmented images in different formats.
- **Dependency:** FR1
- **Priority:** Essential
- **Requirement Revision History:** [Initial creation: 2024-05-28]

# Non-functional Requirements

## Number: NFR1
- **Statement:** The software must run on Windows and macOS operating systems.
- **Evaluation Method:** Test the software on both Windows and macOS environments.
- **Dependency:** None
- **Priority:** Essential
- **Requirement Revision History:** [Initial creation: 2024-05-28]

## Number: NFR2
- **Statement:** The software should be user-friendly and intuitive, requiring minimal technical expertise to operate.
- **Evaluation Method:** Conduct usability testing with users of varying technical backgrounds.
- **Dependency:** FR1
- **Priority:** High
- **Requirement Revision History:** [Initial creation: 2024-05-28]

## Number: NFR3
- **Statement:** The software should provide fast and efficient image partitioning, processing images within a reasonable time frame.
- **Evaluation Method:** Measure the processing time for segmenting different sizes and types of images.
- **Dependency:** FR1, FR3
- **Priority:** High
- **Requirement Revision History:** [Initial creation: 2024-05-28]
