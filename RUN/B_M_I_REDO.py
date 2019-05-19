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

username_input = None


def compare_results(results_user, results_other):
    output = []
    for line in results_user:
        if line not in results_other:
            output.append('HAVE: ' + line)

    for line in results_other:
        if line not in results_user:
            output.append('DO NOT HAVE: ' + line)

    return output


def first_launch_dirs():
    print(pyfiglet.figlet_format("MEDIA_INDEX", font="cybermedium"))
    separator()

    global username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input

    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    separator()

    user_info_file = os.path.expanduser("~/{0}_MEDIA_INDEX/{0}_USER_INFO.csv".format(username_input))

    if os.path.isfile(user_info_file):
        user_info_file = list(csv.reader(open(user_info_file)))
        print(user_info_file)
        movie_dir_input = user_info_file[1][1]
        tv_dir_input = user_info_file[2][1]
        movie_alt_dir_input = user_info_file[3][1]
        tv_alt_dir_input = user_info_file[4][1]
    else:
        print("ENTER PATH OF MOVIE DIRECTORY:")
        movie_dir_input = select_directory_with_tk_gui()
        print()
        print("ENTER PATH OF TV DIRECTORY:")
        tv_dir_input = select_directory_with_tk_gui()
        print()
        print("ENTER PATH OF ALTERNATE MOVIE DIRECTORY, IF NONE HIT CANCEL:")
        movie_alt_dir_input = select_directory_with_tk_gui()
        print()
        print("ENTER PATH OF ALTERNATE TV DIRECTORY, IF NONE HIT CANCEL:")
        tv_alt_dir_input = select_directory_with_tk_gui()
        separator()

        user_info = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                     'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}

        os.makedirs(os.path.expanduser(r'~/{0}_MEDIA_INDEX/'.format(username_input)), exist_ok=True)
        os.makedirs(os.path.expanduser(r'~/{0}_MEDIA_INDEX/FILES'.format(username_input)), exist_ok=True)

        with open(user_info_file, 'w', encoding='UTF8', newline='') as f:
            csv_writer = csv.writer(f)
            for user_data in user_info.items():
                csv_writer.writerow(user_data)


def launch_media_index():
    first_launch_dirs()
    print(pyfiglet.figlet_format("MEDIA_INDEX", font="cybermedium"))
    separator()
    print("1) QUERIES - 2) SORTING - 3) FILE DATA/INFO - 4) GRAPHS - 5) TOTALS - 6) INDEXING")
    print()
    print("0) EXIT")
    separator()
    lmi_input = input("ENTER #")
    separator()
    lmi_input_action = int(lmi_input)
    if lmi_input_action == 1:
        pass
    elif lmi_input_action == 2:
        pass
    elif lmi_input_action == 3:
        pass
    elif lmi_input_action == 4:
        pass
    elif lmi_input_action == 5:
        pass
    elif lmi_input_action == 6:
        pass
    elif lmi_input_action == 0:
        exit()


def select_directory_with_tk_gui():
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    root.destroy()
    return selected_directory


def separator():
    for lines in "\n", '-' * 100, "\n":
        print(lines)


launch_media_index()
