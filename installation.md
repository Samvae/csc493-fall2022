# Star Splitter Installation Guide

This guide outlines the steps to install Star Splitter, a Python program for image partitioning using the A* algorithm in astrophotography.

## 1. Download and install a Python IDE

Choose and install a Python IDE (Integrated Development Environment) of your choice. Popular options include:

- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/)

## 2. Clone the Star Splitter repository from GitHub

Clone directly from GitHub or open a terminal and execute the following command to clone the repository:

```bash
git clone https://github.com/Samvae/csc493-fall2022.git
```

## 3. Open and Run the Program in an IDE
1. Open the Star Splitter code (App.py) in your IDE.
2. Locate the run function or the main execution block of the program.
3. Run the program using your IDE's built-in functionality.


## 4. Install Required Libraries

```bash
pip install tkinter
pip install customtkinter
pip install matplotlib
pip install numpy
pip install opencv-python
```
You can also include these imports in your script:

```bash
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

```
