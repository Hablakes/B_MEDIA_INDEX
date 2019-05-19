import csv
import os
import re
import textwrap

import guessit
import pyfiglet
import pymediainfo

import matplotlib.pylab as plt
import numpy as np

from ascii_graph import Pyasciigraph

from tkinter import filedialog
from tkinter import *


username_input = None

media_index_folder = '~/{0}_MEDIA_INDEX'


all_extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
                  ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
                  ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm",
                  ".rmvb", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm", ".nfo",
                  ".srt")

video_extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
                    ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
                    ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm",
                    ".rmvb", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


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

    user_info_file = os.path.expanduser((media_index_folder + '/{0}_USER_INFO.csv').format(username_input))

    if os.path.isfile(user_info_file):
        user_info_file = list(csv.reader(open(user_info_file)))
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

        os.makedirs(os.path.expanduser((media_index_folder + '/').format(username_input)), exist_ok=True)
        os.makedirs(os.path.expanduser((media_index_folder + '/FILES').format(username_input)), exist_ok=True)

        with open(user_info_file, 'w', encoding='UTF8', newline='') as f:
            csv_writer = csv.writer(f)
            for user_data in user_info.items():
                csv_writer.writerow(user_data)


def launch_media_index():
    first_launch_dirs()
    print(pyfiglet.figlet_format("MEDIA_INDEX", font="cybermedium"))
    separator()
    print("1) SEARCH DATABASE")
    print()
    print("0) EXIT")
    separator()
    lmi_input = input("ENTER #")
    separator()
    lmi_input_action = int(lmi_input)
    if lmi_input_action == 1:
        walk_directories_and_create_indices(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                            tv_alt_dir_input)
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


def walk_directories_and_create_indices(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                        tv_alt_dir_input):
    movie_all_files_results = []
    movie_video_files_results = []

    if movie_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_dir_input):
            for movie_file in sorted(files):
                if movie_file.lower().endswith(all_extensions):
                    movie_all_files_results.append([root + '/' + movie_file])
                if movie_file.lower().endswith(video_extensions):
                    movie_video_files_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(all_extensions):
                    movie_all_files_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(video_extensions):
                    movie_video_files_results.append([root + '/' + alt_file])

    with open(os.path.expanduser((media_index_folder + '/MOVIE_INDEX_ALL_FILES.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_all_files_results):
            csv_writer.writerow(movie_row)

    with open(os.path.expanduser((media_index_folder + '/MOVIE_INDEX_VIDEO_FILES.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_video_files_results):
            csv_writer.writerow(movie_row)

    tv_show_all_files_results = []
    tv_show_video_files_results = []

    if tv_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_dir_input):
            for tv_file in sorted(files):
                if tv_file.lower().endswith(all_extensions):
                    tv_show_all_files_results.append([root + '/' + tv_file])
                if tv_file.lower().endswith(video_extensions):
                    tv_show_video_files_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(all_extensions):
                    tv_show_all_files_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(video_extensions):
                    tv_show_video_files_results.append([root + '/' + alt_file])

    with open(os.path.expanduser((media_index_folder + '/TV_INDEX_ALL_FILES.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_all_files_results):
            csv_writer.writerow(tv_row)

    with open(os.path.expanduser((media_index_folder + '/TV_INDEX_VIDEO_FILES.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_video_files_results):
            csv_writer.writerow(tv_row)


launch_media_index()
