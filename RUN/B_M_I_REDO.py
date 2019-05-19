import csv
import os
import re
import textwrap

import guessit
import pyfiglet
import pymediainfo

import matplotlib.pylab as plt
import numpy as np
from tkinter import filedialog
from tkinter import *

from ascii_graph import Pyasciigraph


directory_selected_in_gui_list = []


def select_directory_with_tk_gui():
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    directory_selected_in_gui_list.append(selected_directory)
    root.destroy()
    print(directory_selected_in_gui_list[0])


select_directory_with_tk_gui()
