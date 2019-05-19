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


def compare_results(results_user, results_other):
    output = []
    for line in results_user:
        if line not in results_other:
            output.append('HAVE: ' + line)

    for line in results_other:
        if line not in results_user:
            output.append('DO NOT HAVE: ' + line)

    return output


def select_directory_with_tk_gui():
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    directory_selected_in_gui_list.append(selected_directory)
    root.destroy()


def sep():
    for lines in "\n", '-' * 100, "\n":
        print(lines)


select_directory_with_tk_gui()
