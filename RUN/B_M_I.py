import csv
import os
import re
import textwrap

import guessit
import pymediainfo

import matplotlib.pylab as plt
import numpy as np

from ascii_graph import Pyasciigraph

all_extens = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm", ".nfo", ".srt")

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

nfo_extensions = ".nfo"
srt_extensions = ".srt"

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")


username_input = None


def first_launch_dirs():

    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input
    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    if username_input == 'bx':
        user_info_file = list(csv.reader(open(
            r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input + '-USER-INFO.csv')))
        movie_dir_input = user_info_file[1][1]
        tv_dir_input = user_info_file[2][1]
        movie_alt_dir_input = user_info_file[3][1]
        tv_alt_dir_input = user_info_file[4][1]
    else:
        movie_dir_input = input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):")
        tv_dir_input = input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):")
        movie_alt_dir_input = input(
            "ENTER PATH OF ANY ALTERNATE MOVIE DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
        tv_alt_dir_input = input(
            "ENTER PATH OF ANY ALTERNATE TV SHOW DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        user_info = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                     'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}
        with open(
                r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input + '-USER-INFO.csv',
                'w') as f:
            csv_writer = csv.writer(f)
            for row in user_info.items():
                csv_writer.writerow(row)
        os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/', exist_ok=True)
        os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES', exist_ok=True)

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', 'w'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', 'w'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-FILES-INDEX.csv'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-NFO-FILES-INDEX.csv'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w'):
            pass
        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w'):
            pass


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
    lmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    lmi_action = int(lmi_input)
    if lmi_action == 1:
        run_query()
    elif lmi_action == 2:
        run_sort()
    elif lmi_action == 3:
        run_file_query_and_sort()
    elif lmi_action == 4:
        run_graphs()
    elif lmi_action == 5:
        totals_query()
    elif lmi_action == 6:
        create_media_indices_all()
    elif lmi_action == 0:
        exit()


def run_query():
    print("___     _  _ ____ ___  _ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |\/| |___ |  \ | |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |  | |___ |__/ | |  |    |_\| |__| |___ |  \   |   ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("SEARCH TITLES         -   1) MOVIES - 2) TV SHOW SERIES")
    print()
    print("SEARCH FOR PLOTS OF   -   3) MOVIES - 4) TV SHOW SERIES & EPISODES                   - 5) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    title_search_type = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    title_search_type_lower = int(title_search_type)
    if title_search_type_lower == 1:
        movie_title_search(username_input)
    elif title_search_type_lower == 2:
        tv_title_search(username_input)
    elif title_search_type_lower == 3:
        movie_nfo_search_plot_results(username_input)
    elif title_search_type_lower == 4:
        pass
    elif title_search_type_lower == 5:
        launch_media_index()


def movie_title_search(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_title_search_action = input("QUERY MOVIES:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    movie_title_search_action = movie_title_search_action.lower()
    print("SEARCH RESULTS:")
    print()
    print("MOVIES:")
    print()
    for movie_search_result in media_index_list:
        if movie_string in movie_search_result[0]:
            movie_search_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result), flags=0)
            if movie_title_search_action in movie_search_info[0].lower():
                print(movie_search_info[0])
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def tv_title_search(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_title_search_action = input("QUERY TV SHOWS:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    tv_title_search_action = tv_title_search_action.lower()
    print()
    print()
    print("SEARCH RESULTS:")
    print()
    print("TV SHOWS:")
    print()
    for tv_search_result in media_index_list:
        if tv_string in tv_search_result[0]:
            tv_search_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result), flags=0)
            if tv_title_search_action in tv_search_info[0].lower():
                print(tv_search_info[0])
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def movie_nfo_search_plot_results(username_input):
    movie_nfos = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-INDEX.csv'))
    movie_nfo_files_results = []
    movie_nfo_result = []

    print("SEARCH FOR MOVIE PLOT DESCRIPTION:")
    print()
    nfo_file = input("ENTER TITLE:")
    print()

    for nfo_files_index in movie_nfos:
        for nfo_files in nfo_files_index:
            if nfo_file.lower() in nfo_files.lower():
                movie_nfo_files_results.append(nfo_files)

    if int(len(movie_nfo_files_results)) == 1:
        with open(movie_nfo_files_results[0]) as f:
            for line in f.readlines():
                if '<plot>' in line:
                    movie_nfo_result.append(line.split('.'))
        print("------------------------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------------------------")
        print()
        for line in movie_nfo_result[0]:
            print(line + '.')
        print()
        print("------------------------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------------------------")
        print()
        print("SEARCH AGAIN?   -   1) YES - 2) NO")
        print()
        sa_input = int(input('ENTER #'))
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        if int(sa_input) == 1:
            movie_nfo_search_plot_results(username_input)
        else:
            pass

    elif int(len(movie_nfo_files_results)) == 0:
        print("NO MATCHES")
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("SEARCH AGAIN?   -   1) YES - 2) NO")
        print()
        sa_input = int(input('ENTER #'))
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        if int(sa_input) == 1:
            movie_nfo_search_plot_results(username_input)
        else:
            pass

    elif int(len(movie_nfo_files_results)) > 1:
        for line in movie_nfo_files_results:
            print(line)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
        print("REFINE SEARCH WITH ABOVE RESULTS: SINGLE MATCH NEEDED TO PROCEED")
        print()
        print("--------------------------------------------------------------------------------------------------")
        movie_nfo_search_plot_results(username_input)


def run_sort():
    print("___     _  _ ____ ___  _ ____    ____ ____ ____ ___")
    print("|__] __ |\/| |___ |  \ | |__| __ [__  |  | |__/  |")
    print("|__]    |  | |___ |__/ | |  |    ___] |__| |  \  | ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("MOVIES & TV SHOWS TITLES  -   TITLE - 1) ASCENDING - 2) DESCENDING")
    print()
    print("MOVIES & TV SHOWS TITLES  -    YEAR - 3) ASCENDING - 4) DESCENDING")
    print()
    print("TV SHOW - EPISODES -          TITLE - 5) ASCENDING - 6) DESCENDING")
    print()
    print("TV SHOW - EPISODES -       EPISODES - 7) ASCENDING - 8) DESCENDING                   - 9) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    sort_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global sort_options_int
    sort_options_int = int(sort_input)
    if sort_options_int == 1:
        sort_function_base(username_input, sort_options_int=1)
    elif sort_options_int == 2:
        sort_function_base(username_input, sort_options_int=2)
    elif sort_options_int == 3:
        sort_function_base(username_input, sort_options_int=3)
    elif sort_options_int == 4:
        sort_function_base(username_input, sort_options_int=4)
    elif sort_options_int == 5:
        total_tv_episodes_sort_function_base(username_input, sort_options_int=5)
    elif sort_options_int == 6:
        total_tv_episodes_sort_function_base(username_input, sort_options_int=6)
    elif sort_options_int == 7:
        total_tv_episodes_sort_function_base(username_input, sort_options_int=7)
    elif sort_options_int == 8:
        total_tv_episodes_sort_function_base(username_input, sort_options_int=8)
    elif sort_options_int == 9:
        launch_media_index()


def sort_function_base(username_input, sort_options_int):
    media_index = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    sorted_year = sorted(media_index, key=lambda x: (x[0], x[2]))
    sorted_year_r = sorted(media_index, key=lambda x: (x[0], x[2]), reverse=True)
    if sort_options_int == 1:
        for title_item in sorted_title:
            print(title_item)
    elif sort_options_int == 2:
        for title_item in sorted_title_r:
            print(title_item)
    elif sort_options_int == 3:
        for title_item in sorted_year:
            print(title_item)
    elif sort_options_int == 4:
        for title_item in sorted_year_r:
            print(title_item)


def total_tv_episodes_sort_function_base(username_input, sort_options_int):
    tv_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}
    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        tv_show_episodes_found.append(found_tv_title)
        tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)
    sorted_by_key_d = sorted(tv_show_found.items(), key=lambda kv: kv[0])
    sorted_by_key_a = sorted(tv_show_found.items(), key=lambda kv: kv[0], reverse=True)
    sorted_by_value_d = sorted(tv_show_found.items(), key=lambda kv: kv[1])
    sorted_by_value_a = sorted(tv_show_found.items(), key=lambda kv: kv[1], reverse=True)
    if sort_options_int == 5:
        for item in sorted_by_key_d:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 6:
        for item in sorted_by_key_a:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 7:
        for item in sorted_by_value_d:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 8:
        for item in sorted_by_value_a:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()


def run_file_query_and_sort():
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
    data_query_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    data_query_int = int(data_query_input)
    if data_query_int == 1:
        movie_query_all_results(username_input)
    elif data_query_int == 2:
        tv_query_all_results(username_input)
    elif data_query_int == 3:
        launch_media_index()


def movie_query_all_results(username_input):
    mv_files_results_list = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-RESULTS.csv'))

    mv_query_action = input("ENTER SEARCH QUERY (MOVIES):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    mv_query_action_lower = str(mv_query_action.lower())

    for movie_file in mv_files_results_list:

        if mv_query_action_lower in movie_file[1].lower():

            print()
            print()
            print("MOVIE FOLDER")
            print()
            print(movie_file[0])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("MOVIE TITLE")
            print()
            print(movie_file[1])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("MOVIE YEAR")
            print()
            print(movie_file[2])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("MOVIE RESOLUTION")
            print()
            print(movie_file[3])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("MOVIE FILE-TYPE")
            print()
            print(movie_file[4])
            print("--------------------------------------------------------------------------------------------------")

            if int(len(movie_file[6])) != 0:

                print("RATING")
                print()
                mv_rating = re.findall("<rating>(.*?)</rating>", movie_file[6])
                print(mv_rating[0])
                print()
                print("-------------------------------------------------"
                      "-------------------------------------------------")
                print()

            if int(len(movie_file[5])) != 0:

                    print("PLOT")
                    print()
                    if '</plot>' not in movie_file[5]:
                        mv_plot = re.findall("<plot>(.*?)", movie_file[5])
                        print(textwrap.fill(mv_plot[0], 80))
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

                    elif "</plot>" in movie_file[5]:
                        mv_plot = re.findall("<plot>(.*?)</plot>", movie_file[5])
                        print(textwrap.fill(mv_plot[0], 80))
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()


def tv_query_all_results(username_input):
    tv_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-RESULTS.csv')))

    tv_show_query_action = input("ENTER SEARCH QUERY (TV SHOWS):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    tv_show_query_action_lower = str(tv_show_query_action.lower())

    for tv_file in tv_files_results_list:

        if tv_show_query_action_lower in tv_file[1].lower():

            print()
            print()
            print("TV SHOW FOLDER")
            print()
            print(tv_file[0])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW TITLE")
            print()
            print(tv_file[1])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW YEAR")
            print()
            print(tv_file[2])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW EPISODE TITLE")
            print()
            print(tv_file[3])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("SEASON NUMBER")
            print()
            print(tv_file[4])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("EPISODE NUMBER")
            print()
            print(tv_file[5])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("RESOLUTION")
            print()
            print(tv_file[6])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("FILE-TYPE")
            print()
            print(tv_file[7])
            print("--------------------------------------------------------------------------------------------------")
            print()
            if int(len(tv_file[9])) != 0:

                print("RATING")
                print()
                tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                print(tv_rating[0])
                print()
                print("-------------------------------------------------"
                      "-------------------------------------------------")
                print()

            if int(len(tv_file[8])) != 0:

                    print("PLOT")
                    print()
                    if '</plot>' not in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)", tv_file[8])
                        print(textwrap.fill(tv_plot[0], 80))
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

                    elif "</plot>" in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                        print(textwrap.fill(tv_plot[0], 80))
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

        elif tv_show_query_action_lower in tv_file[3].lower():

            print()
            print()
            print("TV SHOW FOLDER")
            print()
            print(tv_file[0])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW TITLE")
            print()
            print(tv_file[1])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW YEAR")
            print()
            print(tv_file[2])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW EPISODE TITLE")
            print()
            print(tv_file[3])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("SEASON NUMBER")
            print()
            print(tv_file[4])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("EPISODE NUMBER")
            print()
            print(tv_file[5])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("RESOLUTION")
            print()
            print(tv_file[6])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("FILE-TYPE")
            print()
            print(tv_file[7])
            print("--------------------------------------------------------------------------------------------------")
            print()
            if int(len(tv_file[9])) != 0:

                print("RATING")
                print()
                tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                print(tv_rating[0])
                print()
                print("-------------------------------------------------"
                      "-------------------------------------------------")
                print()

            if int(len(tv_file[8])) != 0:

                    print("PLOT")
                    print()
                    if '</plot>' not in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)", tv_file[8])
                        print(tv_plot)
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

                    elif "</plot>" in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                        print(tv_plot[0])
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()


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
    graph_options_int = int(graph_options)
    if graph_options_int == 1:
        run_picture_graphs()
    elif graph_options_int == 2:
        run_terminal_graphs()
    elif graph_options_int == 3:
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
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)")
    print()
    print("7) MOVIES (FILE-TYPE AMOUNTS)       - 8) TV SHOWS (FILE-TYPE AMOUNTS)                - 9) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    picture_graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global picture_graph_options_int
    picture_graph_options_int = int(picture_graph_options)
    if picture_graph_options_int == 1:
        bar_graph_options_base(username_input, picture_graph_options_int=1)
    elif picture_graph_options_int == 2:
        bar_graph_options_base(username_input, picture_graph_options_int=2)
    elif picture_graph_options_int == 3:
        bar_graph_options_base(username_input, picture_graph_options_int=3)
    elif picture_graph_options_int == 4:
        bar_graph_options_base(username_input, picture_graph_options_int=4)
    elif picture_graph_options_int == 5:
        pie_chart_options_base(username_input, picture_graph_options_int=5)
    elif picture_graph_options_int == 6:
        pie_chart_options_base(username_input, picture_graph_options_int=6)
    elif picture_graph_options_int == 7:
        search_file_type_totals_movies(username_input, picture_graph_options_int=7,
                                       terminal_graph_options_int='', b_totals_query_input_int='')
    elif picture_graph_options_int == 8:
        search_file_type_totals_tv(username_input, picture_graph_options_int=8,
                                   terminal_graph_options_int='', b_totals_query_input_int='')
    elif picture_graph_options_int == 9:
        launch_media_index()


def bar_graph_options_base(username_input, picture_graph_options_int):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_dict = {}
    movie_decades_dict = {}
    tv_decades_amount_dict = {}
    tv_years_dict = {}
    movie_year_totals = {}
    movie_decades_totals = {}
    tv_year_totals = {}
    tv_decades_totals = {}

    for title_item in media_index_list:
        title_item_year = re.split("(.+) \((\d{4})\)", title_item[2], flags=0)
        title_item_year_int = int(title_item_year[0])
        title_item_decade_int = int(title_item_year[0][:-1] + '0')
        if title_item_year_int in years_range:
            if movie_string in title_item:
                if title_item_year_int not in movie_years_dict:
                    movie_years_dict[title_item_year_int] = []
                movie_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in movie_decades_dict:
                    movie_decades_dict[title_item_decade_int] = []
                movie_decades_dict[title_item_decade_int].append(title_item)
            if tv_string in title_item:
                if title_item_year_int not in tv_years_dict:
                    tv_years_dict[title_item_year_int] = []
                tv_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in tv_decades_amount_dict:
                    tv_decades_amount_dict[title_item_decade_int] = []
                tv_decades_amount_dict[title_item_decade_int].append(title_item)

    if picture_graph_options_int == 1:

        for year_values, value in sorted(movie_years_dict.items()):
            movie_year_totals[year_values] = len(value)
        x, y = zip(*sorted(movie_year_totals.items()))
        plt.bar(x, y)
        plt.savefig(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/MOVIE-YEAR-RESULTS.png')
        plt.show()

    if picture_graph_options_int == 2:

        for year_values, value in sorted(tv_years_dict.items()):
            tv_year_totals[year_values] = len(value)
        x, y = zip(*sorted(tv_year_totals.items()))
        plt.bar(x, y)
        plt.savefig(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/TV-YEAR-RESULTS.png')
        plt.show()

    if picture_graph_options_int == 3:

        for year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals[year_values] = len(value)
        x, y = zip(*movie_decades_totals.items())
        plt.bar(x, y, width=5)
        plt.savefig(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/MOVIE-DECADE-RESULTS.png')
        plt.show()

    if picture_graph_options_int == 4:

        for year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals[year_values] = len(value)
        x, y = zip(*tv_decades_totals.items())
        plt.bar(x, y, width=5)
        plt.savefig(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/TV-DECADE-RESULTS.png')
        plt.show()


def pie_chart_options_base(username_input, picture_graph_options_int):
    movie_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    tv_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))

    m_ten_eighty_found_list = []
    m_seven_twenty_found_list = []
    m_standard_def_found_list = []
    m_empty_response_list = []
    movies_total_list = []

    tv_ten_eighty_found_list = []
    tv_seven_twenty_found_list = []
    tv_standard_def_found_list = []
    tv_empty_response_list = []
    tv_total_list = []

    for res in movie_files_results_list:

        if re.findall("19\d{2}x", res[2]):
            m_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[2]):
            m_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[2]):
            m_standard_def_found_list.append(res)
        else:
            m_empty_response_list.append(+1)
        movies_total_list.append(+1)

    movie_data = [float(len(m_ten_eighty_found_list)), float(len(m_seven_twenty_found_list)),
                  float(len(m_standard_def_found_list))]

    for res in tv_files_results_list:

        if re.findall("19\d{2}x", res[6]):
            tv_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[6]):
            tv_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[6]):
            tv_standard_def_found_list.append(res)
        else:
            tv_empty_response_list.append(+1)
        tv_total_list.append(+1)

    tv_data = [float(len(tv_ten_eighty_found_list)), float(len(tv_seven_twenty_found_list)),
               float(len(tv_standard_def_found_list))]

    def format_data(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    labels = ['1080p', '720p', 'SD (Below 720p)']

    colors = ['#85c1e9', '#a569bd', '#808b96']

    if picture_graph_options_int == 5:
        fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

        wedges, texts, autotexts = ax.pie(movie_data, autopct=lambda pct: format_data(pct, movie_data),
                                          shadow=True, colors=colors, textprops=dict(color="black"))

        ax.legend(wedges, labels,
                  title="RESOLUTIONS",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=9, weight='bold')
        ax.set_title("MOVIE-RESOLUTION-RESULTS")
        plt.savefig(
            r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/MOVIE-RESOLUTION-RESULTS.png')
        plt.show()

    if picture_graph_options_int == 6:
        fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

        wedges, texts, autotexts = ax.pie(tv_data, autopct=lambda pct: format_data(pct, tv_data),
                                          shadow=True, colors=colors, textprops=dict(color="black"))

        ax.legend(wedges, labels,
                  title="RESOLUTIONS",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=9, weight='bold')
        ax.set_title("TV-SHOW-RESOLUTION-RESULTS")
        plt.savefig(
            r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/TV-SHOW-RESOLUTION-RESULTS.png')
        plt.show()


def search_file_type_totals_movies(username_input, b_totals_query_input_int, picture_graph_options_int,
                                   terminal_graph_options_int):
    movie_file_index = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    extensions_dict = {}
    extensions_totals = {}

    for file_type in movie_file_index:
        if str(',') not in file_type[3]:
            if file_type[3] not in extensions_dict:
                extensions_dict[file_type[3]] = []
            extensions_dict[file_type[3]].append(file_type[3])
    movie_file_type_totals = {}

    if b_totals_query_input_int == 7:

        for movie_file_type_values, value in sorted(extensions_dict.items()):
            movie_file_type_totals[movie_file_type_values] = len(value)
        print()
        print("TOTAL AMOUNTS OF FILE-TYPES IN MOVIES:")
        print()
        print(movie_file_type_totals)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()

    if picture_graph_options_int == 7:

        for movie_file_type_values, value in sorted(extensions_dict.items()):
            movie_file_type_totals[movie_file_type_values] = len(value)

        x, y = zip(*sorted(movie_file_type_totals.items()))
        plt.bar(x, y)
        plt.savefig(
            r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/MOVIE-FILETYPE-RESULTS.png')
        plt.show()

    if terminal_graph_options_int == 7:

        for file_type_values, value in sorted(extensions_dict.items()):
            extensions_totals[file_type_values] = len(value)

        file_type_totals_terminal_graph_list = []

        for key, value in extensions_totals.items():
            file_type_totals_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: FILE-TYPE AMOUNTS', file_type_totals_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()


def search_file_type_totals_tv(username_input, b_totals_query_input_int, picture_graph_options_int,
                               terminal_graph_options_int):
    tv_file_index = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    extensions_dict = {}
    extensions_totals = {}

    for file_type in tv_file_index:
        if str(',') not in file_type[7]:
            if file_type[7] not in extensions_dict:
                extensions_dict[file_type[7]] = []
            extensions_dict[file_type[7]].append(file_type[7])
    tv_file_type_totals = {}

    if b_totals_query_input_int == 8:

        for tv_file_type_values, value in sorted(extensions_dict.items()):
            tv_file_type_totals[tv_file_type_values] = len(value)
        print()
        print("TOTAL AMOUNTS OF FILE-TYPES IN TV SHOWS:")
        print()
        print(tv_file_type_totals)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()

    if picture_graph_options_int == 8:

        for tv_file_type_values, value in sorted(extensions_dict.items()):
            tv_file_type_totals[tv_file_type_values] = len(value)

        x, y = zip(*sorted(tv_file_type_totals.items()))
        plt.bar(x, y)
        plt.savefig(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES/TV-FILETYPE-RESULTS.png')
        plt.show()

    if terminal_graph_options_int == 8:

        for file_type_values, value in sorted(extensions_dict.items()):
            extensions_totals[file_type_values] = len(value)

        file_type_totals_terminal_graph_list = []

        for key, value in extensions_totals.items():
            file_type_totals_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: FILE-TYPE AMOUNTS', file_type_totals_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()


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
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)")
    print()
    print("7) MOVIES (FILE-TYPE AMOUNTS)       - 8) TV SHOWS (FILE-TYPE AMOUNTS)                - 9) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    terminal_graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global terminal_graph_options_int
    terminal_graph_options_int = int(terminal_graph_options)
    if terminal_graph_options_int == 1:
        terminal_graph_options_base_0(username_input, terminal_graph_options_int=1)
    elif terminal_graph_options_int == 2:
        terminal_graph_options_base_0(username_input, terminal_graph_options_int=2)
    elif terminal_graph_options_int == 3:
        terminal_graph_options_base_0(username_input, terminal_graph_options_int=3)
    elif terminal_graph_options_int == 4:
        terminal_graph_options_base_0(username_input, terminal_graph_options_int=4)
    elif terminal_graph_options_int == 5:
        terminal_graph_options_base_1(username_input, terminal_graph_options_int=5)
    elif terminal_graph_options_int == 6:
        terminal_graph_options_base_1(username_input, terminal_graph_options_int=6)
    elif terminal_graph_options_int == 7:
        search_file_type_totals_movies(username_input, terminal_graph_options_int=7,
                                       picture_graph_options_int='', b_totals_query_input_int='')
    elif terminal_graph_options_int == 8:
        search_file_type_totals_tv(username_input, terminal_graph_options_int=8,
                                   picture_graph_options_int='', b_totals_query_input_int='')
    elif terminal_graph_options_int == 9:
        launch_media_index()


def terminal_graph_options_base_0(username_input, terminal_graph_options_int):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))

    movie_years_dict = {}
    movie_decades_dict = {}
    tv_decades_amount_dict = {}
    tv_years_dict = {}
    movie_year_totals = {}
    movie_decades_totals = {}
    tv_year_totals = {}
    tv_decades_totals = {}

    for title_item in media_index_list:
        title_item_year = re.split("(.+) \((\d{4})\)", title_item[2], flags=0)
        title_item_year_int = int(title_item_year[0])
        title_item_decade_int = int(title_item_year[0][:-1] + '0')
        if title_item_year_int in years_range:
            if movie_string in title_item:
                if title_item_year_int not in movie_years_dict:
                    movie_years_dict[title_item_year_int] = []
                movie_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in movie_decades_dict:
                    movie_decades_dict[title_item_decade_int] = []
                movie_decades_dict[title_item_decade_int].append(title_item)
            if tv_string in title_item:
                if title_item_year_int not in tv_years_dict:
                    tv_years_dict[title_item_year_int] = []
                tv_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in tv_decades_amount_dict:
                    tv_decades_amount_dict[title_item_decade_int] = []
                tv_decades_amount_dict[title_item_decade_int].append(title_item)

    if terminal_graph_options_int == 1:

        for movie_year_values, value in sorted(movie_years_dict.items()):
            movie_year_totals[movie_year_values] = len(value)
        movie_data = sorted(movie_year_totals.items())

        movie_years_terminal_graph_list = []

        for key, value in movie_data:
            movie_years_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()

        for line in graph.graph('MOVIES: YEAR AMOUNTS', movie_years_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()

    if terminal_graph_options_int == 2:

        for tv_year_values, value in sorted(tv_years_dict.items()):
            tv_year_totals[tv_year_values] = len(value)
        tv_data = sorted(tv_year_totals.items())

        tv_years_terminal_graph_list = []

        for key, value in tv_data:
            tv_years_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: YEAR AMOUNTS', tv_years_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()

    if terminal_graph_options_int == 3:

        for movie_year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals[movie_year_values] = len(value)

        movie_decades_terminal_graph_list = []

        for key, value in movie_decades_totals.items():
            movie_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: DECADE AMOUNTS', movie_decades_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()

    if terminal_graph_options_int == 4:

        for tv_year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals[tv_year_values] = len(value)

        tv_decades_terminal_graph_list = []

        for key, value in tv_decades_totals.items():
            tv_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: DECADE AMOUNTS', tv_decades_terminal_graph_list):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()


def terminal_graph_options_base_1(username_input, terminal_graph_options_int):
    movie_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    tv_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))

    m_ten_eighty_found_list = []
    m_seven_twenty_found_list = []
    m_standard_def_found_list = []
    m_empty_response_list = []
    movies_total_list = []
    tv_ten_eighty_found_list = []
    tv_seven_twenty_found_list = []
    tv_standard_def_found_list = []
    tv_empty_response_list = []
    tv_total_list = []

    for res in movie_files_results_list:

        if re.findall("19\d{2}x", res[2]):
            m_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[2]):
            m_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[2]):
            m_standard_def_found_list.append(res)
        else:
            m_empty_response_list.append(+1)
        movies_total_list.append(+1)

    movies_graph_terminal_results = [('1080p', float(len(m_ten_eighty_found_list))),
                                     ('720p', float(len(m_seven_twenty_found_list))),
                                     ('SD (Below 720p)', float(len(m_standard_def_found_list)))]

    for res in tv_files_results_list:

        if re.findall("19\d{2}x", res[6]):
            tv_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[6]):
            tv_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[6]):
            tv_standard_def_found_list.append(res)
        else:
            tv_empty_response_list.append(+1)
        tv_total_list.append(+1)

    tv_shows_graph_terminal_results = [('1080p', float(len(tv_ten_eighty_found_list))),
                                       ('720p', float(len(tv_seven_twenty_found_list))),
                                       ('SD (Below 720p)', float(len(tv_standard_def_found_list)))]

    if terminal_graph_options_int == 5:

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: RESOLUTION PERCENTAGES', movies_graph_terminal_results):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()

    if terminal_graph_options_int == 6:

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: RESOLUTION PERCENTAGES', tv_shows_graph_terminal_results):
            print(line)
            print("--------------------------------------------------------------------------------------------------")
        print()
        print()


def totals_query():
    print("___     ___ ____ ___ ____ _    ____    ____ _  _ ____ ____ _   _")
    print("|__] __  |  |  |  |  |__| |    [__  __ |  | |  | |___ |__/  \_/ ")
    print("|__]     |  |__|  |  |  | |___ ___]    |_\| |__| |___ |  \   |   ")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) MOVIES BY YEAR        - 2) TV SHOWS BY YEAR        - 3) MOVIES TOTAL")
    print()
    print("4) TV SHOWS TOTALS       - 5) MOVIES BY DECADE        - 6) TV SHOWS BY DECADE")
    print()
    print("7) MOVIE FILE-TYPES      - 8) TV SHOWS FILE-TYPES     - 9) EPISODES TOTAL IN A TV SHOW")
    print()
    print("10) LIBRARY TOTAL                                                                   - 11) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    b_totals_query_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global b_totals_query_input_int
    b_totals_query_input_int = int(b_totals_query_input)
    if b_totals_query_input_int == 1:
        movie_year_totals(username_input)
    elif b_totals_query_input_int == 2:
        tv_year_totals(username_input)
    elif b_totals_query_input_int == 3:
        movie_titles_amount(username_input)
    elif b_totals_query_input_int == 4:
        tv_titles_amount(username_input)
    elif b_totals_query_input_int == 5:
        movie_decades_totals(username_input)
    elif b_totals_query_input_int == 6:
        tv_decades_totals(username_input)
    elif b_totals_query_input_int == 7:
        search_file_type_totals_movies(username_input, b_totals_query_input_int=7,
                                       picture_graph_options_int='', terminal_graph_options_int='')
    elif b_totals_query_input_int == 8:
        search_file_type_totals_tv(username_input, b_totals_query_input_int=8,
                                   picture_graph_options_int='', terminal_graph_options_int='')
    elif b_totals_query_input_int == 9:
        total_tv_episodes_in_show_title(username_input)
    elif b_totals_query_input_int == 10:
        library_total_amount(username_input)
    elif b_totals_query_input_int == 11:
        launch_media_index()


def movie_titles_amount(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def tv_titles_amount(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv')))
    tv_amounts_list = []
    episode_amounts_list = []
    for counted_tv_title in media_index_list:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)

    for counted_episode_title in tv_index_list:
        episode_amounts_list.append(+1)
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def library_total_amount(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv')))
    tv_amounts_list = []
    episode_amounts_list = []
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)

    for counted_tv_title in media_index_list:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)

    for counted_episode_title in tv_index_list:
        episode_amounts_list.append(+1)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF ITEMS IN MEDIA-LIBRARY:")
    print()
    print(len(movie_amounts_list) + len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def total_tv_episodes_in_show_title(username_input):
    tv_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}

    print()
    tv_total_query_action = input("ENTER TV SHOW TITLE:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    tv_total_query_action_lower = tv_total_query_action.lower()
    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        if tv_total_query_action_lower in found_tv_title.lower():
            tv_show_episodes_found.append(found_tv_title)
            tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)
    for item in tv_show_found.items():
        print()
        print("TITLE NAME: # OF EPISODES")
        print()
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def movie_year_totals(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    movie_totals_query_action = input("ENTER #")
    print()
    movie_totals_query_action = int(movie_totals_query_action)
    for media_movie in media_index_list:
        media_movie_year = int(media_movie[2])
        if movie_string in media_movie:
            if media_movie_year in years_range:
                if media_movie_year not in movie_years_amount_dict:
                    movie_years_amount_dict[media_movie_year] = []
                movie_years_amount_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_amount_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    movie_data = sorted(media_movie_year_totals.items())
    for movie_year_query in movie_data:
        if movie_totals_query_action in movie_year_query:
            print()
            print("# OF MOVIES IN THIS YEAR:")
            print()
            print(movie_year_query[1])
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()


def movie_decades_totals(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_decades_dict = {}
    for media_movie in media_index_list:
        media_movie_year = re.split("(.+) \((\d{4})\)", media_movie[2], flags=0)
        media_movie_year_int = int(media_movie_year[0][:-1] + '0')
        if movie_string in media_movie:
            if media_movie_year_int in years_range:
                if media_movie_year_int not in movie_years_decades_dict:
                    movie_years_decades_dict[media_movie_year_int] = []
                movie_years_decades_dict[media_movie_year_int].append(media_movie)
    media_movie_years_decades_totals = {}
    for movie_year_values, value in sorted(movie_years_decades_dict.items()):
        media_movie_years_decades_totals[movie_year_values] = len(value)
    print()
    print("# OF MOVIES BY DECADE:")
    for item in media_movie_years_decades_totals.items():
        print()
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def tv_year_totals(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    tv_totals_query_action = input("ENTER #")
    print()
    tv_totals_query_action = int(tv_totals_query_action)
    for media_tv in media_index_list:
        media_tv_year = int(media_tv[2])
        if tv_string in media_tv:
            if media_tv_year in years_range:
                if media_tv_year not in tv_years_amount_dict:
                    tv_years_amount_dict[media_tv_year] = []
                tv_years_amount_dict[media_tv_year].append(media_tv)
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_years_amount_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
    tv_data = sorted(media_tv_year_totals.items())
    for tv_year_query in tv_data:
        if tv_totals_query_action in tv_year_query:
            print()
            print("# OF TV SHOWS IN THIS YEAR:")
            print()
            print(tv_year_query[1])
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()


def tv_decades_totals(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_decades_amount_dict = {}
    for media_tv in media_index_list:
        media_tv_year = re.split("(.+) \((\d{4})\)", media_tv[2], flags=0)
        media_tv_year_int = int(media_tv_year[0][:-1] + '0')
        if tv_string in media_tv:
            if media_tv_year_int in years_range:
                if media_tv_year_int not in tv_years_decades_amount_dict:
                    tv_years_decades_amount_dict[media_tv_year_int] = []
                tv_years_decades_amount_dict[media_tv_year_int].append(media_tv)
    media_tv_years_decades_totals = {}
    for tv_year_values, value in sorted(tv_years_decades_amount_dict.items()):
        media_tv_years_decades_totals[tv_year_values] = len(value)
    print()
    print("# OF TV SHOWS BY DECADE:")
    for item in media_tv_years_decades_totals.items():
        print()
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def create_media_indices_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDICES              -  2) UPDATE MEDIA INDEX")
    print()
    print("3) CREATE NEW PARSE-RESULTS INDICES      -  4) UPDATE PARSE-RESULTS INDICES")
    print()
    print("5) CREATE ALL NEW INDICES                -  6) UPDATE ALL INDICES")
    print()
    print("7) COMPARE AGAINST ANOTHER RESULTS FILE  -  8) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_input)
    if cmi_action == 1:
        scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                          movie_alt_dir_input, tv_alt_dir_input)
        search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input,
                                                movie_alt_dir_input, tv_alt_dir_input)
    elif cmi_action == 2:
        compare_old_and_updated_indices_and_create_differences_files(
            username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
    elif cmi_action == 3:
        create_media_files_index_results_csv(username_input)
    elif cmi_action == 4:
        create_updated_media_files_index_results_csv(username_input)
        re_sort_csv_indices(username_input)
    elif cmi_action == 5:
        scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                          movie_alt_dir_input, tv_alt_dir_input)
        search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input,
                                                movie_alt_dir_input, tv_alt_dir_input)
        create_media_files_index_results_csv(username_input)
    elif cmi_action == 6:
        scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                          movie_alt_dir_input, tv_alt_dir_input)
        compare_old_and_updated_indices_and_create_differences_files(
            username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
        create_updated_media_files_index_results_csv(username_input)
        re_sort_csv_indices(username_input)
    elif cmi_action == 7:
        compare_movie_results_file_and_create_differences_files(username_input)
        compare_tv_results_file_and_create_differences_files(username_input)
    elif cmi_action == 8:
        launch_media_index()


def scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                      tv_alt_dir_input):
    movie_dir_list = os.listdir(movie_dir_input)
    tv_dir_list = os.listdir(tv_dir_input)
    movie_title_items = []
    tv_title_items = []

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

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in movie_title_items:
            csv_writer.writerow(file_row)
        for file_row in tv_title_items:
            csv_writer.writerow(file_row)


def search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                            tv_alt_dir_input):
    movie_all_results = []
    movie_file_results = []
    m_nfo_file_results = []
    m_srt_file_results = []
    for root, dirs, files in os.walk(movie_dir_input):
        for movie_file in sorted(files):
            if movie_file.endswith(all_extens):
                movie_all_results.append([root + '/' + movie_file])
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])
            if movie_file.endswith(nfo_extensions):
                m_nfo_file_results.append([root + '/' + movie_file])
            if movie_file.endswith(srt_extensions):
                m_srt_file_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(all_extens):
                    movie_all_results.append([root + '/' + alt_file])
                if alt_file.endswith(extensions):
                    movie_file_results.append([root + '/' + alt_file])
                if alt_file.endswith(nfo_extensions):
                    m_nfo_file_results.append([root + '/' + alt_file])
                if alt_file.endswith(srt_extensions):
                    m_srt_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_all_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(m_nfo_file_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-SRT-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(m_srt_file_results):
            csv_writer.writerow(movie_row)

    tv_show_all_results = []
    tv_show_file_results = []
    t_nfo_file_results = []
    t_srt_file_results = []
    for root, dirs, files in os.walk(tv_dir_input):
        for tv_file in sorted(files):
            if tv_file.endswith(all_extens):
                tv_show_all_results.append([root + '/' + tv_file])
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])
            if tv_file.endswith(nfo_extensions):
                t_nfo_file_results.append([root + '/' + tv_file])
            if tv_file.endswith(srt_extensions):
                t_srt_file_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(all_extens):
                    tv_show_all_results.append([root + '/' + alt_file])
                if alt_file.endswith(extensions):
                    tv_show_file_results.append([root + '/' + alt_file])
                if alt_file.endswith(nfo_extensions):
                    t_nfo_file_results.append([root + '/' + alt_file])
                if alt_file.endswith(srt_extensions):
                    t_srt_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_all_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-NFO-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(t_nfo_file_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-SRT-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(t_srt_file_results):
            csv_writer.writerow(tv_row)


def movie_index_results(username_input):
    movie_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv'))
    movie_index_file_results = []

    for movie_file in movie_index:

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

        title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (title_and_year[-5:-1])

        mv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)


def tv_show_index_results(username_input):
    tv_index = csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv'))
    tv_index_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

        title_and_year = (tv_file[0].rsplit('/')[-2])

        tv_year = (title_and_year[-5:-1])

        tv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                tv_index_file_results.append(
                    [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                     title.get('episode'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


def create_media_files_index_results_csv(username_input):
    movie_index_results(username_input)
    tv_show_index_results(username_input)


def movie_index_update_results(username_input):
    movie_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv'))
    movie_index_file_results = []

    for movie_file in movie_index:

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

        title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (title_and_year[-5:-1])

        mv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "a",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)


def tv_show_index_update_results(username_input):
    tv_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv'))
    tv_index_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

        title_and_year = (tv_file[0].rsplit('/')[-2])

        tv_year = (title_and_year[-5:-1])

        tv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                tv_index_file_results.append(
                    [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                     title.get('episode'), title('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', "a",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


def re_sort_csv_indices(username_input):
    movie_results = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "r"))
    sorted_movie_results = sorted(movie_results, key=lambda row: row[0])
    tv_results = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', "r"))
    sorted_tv_results = sorted(tv_results, key=lambda row: row[0])
    movie_results_file = []
    tv_results_file = []

    for line in sorted_movie_results:
        movie_results_file.append(line)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results_file:
            csv_writer.writerow(movie_row)

    for line in sorted_tv_results:
        tv_results_file.append(line)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_results_file:
            csv_writer.writerow(tv_row)


def create_updated_media_files_index_results_csv(username_input):
    movie_index_update_results(username_input)
    tv_show_index_update_results(username_input)
    re_sort_csv_indices(username_input)
    os.remove(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-TV-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv')


def rename_existing_movie_and_tv_indices_for_update_search(username_input):
    for index_file in os.listdir(r'/home/' + username_input + '/MEDIA-INDEX/'):
        if index_file.startswith('MOVIE-FILES-I'):
            os.rename(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + index_file,
                      r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + 'OLD-' + index_file)
        if index_file.startswith('TV-FILES-I'):
            os.rename(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + index_file,
                      r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + 'OLD-' + index_file)


def update_search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                                   tv_alt_dir_input):
    movie_file_results = []
    for root, dirs, files in os.walk(movie_dir_input):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for movie_file in sorted(files):
                if movie_file.endswith(extensions):
                    movie_file_results.append([root + '/' + movie_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    tv_show_file_results = []
    for root, dirs, files in os.walk(tv_dir_input):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(extensions):
                    tv_show_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)


def compare_old_and_updated_indices_and_create_differences_files(username_input, movie_dir_input, tv_dir_input,
                                                                 movie_alt_dir_input, tv_alt_dir_input):
    rename_existing_movie_and_tv_indices_for_update_search(username_input)
    update_search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                                   tv_alt_dir_input)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv',
              'r') as mi_0, open(
        r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'r') as mi_1:
        old_movie_index = mi_0.readlines()
        new_movie_index = mi_1.readlines()

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv',
              'w') as outFile:
        for line in new_movie_index:
            if line not in old_movie_index:
                outFile.write(line)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-TV-FILES-INDEX.csv',
              'r') as ti_0, open(
        r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', 'r') as ti_1:
        old_tv_index = ti_0.readlines()
        new_tv_index = ti_1.readlines()

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv',
              'w') as outFile:
        for line in new_tv_index:
            if line not in old_tv_index:
                outFile.write(line)


def compare_movie_results_file_and_create_differences_files(username_input):
    print()
    username_input_x = input("ENTER USERNAME FOR THE MOVIE-FILES-RESULTS LISTS TO COMPARE:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv',
              'r') as m_0, open(
              r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'r') as m_1:
        movie_results = m_0.readlines()
        alt_movie_results = m_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-MOVIE-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_m:

            for line in compare_results(movie_results, alt_movie_results):
                outFile_m.write(line)


def compare_tv_results_file_and_create_differences_files(username_input):
    print()
    username_input_x = input("ENTER USERNAME FOR THE TV-FILES-RESULTS LISTS TO COMPARE:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv',
              'r') as t_0, open(
              r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'r') as t_1:
        tv_results = t_0.readlines()
        alt_tv_results = t_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-TV-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_t:

            for line in compare_results(tv_results, alt_tv_results):
                outFile_t.write(line)


def compare_results(results_u, results_a):
    output = []
    for line in results_u:
        if line not in results_a:
            output.append('HAVE: ' + line)

    for line in results_a:
        if line not in results_u:
            output.append('DO NOT HAVE: ' + line)

    return output


first_launch_dirs()

while True:
    launch_media_index()
