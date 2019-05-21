import csv
import os
import pathlib
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


def change_directory_selection():
    print(pyfiglet.figlet_format("CHANGE_DIRECTORY", font="cybermedium"))
    separator()

    directory_selection()


def directory_selection():
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input

    user_info_file = os.path.expanduser((media_index_folder + '/{0}_USER_INFO.csv').format(username_input))

    print("ENTER PATH OF MOVIE DIRECTORY:")
    movie_dir_input = tk_gui_file_browser_window()
    print()
    print("ENTER PATH OF TV DIRECTORY:")
    tv_dir_input = tk_gui_file_browser_window()
    print()
    print("ENTER PATH OF ALTERNATE MOVIE DIRECTORY, IF NONE HIT CANCEL:")
    movie_alt_dir_input = tk_gui_file_browser_window()
    print()
    print("ENTER PATH OF ALTERNATE TV DIRECTORY, IF NONE HIT CANCEL:")
    tv_alt_dir_input = tk_gui_file_browser_window()
    separator()

    user_info_dict = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                      'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}

    with open(user_info_file, 'w', encoding='UTF8', newline='') as f:
        csv_writer = csv.writer(f)
        for user_data in user_info_dict.items():
            csv_writer.writerow(user_data)


def launch_media_index():
    print(pyfiglet.figlet_format("MEDIA_INDEX", font="cybermedium"))
    separator()

    global username_input

    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    separator()

    username_check_and_folder_creation()


def library_total_amount():
    media_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF8')))
    tv_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_VIDEO_FILES_PATHS.csv').format(username_input)), encoding='UTF8')))

    tv_amounts_list = []
    episode_amounts_list = []
    movie_amounts_list = []

    for counted_movie_title in media_index_list:
        if str("MOVIE") in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)

    for counted_tv_title in media_index_list:
        if str("TV") in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)

    for counted_episode_titles in tv_index_list:
        episode_amounts_list.append(+1)

    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    separator()
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    separator()
    print()
    print("TOTAL AMOUNT OF ITEMS IN MEDIA-LIBRARY:")
    print()
    print(len(movie_amounts_list) + len(episode_amounts_list))
    separator()


def media_index_home():
    username_check_and_folder_creation()
    print(pyfiglet.figlet_format("MEDIA_INDEX", font="cybermedium"))
    separator()

    print("1) ADD DATABASE DIRECTORIES   -   2) CHANGE DATABASE DIRECTORIES")
    print()
    print("3) CREATE PATH INDICES        -   4) CREATE TITLE INDEX")
    print()
    print("5) DISPLAY LIBRARY TOTALS     -   6) TERMINAL GRAPH OPTIONS")
    print()
    print("0) EXIT")
    separator()

    lmi_input = input("ENTER #")
    separator()
    lmi_input_action = int(lmi_input)

    if lmi_input_action == 0:
        exit()
    elif lmi_input_action == 1:
        walk_directories_and_create_indices(movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
    elif lmi_input_action == 2:
        change_directory_selection()
    elif lmi_input_action == 3:
        walk_directories_and_create_indices(movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
    elif lmi_input_action == 4:
        scrape_media_folders_info_for_csv(movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
    elif lmi_input_action == 5:
        library_total_amount()
    elif lmi_input_action == 6:
        run_terminal_graphs()


def run_terminal_graphs():
    print(pyfiglet.figlet_format("TERMINAL_GRAPHS", font="cybermedium"))
    separator()

    print("1) MOVIES (TITLES PER YEAR)         - 2) TV SHOWS (TITLES PER YEAR)")
    print()
    print("3) MOVIES (TITLES PER DECADE)       - 4) TV SHOWS (TITLES PER DECADE)")
    print()
    print("0) MAIN MENU")
    separator()

    terminal_graph_options = input("ENTER #")
    separator()
    terminal_graph_options_int = int(terminal_graph_options)

    if terminal_graph_options_int == 1:
        terminal_graph_options_base(terminal_graph_options_int=1)
    elif terminal_graph_options_int == 2:
        terminal_graph_options_base(terminal_graph_options_int=2)
    elif terminal_graph_options_int == 3:
        terminal_graph_options_base(terminal_graph_options_int=3)
    elif terminal_graph_options_int == 4:
        terminal_graph_options_base(terminal_graph_options_int=4)
    elif terminal_graph_options_int == 0:
        media_index_home()


def separator():
    for lines in "\n", '-' * 100, "\n":
        print(lines)


def scrape_media_folders_info_for_csv(movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input):
    movie_title_items = []
    tv_title_items = []

    if movie_dir_input is not str(''):
        movie_dir_list = os.listdir(movie_dir_input)

        for movie_found in sorted(movie_dir_list):
            movie_scrape_info = guessit.guessit(movie_found)

            title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]

            if "," in title_item_check[2]:
                title_item_check.append(title_item_check[2][-5:-1])
                title_item_check.remove(title_item_check[2])

            movie_title_items.append(title_item_check)

    if movie_alt_dir_input is not str(''):
        movie_alt_dir_list = os.listdir(movie_alt_dir_input)

        for movie_found in sorted(movie_alt_dir_list):
            movie_scrape_info = guessit.guessit(movie_found)

            title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]

            if "," in title_item_check[2]:
                title_item_check.append(title_item_check[2][-5:-1])
                title_item_check.remove(title_item_check[2])

            movie_title_items.append(title_item_check)

    if tv_dir_input is not str(''):
        tv_dir_list = os.listdir(tv_dir_input)

        for tv_found in sorted(tv_dir_list):
            tv_scrape_info = guessit.guessit(tv_found)

            title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]

            if "," in title_item_check[2]:
                title_item_check.append(title_item_check[2][-5:-1])
                title_item_check.remove(title_item_check[2])

            tv_title_items.append(title_item_check)

    if tv_alt_dir_input is not str(''):
        tv_alt_dir_list = os.listdir(tv_alt_dir_input)

        for tv_found in sorted(tv_alt_dir_list):
            tv_scrape_info = guessit.guessit(tv_found)

            title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]

            if "," in title_item_check[2]:
                title_item_check.append(title_item_check[2][-5:-1])
                title_item_check.remove(title_item_check[2])

            tv_title_items.append(title_item_check)

    with open(os.path.expanduser((media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in movie_title_items:
            csv_writer.writerow(file_row)
        for file_row in tv_title_items:
            csv_writer.writerow(file_row)


def terminal_graph_options_base(terminal_graph_options_int):
    media_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF8')))

    movie_years_dict = {}
    movie_decades_dict = {}
    tv_years_dict = {}
    tv_decades_amount_dict = {}

    movie_year_totals_dict = {}
    movie_decades_totals_dict = {}
    tv_year_totals_dict = {}
    tv_decades_totals_dict = {}

    for title_item in media_index_list:
        title_item_year = re.split("(.+) \((\d{4})\)", title_item[2], flags=0)
        title_item_year_int = int(title_item_year[0])
        title_item_decade_int = int(title_item_year[0][:-1] + '0')

        if title_item_year_int in range(1900, 2100, 1):
            if str("MOVIE") in title_item:

                if title_item_year_int not in movie_years_dict:
                    movie_years_dict[title_item_year_int] = []
                movie_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in movie_decades_dict:
                    movie_decades_dict[title_item_decade_int] = []
                movie_decades_dict[title_item_decade_int].append(title_item)

            if str("TV") in title_item:
                if title_item_year_int not in tv_years_dict:
                    tv_years_dict[title_item_year_int] = []
                tv_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in tv_decades_amount_dict:
                    tv_decades_amount_dict[title_item_decade_int] = []
                tv_decades_amount_dict[title_item_decade_int].append(title_item)

    if terminal_graph_options_int == 1:

        for movie_year_values, value in sorted(movie_years_dict.items()):
            movie_year_totals_dict[movie_year_values] = len(value)
        movie_data = sorted(movie_year_totals_dict.items())

        movie_years_terminal_graph_list = []

        for key, value in movie_data:
            movie_years_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()

        for line in graph.graph('MOVIES: YEAR AMOUNTS', movie_years_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 2:

        for tv_year_values, value in sorted(tv_years_dict.items()):
            tv_year_totals_dict[tv_year_values] = len(value)
        tv_data = sorted(tv_year_totals_dict.items())

        tv_years_terminal_graph_list = []

        for key, value in tv_data:
            tv_years_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: YEAR AMOUNTS', tv_years_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 3:

        for movie_year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals_dict[movie_year_values] = len(value)

        movie_decades_terminal_graph_list = []

        for key, value in movie_decades_totals_dict.items():
            movie_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: DECADE AMOUNTS', movie_decades_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 4:

        for tv_year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals_dict[tv_year_values] = len(value)

        tv_decades_terminal_graph_list = []

        for key, value in tv_decades_totals_dict.items():
            tv_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: DECADE AMOUNTS', tv_decades_terminal_graph_list):
            print()
            print(line)
        separator()


def tk_gui_file_browser_window():
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    root.destroy()
    return selected_directory


def username_check_and_folder_creation():
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input

    user_info_file = os.path.expanduser((media_index_folder + '/{0}_USER_INFO.csv').format(username_input))

    if os.path.isfile(user_info_file):
        user_info_file_check = list(csv.reader(open(user_info_file)))
        movie_dir_input = user_info_file_check[1][1]
        tv_dir_input = user_info_file_check[2][1]
        movie_alt_dir_input = user_info_file_check[3][1]
        tv_alt_dir_input = user_info_file_check[4][1]
    else:
        os.makedirs(os.path.expanduser((media_index_folder + '/').format(username_input)), exist_ok=True)
        os.makedirs(os.path.expanduser((media_index_folder + '/FILES').format(username_input)), exist_ok=True)

        directory_selection()


def walk_directories_and_create_indices(movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input):
    movie_video_files_results = []

    if movie_dir_input is not str(''):
        for root, dirs, files in os.walk(movie_dir_input):
            for movie_file in sorted(files):
                if movie_file.lower().endswith(video_extensions):
                    movie_video_files_results.append([(pathlib.Path(root) / movie_file).as_posix()])

    if movie_alt_dir_input is not str(''):
        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(video_extensions):
                    movie_video_files_results.append([(pathlib.Path(root) / alt_file).as_posix()])

    with open(os.path.expanduser((media_index_folder + '/MOVIE_VIDEO_FILES_PATHS.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_video_files_results):
            csv_writer.writerow(movie_row)

    tv_show_video_files_results = []

    if tv_dir_input is not str(''):
        for root, dirs, files in os.walk(tv_dir_input):
            for tv_file in sorted(files):
                if tv_file.lower().endswith(video_extensions):
                    tv_show_video_files_results.append([(pathlib.Path(root) / tv_file).as_posix()])

    if tv_alt_dir_input is not str(''):
        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(video_extensions):
                    tv_show_video_files_results.append([(pathlib.Path(root) / alt_file).as_posix()])

    with open(os.path.expanduser((media_index_folder + '/TV_VIDEO_FILES_PATHS.csv').format(username_input)), "w",
              encoding='UTF8', newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_video_files_results):
            csv_writer.writerow(tv_row)


launch_media_index()

while True:
    media_index_home()
