import csv
import re

from ascii_graph import Pyasciigraph

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")


def terminal_graph_options_base_0(username_input, terminal_graph_options_int):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))

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
        csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    tv_files_results_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv')))

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
