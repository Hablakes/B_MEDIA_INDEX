import csv
import os
import re

from ascii_graph import Pyasciigraph
import guessit
import matplotlib.pylab as plt
import numpy as np
import pymediainfo

username_input = []
movie_dir_input = []
tv_dir_input = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")


def first_launch_media_index():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("IS THIS THE FIRST TIME RUNNING THE INDEX ON THIS DB?   -   1) YES - 2) NO            - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    first_lmi_input_action = input("ENTER #")
    first_lmi_input_action_lower = int(first_lmi_input_action.lower())
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    if first_lmi_input_action_lower == 1:
        pass
    elif first_lmi_input_action_lower == 2:
        pass
    elif first_lmi_input_action_lower == 3:
        exit()


def first_launch_username():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    username_input.append(input("ENTER YOUR USERNAME (CASE-SENSITIVE):"))

    os.makedirs(r'/home/' + username_input[0] + '/MEDIA-INDEX/', exist_ok=True)

    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as media_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as movie_files_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tv_files_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as movie_files_results_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tv_files_results_csv:
        pass


def first_launch_dirs():
    first_launch_username()
    movie_dir_input.append(input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):"))
    tv_dir_input.append(input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):"))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("OK, THAT'S ALL WE NEED FOR NOW, THIS MAY TAKE AWHILE (DEPENDING ON THE SIZE OF YOUR LIBRARY)")
    print()
    print("PROCEED?   -   1) YES - 2) NO")
    first_launch_action = input()
    first_launch_action_lower = int(first_launch_action.lower())
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    if first_launch_action_lower == 1:
        pass
        pass
        launch_media_index()
    elif first_launch_action_lower == 2:
        exit()


def second_launch_lmi():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    username_input.append(input("ENTER YOUR USERNAME (CASE-SENSITIVE):"))
    movie_dir_input.append(input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):"))
    tv_dir_input.append(input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):"))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    launch_media_index()


def launch_media_index():
    print("___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("|__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/")
    print("|__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) QUERIES - 2) SORTING - 3) FILE DATA/INFO - 4) GRAPHS - 5) TOTALS - 6) INDEXING    - 0) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    lmi_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    lmi_action = int(lmi_action)
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


def run_query():
    print("___     _  _ ____ ___  _ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |\/| |___ |  \ | |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |  | |___ |__/ | |  |    |_\| |__| |___ |  \   |   ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("SEARCH TITLES - 1) MOVIES - 2) TV SHOWS                                              - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    title_search_type = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    title_search_type_lower = int(title_search_type)
    if title_search_type_lower == 1:
        pass
    elif title_search_type_lower == 2:
        pass
    elif title_search_type_lower == 3:
        launch_media_index()


def run_sort():
    print("___     _  _ ____ ___  _ ____    ____ ____ ____ ___")
    print("|__] __ |\/| |___ |  \ | |__| __ [__  |  | |__/  |")
    print("|__]    |  | |___ |__/ | |  |    ___] |__| |  \  | ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("TITLE - 1) ASCENDING - 2) DESCENDING - YEAR - 3) ASCENDING - 4) DESCENDING           - 5) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    sort_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    sort_options = int(sort_options)
    if sort_options == 1:
        pass
    elif sort_options == 2:
        pass
    elif sort_options == 3:
        pass
    elif sort_options == 4:
        pass
    elif sort_options == 5:
        launch_media_index()


def file_query_and_sort():
    print("___     ____ _ _    ____    ___  ____ ___ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |___ | |    |___ __ |  \ |__|  |  |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |    | |___ |___    |__/ |  |  |  |  |    |_\| |__| |___ |  \   |")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("SEARCH TITLES - 1) MOVIES - 2) TV SHOWS                                              - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    data_query_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    data_query_options = int(data_query_options)
    if data_query_options == 1:
        pass
    elif data_query_options == 2:
        pass
    elif data_query_options == 3:
        launch_media_index()


def run_graphs():
    print("___     ____ ____ ____ ___  _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | __ |__/ |__| |__] |__| __ |  | |__]  |  | |  | |\ | [__")
    print("|__]    |__] |  \ |  | |    |  |    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) PICTURE GRAPHS (MAT-PLOT-LIB)    - 2) TERMINAL GRAPHS (ASCII-CHART)               - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = int(graph_options)
    if graph_options == 1:
        pass
    elif graph_options == 2:
        pass
    elif graph_options == 3:
        launch_media_index()


def run_picture_graphs():
    print("___     ___  _ ____ ___ _  _ ____ ____    ____ ____ ____ ___  _  _ ____")
    print("|__] __ |__] | |     |  |  | |__/ |___ __ | __ |__/ |__| |__] |__| [__")
    print("|__]    |    | |___  |  |__| |  \ |___    |__] |  \ |  | |    |  | ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) MOVIES (TITLES PER YEAR)         - 2) TV SHOWS (TITLES PER YEAR)")
    print()
    print("3) MOVIES (TITLES PER DECADE)       - 4) TV SHOWS (TITLES PER DECADE)")
    print()
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)          - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = int(graph_options)
    if graph_options == 1:
        pass
    elif graph_options == 2:
        pass
    elif graph_options == 3:
        pass
    elif graph_options == 4:
        pass
    elif graph_options == 5:
        pass
    elif graph_options == 6:
        pass
    elif graph_options == 7:
        launch_media_index()


def run_terminal_graphs():
    print("___     ___ ____ ____ _  _ _ _  _ ____ _       ____ ____ ____ ___  _  _ ____")
    print("|__] __  |  |___ |__/ |\/| | |\ | |__| |    __ | __ |__/ |__| |__] |__| [__")
    print("|__]     |  |___ |  \ |  | | | \| |  | |___    |__] |  \ |  | |    |  | ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) MOVIES (TITLES PER YEAR)         - 2) TV SHOWS (TITLES PER YEAR)")
    print()
    print("3) MOVIES (TITLES PER DECADE)       - 4) TV SHOWS (TITLES PER DECADE)")
    print()
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)          - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = int(graph_options)
    if graph_options == 1:
        pass
    elif graph_options == 2:
        pass
    elif graph_options == 3:
        pass
    elif graph_options == 4:
        pass
    elif graph_options == 5:
        pass
    elif graph_options == 6:
        pass
    elif graph_options == 7:
        launch_media_index()


def totals_query():
    print("___     ___ ____ ___ ____ _    ____    ____ _  _ ____ ____ _   _")
    print("|__] __  |  |  |  |  |__| |    [__  __ |  | |  | |___ |__/  \_/ ")
    print("|__]     |  |__|  |  |  | |___ ___]    |_\| |__| |___ |  \   |   ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) MOVIES BY YEAR        - 2) MOVIES BY DECADE        - 3) MOVIES TOTAL")
    print()
    print("4) TV SHOWS BY YEAR      - 5) TV SHOWS BY DECADE      - 6) TV SHOWS TOTALS           - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    b_totals_query_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    b_totals_query_action = int(b_totals_query_action)
    if b_totals_query_action == 1:
        pass
    elif b_totals_query_action == 2:
        pass
    elif b_totals_query_action == 3:
        pass
    elif b_totals_query_action == 4:
        pass
    elif b_totals_query_action == 5:
        pass
    elif b_totals_query_action == 6:
        pass
    elif b_totals_query_action == 7:
        launch_media_index()


def create_media_indices_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX FROM DIRECTORIES - 2) CREATE NEW MEDIA INDEX FROM FILES    - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_action)
    if cmi_action == 1:
        pass
    elif cmi_action == 2:
        pass
    elif cmi_action == 3:
        launch_media_index()
