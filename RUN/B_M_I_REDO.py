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


def launch_media_index():
    sep()
    print(pyfiglet.figlet_format("MEDIA-INDEX", font="cybermedium"))
    sep()
    print("1) QUERIES - 2) SORTING - 3) FILE DATA/INFO - 4) GRAPHS - 5) TOTALS - 6) INDEXING")
    print()
    print("0) EXIT")
    sep()
    lmi_input = input("ENTER #")
    sep()
    lmi_action = int(lmi_input)
    if lmi_action == 1:
        pass
    elif lmi_action == 2:
        pass
    elif lmi_action == 3:
        pass
    elif lmi_action == 4:
        pass
    elif lmi_action == 5:
        pass
    elif lmi_action == 6:
        pass
    elif lmi_action == 0:
        exit()


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


launch_media_index()
