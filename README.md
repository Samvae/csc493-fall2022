# Star Splitter : Image Partitioning with A* for Astrophotography
## Description/Motivation

Star Splitter will utilize the A* algorithm, a pathfinding algorithm known for its efficiency and effectiveness in traversing graphs, to create paths for dividing astrophotography images into meaningful segments. The GUI will allow users to interactively define segmentation parameters, such as brightness thresholds, and visualize the segmentation process in real-time. Additionally, users will have the flexibility to customize the partitioning algorithm's parameters to suit their specific analysis needs.

## Project Concept
[Click here to read the project concept](/concept.md)

## Scope

The scope of Star Splitter includes developing a user-friendly tool for segmenting astrophotography images using the A* algorithm. Major features will include a graphical user interface (GUI) for interactive image partitioning, real-time visualization of segmentation results, customizable segmentation parameters, and export functionality for segmented images. Out of scope for this project are segmentation beyond splitting images, machine learning integration, object identifier, and 3D visualization. These out-of-scope features may be considered for future development but will not be included in the initial project.


## Vision

Star Splitter aims to improve the analysis of astrophotography images by providing an intuitive tool for image partitioning. This tool will enable astronomers and enthusiasts to easily segment and explore celestial objects in their images, leading to faster data analysis and the potential for new discoveries. By the project's completion, users will have a reliable and user-friendly application that enhances their ability to study the night sky, making advanced image analysis accessible to a broader audience.


### Prerequisites

Python IDE: Ensure you have a Python Integrated Development Environment (IDE) installed on your system. Popular choices include PyCharm, Visual Studio Code, or Jupyter Notebook.

Python Libraries:
*These can be installed using:*
- tkinter (usually included with Python installations)
- customtkinter: `pip install customtkinter`
- matplotlib: `pip install matplotlib`
- numpy: `pip install numpy`
- OpenCV (cv2): `pip install opencv-python`
- aStar: (Assuming this is your custom library, provide installation instructions if applicable)

## Requirements

[Click here to see the requirements](/requirements.md)

## Design
[Click here to see the design specifications](/design.md)

## Test Plan
[Click here to see the test plan document](/test.plan.md)


## Built With

Star Splitter: Image partitioning with A* for Astrophotography was built using the following frameworks and libraries:

- **tkinter**: Standard Python interface to the Tk GUI toolkit, used for creating the graphical user interface.
- **customtkinter**: A modern and customizable version of tkinter.
- **matplotlib**: A plotting library for Python, used for visualizing image segmentation results.
- **numpy**: Used for numerical computing and array manipulation in Python.
- **OpenCV (cv2)**: A computer vision library used for image processing tasks.
- **AStarPathfinding**: A custom implementation of the A* algorithm for pathfinding and image partitioning.
- **matplotlib.animation**: Used for creating animations in matplotlib.
- **FigureCanvasTkAgg**: A matplotlib backend that embeds matplotlib plots into Tkinter applications.
- **NavigationToolbar2Tk**: A matplotlib toolbar that integrates with Tkinter.

## Author

**Sam Villahermosa**: Star Splitter : Image Partitioning with A* for Astrophotography [LinkedIn](https://www.linkedin.com/in/samvillahermosa/)

#### About the Lead Developer: 

Sam is an upcoming senior at Berea College, pursuing a degree in Computer Science. With a passion for both physical and mental well-being, Sam enjoys balancing academic pursuits with outdoor activities and fitness. 

A dedicated coder and lifelong learner, Sam is motivated by the opportunity to create impactful solutions that enhance society's quality of life, whether through entertainment or practical applications. With an interest in software development, Sam is committed to continuous growth and innovation in the field.

In addition to programming, Sam enjoys exploring new technologies, reading, and spending time with friends and family. With a proactive approach to challenges and a collaborative spirit, Sam strives to contribute positively to every project and team environment.


## Acknowledgments

- [GeeksforGeeks - A* Algorithm](https://www.geeksforgeeks.org/a-search-algorithm/)
- [GeeksforGeeks - OpenCV ](https://www.geeksforgeeks.org/opencv-python-tutorial/)
- [OpenCV Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- Professor Deanna M. Wilborne 
- Berea College


## License

MIT License

Copyright (c) 2024 Sam Villahermosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Installation and Use Guide
[Click here to see the installation guide](/installation.md)