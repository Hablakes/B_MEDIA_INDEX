import csv
import re

from ascii_graph import Pyasciigraph

username_input = []
movie_dir_input = []
tv_dir_input = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")


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
        get_movie_years_for_dict_and_graph_terminal()
    elif graph_options == 2:
        get_tv_years_for_dict_and_graph_terminal()
    elif graph_options == 3:
        get_movie_years_decades_totals_graphs_terminal()
    elif graph_options == 4:
        get_tv_years_decades_totals_graphs_terminal()
    elif graph_options == 5:
        search_resolution_totals_movies_terminal()
    elif graph_options == 6:
        search_resolution_totals_tv_shows_terminal()
    elif graph_options == 7:
        pass


def get_movie_years_for_dict_and_graph_terminal():
    media_index_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_dict = {}
    for media_movie in media_index_list:
        media_movie_year = re.split("(.+) \((\d{4})\)", media_movie[2], flags=0)
        media_movie_year_int = int(media_movie_year[0])
        if movie_string in media_movie:
            if media_movie_year_int in movie_years_range:
                if media_movie_year_int not in movie_years_dict:
                    movie_years_dict[media_movie_year_int] = []
                movie_years_dict[media_movie_year_int].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    movie_data = sorted(media_movie_year_totals.items())

    movie_years_terminal_graph_list = []

    for key, value in movie_data:
        movie_years_terminal_graph_list.append((str(key), value))

    graph = Pyasciigraph()
    for line in graph.graph('MOVIES: YEAR AMOUNTS', movie_years_terminal_graph_list):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


def get_tv_years_for_dict_and_graph_terminal():
    media_index_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_dict = {}
    for media_tv in media_index_list:
        media_tv_year = re.split("(.+) \((\d{4})\)", media_tv[2], flags=0)
        media_tv_year_int = int(media_tv_year[0])
        if tv_string in media_tv:
            if media_tv_year_int in tv_show_years_range:
                if media_tv_year_int not in tv_years_dict:
                    tv_years_dict[media_tv_year_int] = []
                tv_years_dict[media_tv_year_int].append(media_tv)
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_years_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
    tv_data = sorted(media_tv_year_totals.items())

    tv_years_terminal_graph_list = []

    for key, value in tv_data:
        tv_years_terminal_graph_list.append((str(key), value))

    graph = Pyasciigraph()
    for line in graph.graph('TV SHOWS: YEAR AMOUNTS', tv_years_terminal_graph_list):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


def get_movie_years_decades_totals_graphs_terminal():
    media_index_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_decades_dict = {}
    for media_movie in media_index_list:
        media_movie_year = re.split("(.+) \((\d{4})\)", media_movie[2], flags=0)
        media_movie_year_int = int(media_movie_year[0][:-1] + '0')
        if movie_string in media_movie:
            if media_movie_year_int in movie_years_range:
                if media_movie_year_int not in movie_years_decades_dict:
                    movie_years_decades_dict[media_movie_year_int] = []
                movie_years_decades_dict[media_movie_year_int].append(media_movie)
    media_movie_years_decades_totals = {}

    for movie_year_values, value in sorted(movie_years_decades_dict.items()):
        media_movie_years_decades_totals[movie_year_values] = len(value)

    movie_decades_terminal_graph_list = []

    for key, value in media_movie_years_decades_totals.items():
        movie_decades_terminal_graph_list.append((str(key), value))

    graph = Pyasciigraph()
    for line in graph.graph('MOVIES: DECADE AMOUNTS', movie_decades_terminal_graph_list):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


def get_tv_years_decades_totals_graphs_terminal():
    media_index_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_decades_amount_dict = {}
    for media_tv in media_index_list:
        media_tv_year = re.split("(.+) \((\d{4})\)", media_tv[2], flags=0)
        media_tv_year_int = int(media_tv_year[0][:-1] + '0')
        if tv_string in media_tv:
            if media_tv_year_int in tv_show_years_range:
                if media_tv_year_int not in tv_years_decades_amount_dict:
                    tv_years_decades_amount_dict[media_tv_year_int] = []
                tv_years_decades_amount_dict[media_tv_year_int].append(media_tv)
    media_tv_years_decades_totals = {}

    for tv_year_values, value in sorted(tv_years_decades_amount_dict.items()):
        media_tv_years_decades_totals[tv_year_values] = len(value)

    tv_decades_terminal_graph_list = []

    for key, value in media_tv_years_decades_totals.items():
        tv_decades_terminal_graph_list.append((str(key), value))

    graph = Pyasciigraph()
    for line in graph.graph('TV SHOWS: DECADE AMOUNTS', tv_decades_terminal_graph_list):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


def search_resolution_totals_movies_terminal():
    movie_files_results_list = list(
        csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    ten_eighty_found_list = []
    seven_twenty_found_list = []
    standard_def_found_list = []
    empty_response_list = []
    movies_total_list = []

    for res in movie_files_results_list:

        if re.findall("19\d{2}x", res[2]):
            ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[2]):
            seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[2]):
            standard_def_found_list.append(res)
        else:
            empty_response_list.append(+1)
        movies_total_list.append(+1)

    movies_graph_terminal_results = [('1080p', float(len(ten_eighty_found_list))),
                                     ('720p', float(len(seven_twenty_found_list))),
                                     ('SD (Below 720p)', float(len(standard_def_found_list)))]

    graph = Pyasciigraph()
    for line in graph.graph('MOVIES: RESOLUTION PERCENTAGES', movies_graph_terminal_results):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


def search_resolution_totals_tv_shows_terminal():
    tv_files_results_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    ten_eighty_found_list = []
    seven_twenty_found_list = []
    standard_def_found_list = []
    empty_response_list = []
    movies_total_list = []

    for res in tv_files_results_list:

        if re.findall("19\d{2}x", res[5]):
            ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[5]):
            seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[5]):
            standard_def_found_list.append(res)
        else:
            empty_response_list.append(+1)
        movies_total_list.append(+1)

    tv_shows_graph_terminal_results = [('1080p', float(len(ten_eighty_found_list))),
                                       ('720p', float(len(seven_twenty_found_list))),
                                       ('SD (Below 720p)', float(len(standard_def_found_list)))]

    graph = Pyasciigraph()
    for line in graph.graph('TV SHOWS: RESOLUTION PERCENTAGES', tv_shows_graph_terminal_results):
        print(line)
        print("--------------------------------------------------------------------------------------------------")
    print()
    print()


while True:
    run_terminal_graphs()
