import csv

import matplotlib.pylab as plt
from ascii_graph import Pyasciigraph

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


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
