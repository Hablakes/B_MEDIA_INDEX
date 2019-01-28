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

all_extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
                  ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
                  ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm",
                  ".rmvb", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm", ".nfo",
                  ".srt")

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


def sep():
    for item in "\n", '-'*98, "\n":
        print(item)


def first_launch_dirs():
    print(pyfiglet.figlet_format("START-MEDIA-INDEX", font="cybermedium"))
    sep()
    global username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input
    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    sep()
    user_info_filename = os.path.expanduser("~/{0}-MEDIA-INDEX/{0}-USER-INFO.csv".format(username_input))

    if os.path.isfile(user_info_filename):
        user_info_file = list(csv.reader(open(user_info_filename)))
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
        sep()

        user_info = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                     'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}

        os.makedirs(os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)), exist_ok=True)
        os.makedirs(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES'.format(username_input)), exist_ok=True)

        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/{0}-USER-INFO.csv'.format(username_input)), 'w',
                  encoding='UTF8') as f:
            csv_writer = csv.writer(f)
            for row in user_info.items():
                csv_writer.writerow(row)

        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-FILES-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-FILES-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-NFO-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-NFO-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-SRT-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-SRT-INDEX.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass
        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), 'w',
                  encoding='UTF8'):
            pass


def launch_media_index():
    print(pyfiglet.figlet_format("MEDIA-INDEX", font="cybermedium"))
    sep()
    print("1) QUERIES - 2) SORTING - 3) FILE DATA/INFO - 4) GRAPHS - 5) TOTALS - 6) INDEXING    - 0) EXIT")
    sep()
    lmi_input = input("ENTER #")
    sep()
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
    print(pyfiglet.figlet_format("MEDIA-QUERY", font="cybermedium"))
    sep()
    print("SEARCH TITLES OF   -   1) MOVIES - 2) TV SHOWS SERIES")
    print()
    print("SEARCH PLOTS OF    -   3) MOVIES - 4) TV SHOWS SERIES / EPISODES")
    print()
    print("SEARCH PLOTS OF    -   5) ALL MEDIA                                                  - 6) EXIT")
    sep()
    title_search_type = input("ENTER #")
    sep()
    title_search_type_lower = int(title_search_type)
    if title_search_type_lower == 1:
        movie_title_search(username_input)
    elif title_search_type_lower == 2:
        tv_title_search(username_input)
    elif title_search_type_lower == 3:
        search_movie_plots(username_input)
    elif title_search_type_lower == 4:
        search_tv_plots(username_input)
    elif title_search_type_lower == 5:
        search_all_plots(username_input)
    elif title_search_type_lower == 6:
        launch_media_index()


def movie_title_search(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
    movie_title_search_action = input("QUERY MOVIES:")
    sep()
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
    sep()


def tv_title_search(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
    tv_title_search_action = input("QUERY TV SHOWS:")
    sep()
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
    sep()


def run_sort():
    print(pyfiglet.figlet_format("SORT-OPTIONS", font="cybermedium"))
    sep()
    print("MOVIES & TV SHOWS TITLES  -   TITLE - 1) ASCENDING - 2) DESCENDING")
    print()
    print("MOVIES & TV SHOWS TITLES  -    YEAR - 3) ASCENDING - 4) DESCENDING")
    print()
    print("TV SHOW - EPISODES -          TITLE - 5) ASCENDING - 6) DESCENDING")
    print()
    print("TV SHOW - EPISODES -       EPISODES - 7) ASCENDING - 8) DESCENDING                   - 9) EXIT")
    sep()
    sort_input = input("ENTER #")
    sep()
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
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                   encoding='UTF8')))
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
            sep()
    if sort_options_int == 6:
        for item in sorted_by_key_a:
            print(item)
            sep()
    if sort_options_int == 7:
        for item in sorted_by_value_d:
            print(item)
            sep()
    if sort_options_int == 8:
        for item in sorted_by_value_a:
            print(item)
            sep()


def run_file_query_and_sort():
    print(pyfiglet.figlet_format("FILE-INFO-QUERY", font="cybermedium"))
    sep()
    print("SEARCH TITLES - 1) MOVIES - 2) TV SHOWS                                              - 3) EXIT")
    sep()
    data_query_input = input("ENTER #")
    sep()
    data_query_int = int(data_query_input)
    if data_query_int == 1:
        movie_query_all_results(username_input)
    elif data_query_int == 2:
        tv_query_all_results(username_input)
    elif data_query_int == 3:
        launch_media_index()


def movie_query_all_results(username_input):
    mv_files_results_list = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), encoding='UTF8'))

    mv_query_action = input("ENTER SEARCH QUERY (MOVIES):")
    sep()
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
            print()

            if int(len(movie_file[6])) != 0:

                print("RATING")
                print()
                if '</rating>' not in movie_file[6]:
                    mv_rating = re.findall("<rating>(.*?)", movie_file[6])
                    print(mv_rating[0])
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()
                elif '</rating>' in movie_file[6]:
                    mv_rating = re.findall("<rating>(.*?)</rating>", movie_file[6])
                    print(mv_rating[0])
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()

            if int(len(movie_file[7])) != 0:

                print("RUNTIME")
                print()
                if '</runtime>' not in movie_file[7]:
                    mv_runtime = re.findall("<runtime>(.*?)", movie_file[7])
                    print(mv_runtime[0], ": Minutes")
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()
                elif '</runtime>' in movie_file[7]:
                    mv_runtime = re.findall("<runtime>(.*?)</runtime>", movie_file[7])
                    print(mv_runtime[0], ": Minutes")
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

                elif '</plot>' in movie_file[5]:
                    mv_plot = re.findall("<plot>(.*?)</plot>", movie_file[5])
                    print(textwrap.fill(mv_plot[0], 80))
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()


def tv_query_all_results(username_input):
    tv_files_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))

    tv_show_query_action = input("ENTER SEARCH QUERY (TV SHOWS):")
    sep()
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
                if '</rating>' not in tv_file[9]:
                    tv_rating = re.findall("<rating>(.*?)", tv_file[9])
                    print(tv_rating[0])
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()
                elif '</rating>' in tv_file[9]:
                    tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                    print(tv_rating[0])
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

                elif '</plot>' in tv_file[8]:
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
                if '</rating>' not in tv_file[9]:
                    tv_rating = re.findall("<rating>(.*?)", tv_file[9])
                    print(tv_rating[0])
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()
                elif '</rating>' in tv_file[9]:
                    tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                    print(tv_rating[0])
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

                elif '</plot>' in tv_file[8]:
                    tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                    print(tv_plot[0])
                    print("-------------------------------------------------"
                          "-------------------------------------------------")
                    print()


def run_graphs():
    print(pyfiglet.figlet_format("GRAPH-OPTIONS", font="cybermedium"))
    sep()
    print("1) PICTURE GRAPHS (MAT-PLOT-LIB)    - 2) TERMINAL GRAPHS (ASCII-CHART)               - 3) EXIT")
    sep()
    graph_options = input("ENTER #")
    sep()
    graph_options_int = int(graph_options)
    if graph_options_int == 1:
        run_picture_graphs()
    elif graph_options_int == 2:
        run_terminal_graphs()
    elif graph_options_int == 3:
        launch_media_index()


def run_picture_graphs():
    print(pyfiglet.figlet_format("PICTURE-GRAPHS", font="cybermedium"))
    sep()
    print("1) MOVIES (TITLES PER YEAR)         - 2) TV SHOWS (TITLES PER YEAR)")
    print()
    print("3) MOVIES (TITLES PER DECADE)       - 4) TV SHOWS (TITLES PER DECADE)")
    print()
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)")
    print()
    print("7) MOVIES (FILE-TYPE AMOUNTS)       - 8) TV SHOWS (FILE-TYPE AMOUNTS)                - 9) EXIT")
    sep()
    picture_graph_options = input("ENTER #")
    sep()
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
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
        plt.savefig(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/MOVIE-YEAR-RESULTS.png'.format(username_input)))
        plt.show()

    if picture_graph_options_int == 2:

        for year_values, value in sorted(tv_years_dict.items()):
            tv_year_totals[year_values] = len(value)
        x, y = zip(*sorted(tv_year_totals.items()))
        plt.bar(x, y)
        plt.savefig(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/TV-YEAR-RESULTS.png'.format(username_input)))
        plt.show()

    if picture_graph_options_int == 3:

        for year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals[year_values] = len(value)
        x, y = zip(*movie_decades_totals.items())
        plt.bar(x, y, width=5)
        plt.savefig(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/MOVIE-DECADE-RESULTS.png'.format(username_input)))
        plt.show()

    if picture_graph_options_int == 4:

        for year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals[year_values] = len(value)
        x, y = zip(*tv_decades_totals.items())
        plt.bar(x, y, width=5)
        plt.savefig(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/TV-DECADE-RESULTS.png'.format(username_input)))
        plt.show()


def pie_chart_options_base(username_input, picture_graph_options_int):
    movie_files_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)),
                   encoding='UTF8')))
    tv_files_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                   encoding='UTF8')))

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

        if re.findall("19\d{2}x", res[3]):
            m_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[3]):
            m_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[3]):
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
            os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/MOVIE-RESOLUTION-RESULTS.png'.format(username_input)))
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
            os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/TV-RESOLUTION-RESULTS.png'.format(username_input)))
        plt.show()


def search_file_type_totals_movies(username_input, b_totals_query_input_int, picture_graph_options_int,
                                   terminal_graph_options_int):
    movie_file_index = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))
    extensions_dict = {}
    extensions_totals = {}

    for file_type in movie_file_index:
        if str(',') not in file_type[4]:
            if file_type[4] not in extensions_dict:
                extensions_dict[file_type[4]] = []
            extensions_dict[file_type[4]].append(file_type[4])
    movie_file_type_totals = {}

    if b_totals_query_input_int == 7:

        for movie_file_type_values, value in sorted(extensions_dict.items()):
            movie_file_type_totals[movie_file_type_values] = len(value)
        print()
        print("TOTAL AMOUNTS OF FILE-TYPES IN MOVIES:")
        print()
        for items in movie_file_type_totals.items():
            print(items)
        sep()

    if picture_graph_options_int == 7:

        for movie_file_type_values, value in sorted(extensions_dict.items()):
            movie_file_type_totals[movie_file_type_values] = len(value)

        x, y = zip(*sorted(movie_file_type_totals.items()))
        plt.bar(x, y)
        plt.savefig(
            os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/MOVIE-FILE-TYPE-RESULTS.png'.format(username_input)))
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
        sep()


def search_file_type_totals_tv(username_input, b_totals_query_input_int, picture_graph_options_int,
                               terminal_graph_options_int):
    tv_file_index = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))
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
        for items in tv_file_type_totals.items():
            print(items)
        sep()

    if picture_graph_options_int == 8:

        for tv_file_type_values, value in sorted(extensions_dict.items()):
            tv_file_type_totals[tv_file_type_values] = len(value)

        x, y = zip(*sorted(tv_file_type_totals.items()))
        plt.bar(x, y)
        plt.savefig(os.path.expanduser(r'~/{0}-MEDIA-INDEX/FILES/TV-FILE-TYPE-RESULTS.png'.format(username_input)))
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
        sep()


def run_terminal_graphs():
    print(pyfiglet.figlet_format("TERMINAL-GRAPHS", font="cybermedium"))
    sep()
    print("1) MOVIES (TITLES PER YEAR)         - 2) TV SHOWS (TITLES PER YEAR)")
    print()
    print("3) MOVIES (TITLES PER DECADE)       - 4) TV SHOWS (TITLES PER DECADE)")
    print()
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)")
    print()
    print("7) MOVIES (FILE-TYPE AMOUNTS)       - 8) TV SHOWS (FILE-TYPE AMOUNTS)                - 9) EXIT")
    sep()
    terminal_graph_options = input("ENTER #")
    sep()
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
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))

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
        sep()

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
        sep()

    if terminal_graph_options_int == 3:

        for movie_year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals[movie_year_values] = len(value)

        movie_decades_terminal_graph_list = []

        for key, value in movie_decades_totals.items():
            movie_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: DECADE AMOUNTS', movie_decades_terminal_graph_list):
            print(line)
        sep()

    if terminal_graph_options_int == 4:

        for tv_year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals[tv_year_values] = len(value)

        tv_decades_terminal_graph_list = []

        for key, value in tv_decades_totals.items():
            tv_decades_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: DECADE AMOUNTS', tv_decades_terminal_graph_list):
            print(line)
        sep()


def terminal_graph_options_base_1(username_input, terminal_graph_options_int):
    movie_files_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))
    tv_files_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))

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

        if re.findall("19\d{2}x", res[3]):
            m_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[3]):
            m_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[3]):
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
        sep()

    if terminal_graph_options_int == 6:

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: RESOLUTION PERCENTAGES', tv_shows_graph_terminal_results):
            print(line)
        sep()


def totals_query():
    print(pyfiglet.figlet_format("TOTALS-QUERY", font="cybermedium"))
    sep()
    print("1) MOVIES BY YEAR        - 2) TV SHOWS BY YEAR        - 3) MOVIES TOTAL")
    print()
    print("4) TV SHOWS TOTALS       - 5) MOVIES BY DECADE        - 6) TV SHOWS BY DECADE")
    print()
    print("7) MOVIE FILE-TYPES      - 8) TV SHOWS FILE-TYPES     - 9) EPISODES TOTAL IN A TV SHOW")
    print()
    print("10) LIBRARY TOTAL                                                                   - 11) EXIT")
    sep()
    b_totals_query_input = input("ENTER #")
    sep()
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
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    sep()


def tv_titles_amount(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
    tv_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-FILES-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
    sep()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    sep()


def library_total_amount(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
    tv_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-FILES-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
    sep()
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    sep()
    print()
    print("TOTAL AMOUNT OF ITEMS IN MEDIA-LIBRARY:")
    print()
    print(len(movie_amounts_list) + len(episode_amounts_list))
    sep()


def total_tv_episodes_in_show_title(username_input):
    tv_results_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
                        encoding='UTF8')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}

    print()
    tv_total_query_action = input("ENTER TV SHOW TITLE:")
    sep()
    tv_total_query_action_lower = tv_total_query_action.lower()
    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        if tv_total_query_action_lower in found_tv_title.lower():
            tv_show_episodes_found.append(found_tv_title)
            tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)
    for item in tv_show_found.items():
        print("TITLE NAME: # OF EPISODES")
        print()
        print(item)
        sep()


def movie_year_totals(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
            sep()


def movie_decades_totals(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
    sep()


def tv_year_totals(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
            sep()


def tv_decades_totals(username_input):
    media_index_list = list(
        csv.reader(open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)),
                        encoding='UTF8')))
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
    sep()


def create_media_indices_all():
    print(pyfiglet.figlet_format("INDEX-OPTIONS", font="cybermedium"))
    sep()
    print("1) CREATE NEW MEDIA INDICES              -  2) UPDATE MEDIA INDEX")
    print()
    print("3) CREATE NEW PARSE-RESULTS INDICES      -  4) UPDATE PARSE-RESULTS INDICES")
    print()
    print("5) CREATE ALL NEW INDICES                -  6) UPDATE ALL INDICES")
    print()
    print("7) COMPARE AGAINST ANOTHER RESULTS FILE  -  8) EXIT")
    sep()
    cmi_input = input("ENTER #")
    sep()
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
        compare_old_and_updated_indices_and_create_differences_files(
            username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
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

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MEDIA-INDEX.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
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
            if movie_file.lower().endswith(all_extensions):
                movie_all_results.append([root + '/' + movie_file])
            if movie_file.lower().endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])
            if movie_file.lower().endswith(nfo_extensions.lower()):
                m_nfo_file_results.append([root + '/' + movie_file])
            if movie_file.lower().endswith(srt_extensions.lower()):
                m_srt_file_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(all_extensions):
                    movie_all_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(extensions):
                    movie_file_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(nfo_extensions):
                    m_nfo_file_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(srt_extensions):
                    m_srt_file_results.append([root + '/' + alt_file])

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-INDEX.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_all_results):
            csv_writer.writerow(movie_row)

    tv_show_all_results = []
    tv_show_file_results = []
    t_nfo_file_results = []
    t_srt_file_results = []
    for root, dirs, files in os.walk(tv_dir_input):
        for tv_file in sorted(files):
            if tv_file.lower().endswith(all_extensions):
                tv_show_all_results.append([root + '/' + tv_file])
            if tv_file.lower().endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])
            if tv_file.lower().endswith(nfo_extensions):
                t_nfo_file_results.append([root + '/' + tv_file])
            if tv_file.lower().endswith(srt_extensions):
                t_srt_file_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(all_extensions):
                    tv_show_all_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(extensions):
                    tv_show_file_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(nfo_extensions):
                    t_nfo_file_results.append([root + '/' + alt_file])
                if alt_file.lower().endswith(srt_extensions):
                    t_srt_file_results.append([root + '/' + alt_file])

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-INDEX.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_all_results):
            csv_writer.writerow(tv_row)


def movie_index_all_results(username_input):
    movie_index = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-INDEX.csv'.format(username_input)), encoding='UTF8'))

    movie_index_file_results = {}

    for movie_file in sorted(movie_index):

        title_key = movie_file[0].rsplit('/')[-2]

        filename_key = movie_file[0].rsplit('/', 1)[-1]

        if title_key not in movie_index_file_results:
            movie_index_file_results[title_key] = {}

        if movie_file[0].lower().endswith(extensions):

            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

            try:
                test = pymediainfo.MediaInfo.parse(movie_file[0])
            except OSError as e:  # If an OSError happens, it enters the below Block.
                print("OSError on {}".format(movie_file[0]))  # Print what File it crashed on
                print(e)  # Print the Error
                continue  # Continue to next Item

            for track in test.tracks:

                if track.track_type == 'Video':
                    movie_index_file_results[title_key]["DIRECTORY"] = title_key
                    movie_index_file_results[title_key]["TITLE"] = title.get('title')
                    movie_index_file_results[title_key]["YEAR"] = title.get('year')
                    movie_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    movie_index_file_results[title_key]["FILE-TYPE"] = title.get('container')
                    movie_index_file_results[title_key]["FILENAME"] = filename_key

        elif movie_file[0].lower().endswith(nfo_extensions):
            try:
                with open(movie_file[0]) as f:
                    for line in f.readlines():
                        if '<plot>' in line:
                            movie_index_file_results[title_key]["PLOT"] = line

                        if '<rating>' in line:
                            movie_index_file_results[title_key]["RATING"] = line

                        if '<runtime>' in line:
                            movie_index_file_results[title_key]["RUN-TIME"] = line
            except Exception as e:
                print(e)  # Print the Error
                print(movie_file[0])  # Print the File it was opening when the Error happened
                continue  # Continue on to the next Item

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.DictWriter(f, ["DIRECTORY", "TITLE", "YEAR", "RESOLUTION", "FILE-TYPE", "PLOT", "RATING",
                                        "RUN-TIME", "FILENAME"])
        for movie_row in movie_index_file_results.values():
            csv_writer.writerow(movie_row)


def tv_index_all_results(username_input):
    tv_index = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-INDEX.csv'.format(username_input)), encoding='UTF8'))

    tv_index_file_results = {}

    for tv_file in sorted(tv_index):

        title_key = tv_file[0].rsplit('/', 1)[-1][:-4]

        folder_title = tv_file[0].rsplit('/')[-2]

        filename_key = tv_file[0].rsplit('/', 1)[-1]

        if tv_file[0].lower().endswith(extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

            try:
                test = pymediainfo.MediaInfo.parse(tv_file[0])
            except OSError as e:  # If an OSError happens, it enters the below Block.
                print("OSError on {}".format(tv_file[0]))  # Print what File it crashed on
                print(e)  # Print the Error
                continue  # Continue to next Item

            for track in test.tracks:

                if track.track_type == 'Video':
                    tv_index_file_results[title_key]["DIRECTORY"] = folder_title
                    tv_index_file_results[title_key]["TITLE"] = title.get('title')
                    tv_index_file_results[title_key]["YEAR"] = title.get('year')
                    tv_index_file_results[title_key]["EPISODE TITLE"] = title.get('episode_title')
                    tv_index_file_results[title_key]["SEASON"] = title.get('season')
                    tv_index_file_results[title_key]["EPISODE NUMBER"] = title.get('episode')
                    tv_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    tv_index_file_results[title_key]["FILE-TYPE"] = title.get('container')
                    tv_index_file_results[title_key]["FILENAME"] = filename_key

        elif tv_file[0].lower().endswith(nfo_extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

                try:
                    with open(tv_file[0]) as f:
                        for line in f.readlines():
                            if '<plot>' in line:
                                tv_index_file_results[title_key]["PLOT"] = line

                            if '<rating>' in line:
                                tv_index_file_results[title_key]["RATING"] = line

                            if '<runtime>' in line:
                                tv_index_file_results[title_key]["RUN-TIME"] = line
                except Exception as e:
                    print(e)  # Print the Error
                    print(tv_file[0])  # Print the File it was opening when the Error happened
                    continue  # Continue on to the next Item

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.DictWriter(f, ["DIRECTORY", "TITLE", "YEAR", "EPISODE TITLE", "SEASON", "EPISODE NUMBER",
                                        "RESOLUTION", "FILE-TYPE", "PLOT", "RATING", "RUN-TIME", "FILENAME"])
        for tv_row in tv_index_file_results.values():
            csv_writer.writerow(tv_row)


def create_media_files_index_results_csv(username_input):
    movie_index_all_results(username_input)
    tv_index_all_results(username_input)


def movie_index_update_results(username_input):
    movie_index = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-INDEX.csv'.format(username_input)), encoding='UTF8'))

    movie_index_update = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-MOVIE-INDEX.csv'.format(username_input)),
             encoding='UTF8'))

    movie_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), encoding='UTF8'))

    movie_index_results_list = []

    movie_index_file_results = {}

    for found_index_file in movie_index:
        movie_index_results_list.append(found_index_file[0].rsplit('/', 1)[-1])

    for found_movie_file in movie_results:
        found_movie_filename = found_movie_file[8]
        if found_movie_filename in movie_index_results_list:
            if found_movie_filename not in movie_index_file_results:
                movie_index_file_results[found_movie_filename] = {}

            movie_index_file_results[found_movie_filename]["DIRECTORY"] = found_movie_file[0]
            movie_index_file_results[found_movie_filename]["TITLE"] = found_movie_file[1]
            movie_index_file_results[found_movie_filename]["YEAR"] = found_movie_file[2]
            movie_index_file_results[found_movie_filename]["RESOLUTION"] = found_movie_file[3]
            movie_index_file_results[found_movie_filename]["FILE-TYPE"] = found_movie_file[4]
            movie_index_file_results[found_movie_filename]["PLOT"] = found_movie_file[5]
            movie_index_file_results[found_movie_filename]["RATING"] = found_movie_file[6]
            movie_index_file_results[found_movie_filename]["RUN-TIME"] = found_movie_file[7]
            movie_index_file_results[found_movie_filename]["FILENAME"] = found_movie_file[8]

    for movie_file in sorted(movie_index_update):

        title_key = movie_file[0].rsplit('/')[-2]

        filename_key = movie_file[0].rsplit('/', 1)[-1]

        if title_key not in movie_index_file_results:
            movie_index_file_results[title_key] = {}

        if movie_file[0].lower().endswith(extensions):

            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

            try:
                test = pymediainfo.MediaInfo.parse(movie_file[0])
            except OSError as e:  # If an OSError happens, it enters the below Block.
                print("OSError on {}".format(movie_file[0]))  # Print what File it crashed on
                print(e)  # Print the Error
                continue  # Continue to next Item

            for track in test.tracks:

                if track.track_type == 'Video':
                    movie_index_file_results[title_key]["DIRECTORY"] = title_key
                    movie_index_file_results[title_key]["TITLE"] = title.get('title')
                    movie_index_file_results[title_key]["YEAR"] = title.get('year')
                    movie_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    movie_index_file_results[title_key]["FILE-TYPE"] = title.get('container')
                    movie_index_file_results[title_key]["FILENAME"] = filename_key

        elif movie_file[0].lower().endswith(nfo_extensions):
            with open(movie_file[0]) as f:
                try:
                    with open(movie_file[0]) as f:
                        for line in f.readlines():
                            if '<plot>' in line:
                                movie_index_file_results[title_key]["PLOT"] = line

                            if '<rating>' in line:
                                movie_index_file_results[title_key]["RATING"] = line

                            if '<runtime>' in line:
                                movie_index_file_results[title_key]["RUN-TIME"] = line
                except Exception as e:
                    print(e)  # Print the Error
                    print(movie_file[0])  # Print the File it was opening when the Error happened
                    continue  # Continue on to the next Item

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.DictWriter(f, ["DIRECTORY", "TITLE", "YEAR", "RESOLUTION", "FILE-TYPE", "PLOT", "RATING",
                                        "RUN-TIME", "FILENAME"])
        for movie_row in movie_index_file_results.values():
            csv_writer.writerow(movie_row)


def tv_show_index_update_results(username_input):
    tv_index = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-INDEX.csv'.format(username_input)), encoding='UTF8'))

    tv_index_update = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-TV-INDEX.csv'.format(username_input)), encoding='UTF8'))

    tv_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), encoding='UTF8'))

    tv_index_results_list = []

    tv_index_file_results = {}

    for found_index_file in tv_index:
        tv_index_results_list.append(found_index_file[0].rsplit('/', 1)[-1])

    for found_tv_file in tv_results:
        found_tv_filename = found_tv_file[11]
        if found_tv_filename in tv_index_results_list:
            if found_tv_filename not in tv_index_file_results:
                tv_index_file_results[found_tv_filename] = {}

            tv_index_file_results[found_tv_filename]["DIRECTORY"] = found_tv_file[0]
            tv_index_file_results[found_tv_filename]["TITLE"] = found_tv_file[1]
            tv_index_file_results[found_tv_filename]["YEAR"] = found_tv_file[2]
            tv_index_file_results[found_tv_filename]["EPISODE TITLE"] = found_tv_file[3]
            tv_index_file_results[found_tv_filename]["SEASON"] = found_tv_file[4]
            tv_index_file_results[found_tv_filename]["EPISODE NUMBER"] = found_tv_file[5]
            tv_index_file_results[found_tv_filename]["RESOLUTION"] = found_tv_file[6]
            tv_index_file_results[found_tv_filename]["FILE-TYPE"] = found_tv_file[7]
            tv_index_file_results[found_tv_filename]["PLOT"] = found_tv_file[8]
            tv_index_file_results[found_tv_filename]["RATING"] = found_tv_file[9]
            tv_index_file_results[found_tv_filename]["RUN-TIME"] = found_tv_file[10]
            tv_index_file_results[found_tv_filename]["FILENAME"] = found_tv_file[11]

    for tv_file in sorted(tv_index_update):

        title_key = tv_file[0].rsplit('/', 1)[-1][:-4]

        folder_title = tv_file[0].rsplit('/')[-2]

        filename_key = tv_file[0].rsplit('/', 1)[-1]

        if tv_file[0].lower().endswith(extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

            try:
                test = pymediainfo.MediaInfo.parse(tv_file[0])
            except OSError as e:  # If an OSError happens, it enters the below Block.
                print("OSError on {}".format(tv_file[0]))  # Print what File it crashed on
                print(e)  # Print the Error
                continue  # Continue to next Item

            for track in test.tracks:

                if track.track_type == 'Video':
                    tv_index_file_results[title_key]["DIRECTORY"] = folder_title
                    tv_index_file_results[title_key]["TITLE"] = title.get('title')
                    tv_index_file_results[title_key]["YEAR"] = title.get('year')
                    tv_index_file_results[title_key]["EPISODE TITLE"] = title.get('episode_title')
                    tv_index_file_results[title_key]["SEASON"] = title.get('season')
                    tv_index_file_results[title_key]["EPISODE NUMBER"] = title.get('episode')
                    tv_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    tv_index_file_results[title_key]["FILE-TYPE"] = title.get('container')
                    tv_index_file_results[title_key]["FILENAME"] = filename_key

        elif tv_file[0].lower().endswith(nfo_extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

                with open(tv_file[0]) as f:
                    try:
                        with open(tv_file[0]) as f:
                            for line in f.readlines():
                                if '<plot>' in line:
                                    tv_index_file_results[title_key]["PLOT"] = line

                                if '<rating>' in line:
                                    tv_index_file_results[title_key]["RATING"] = line

                                if '<runtime>' in line:
                                    tv_index_file_results[title_key]["RUN-TIME"] = line
                    except Exception as e:
                        print(e)  # Print the Error
                        print(tv_file[0])  # Print the File it was opening when the Error happened
                        continue  # Continue on to the next Item

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.DictWriter(f, ["DIRECTORY", "TITLE", "YEAR", "EPISODE TITLE", "SEASON", "EPISODE NUMBER",
                                        "RESOLUTION", "FILE-TYPE", "PLOT", "RATING", "RUN-TIME", "FILENAME"])
        for tv_row in tv_index_file_results.values():
            csv_writer.writerow(tv_row)


def re_sort_csv_indices(username_input):
    movie_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), "r", encoding='UTF8'))
    sorted_movie_results = sorted(movie_results, key=lambda row: row[0])
    tv_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), "r", encoding='UTF8'))
    sorted_tv_results = sorted(tv_results, key=lambda row: row[0])
    movie_results_file = []
    tv_results_file = []

    for line in sorted_movie_results:
        movie_results_file.append(line)

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results_file:
            csv_writer.writerow(movie_row)

    for line in sorted_tv_results:
        tv_results_file.append(line)

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), "w",
              newline="", encoding='UTF8') as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_results_file:
            csv_writer.writerow(tv_row)


def create_updated_media_files_index_results_csv(username_input):
    movie_updates = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-MOVIE-INDEX.csv'.format(username_input)),
        encoding='UTF8'))
    tv_updates = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-TV-INDEX.csv'.format(username_input)),
        encoding='UTF8'))

    for movies in movie_updates:
        if int(len(movies)) != 0:
            movie_index_update_results(username_input)
        else:
            continue

    for tv_shows in tv_updates:
        if int(len(tv_shows)) != 0:
            tv_show_index_update_results(username_input)
        else:
            continue

    os.remove(os.path.expanduser(r'~/{0}-MEDIA-INDEX/OLD-MOVIE-INDEX.csv'.format(username_input)))
    os.remove(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-MOVIE-INDEX.csv'.format(username_input)))
    os.remove(os.path.expanduser(r'~/{0}-MEDIA-INDEX/OLD-TV-INDEX.csv'.format(username_input)))
    os.remove(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-TV-INDEX.csv'.format(username_input)))


def rename_existing_movie_and_tv_indices_for_update_search(username_input):
    for index_file in os.listdir(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/'):
        if index_file.startswith('MOVIE-IND'):
            os.rename(os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + index_file,
                      os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + 'OLD-' + index_file)
        if index_file.startswith('TV-IND'):
            os.rename(os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + index_file,
                      os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + 'OLD-' + index_file)


def compare_old_and_updated_indices_and_create_differences_files(username_input, movie_dir_input, tv_dir_input,
                                                                 movie_alt_dir_input, tv_alt_dir_input):
    rename_existing_movie_and_tv_indices_for_update_search(username_input)
    search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                            tv_alt_dir_input)

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/OLD-MOVIE-INDEX.csv'.format(username_input)),
              'r', encoding='UTF8') as mi_0, open(
        os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-INDEX.csv'.format(username_input)), 'r', encoding='UTF8') as mi_1:
        old_movie_index = mi_0.readlines()
        new_movie_index = mi_1.readlines()

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-MOVIE-INDEX.csv'.format(username_input)),
              'w', encoding='UTF8') as outFile:
        for line in new_movie_index:
            if line not in old_movie_index:
                outFile.write(line)

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/OLD-TV-INDEX.csv'.format(username_input)),
              'r', encoding='UTF8') as ti_0, open(
        os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-INDEX.csv'.format(username_input)), 'r', encoding='UTF8') as ti_1:
        old_tv_index = ti_0.readlines()
        new_tv_index = ti_1.readlines()

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/UPDATES-TO-TV-INDEX.csv'.format(username_input)),
              'w', encoding='UTF8') as outFile:
        for line in new_tv_index:
            if line not in old_tv_index:
                outFile.write(line)


def compare_movie_results_file_and_create_differences_files(username_input):
    print()
    username_input_x = input("ENTER USERNAME FOR THE MOVIE-RESULTS LISTS TO COMPARE:")
    sep()

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)),
              'r', encoding='UTF8') as m_0, open(
        os.path.expanduser(
            r'~/{0}/'.format(username_input)) + username_input_x + '-MEDIA-INDEX/MOVIE-RESULTS.csv',
        'r', encoding='UTF8') as m_1:
        movie_results = m_0.readlines()
        alt_movie_results = m_1.readlines()

        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + username_input_x +
                  '-MOVIE-COMPARISON-RESULTS.csv', 'w', encoding='UTF8') as outFile_m:
            for line in compare_results(movie_results, alt_movie_results):
                outFile_m.write(line)


def compare_tv_results_file_and_create_differences_files(username_input):
    print()
    username_input_x = input("ENTER USERNAME FOR THE TV-RESULTS LISTS TO COMPARE:")
    sep()

    with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)),
              'r', encoding='UTF8') as t_0, open(
        os.path.expanduser(
            r'~/{0}/'.format(username_input)) + username_input_x + '-MEDIA-INDEX/TV-RESULTS.csv',
        'r', encoding='UTF8') as t_1:
        tv_results = t_0.readlines()
        alt_tv_results = t_1.readlines()

        with open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/'.format(username_input)) + username_input_x +
                  '-TV-COMPARISON-RESULTS.csv', 'w', encoding='UTF8') as outFile_t:
            for line in compare_results(tv_results, alt_tv_results):
                outFile_t.write(line)


def compare_results(results_user, results_other):
    output = []
    for line in results_user:
        if line not in results_other:
            output.append('HAVE: ' + line)

    for line in results_other:
        if line not in results_user:
            output.append('DO NOT HAVE: ' + line)

    return output


def search_movie_plots(username_input):
    movie_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), encoding='UTF8'))
    plots_list = []
    for plot in movie_results:
        plots_list.append("MOVIE" + ' - ' + plot[0] + ' - ' + plot[5])
    sep()
    plot_search = input("SEARCH MOVIE PLOTS FOR KEYWORD(S):")
    plot_search_lower = plot_search.lower()
    sep()
    for items in plots_list:
        if plot_search_lower in items.lower():
            print()
            print(textwrap.fill(items, 80))
    sep()


def search_tv_plots(username_input):
    tv_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), encoding='UTF8'))
    plots_list = []
    for plot in tv_results:
        plots_list.append("TV SHOW" + ' - ' + plot[0] + ' - ' + plot[8])
    sep()
    plot_search = input("SEARCH TV SHOW(S) PLOTS FOR KEYWORD(S):")
    plot_search_lower = plot_search.lower()
    sep()
    for items in plots_list:
        if plot_search_lower in items.lower():
            print()
            print(textwrap.fill(items, 80))
    sep()


def search_all_plots(username_input):
    movie_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/MOVIE-RESULTS.csv'.format(username_input)), encoding='UTF8'))
    tv_results = csv.reader(
        open(os.path.expanduser(r'~/{0}-MEDIA-INDEX/TV-RESULTS.csv'.format(username_input)), encoding='UTF8'))
    plots_list = []
    for plot in movie_results:
        plots_list.append("MOVIE" + ' - ' + plot[0] + ' - ' + plot[5])
    for plot in tv_results:
        plots_list.append("TV SHOW" + ' - ' + plot[0] + ' - ' + plot[8])
    sep()
    plot_search = input("SEARCH ALL MEDIA PLOTS FOR KEYWORD(S):")
    plot_search_lower = plot_search.lower()
    sep()
    for items in plots_list:
        if plot_search_lower in items.lower():
            print()
            print(textwrap.fill(items, 80))
    sep()


first_launch_dirs()

while True:
    launch_media_index()
