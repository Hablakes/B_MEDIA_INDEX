import csv
import os

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


def create_media_indices_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX                -  2) UPDATE MEDIA INDEX")
    print()
    print("3) CREATE NEW NFO INDICES                -  4) UPDATE PARSE-RESULTS INDICES")
    print()
    print("5) CREATE NEW PARSE-RESULTS INDICES      -  6) UPDATE ALL INDICES")
    print()
    print("7) CREATE ALL NEW INDICES                -  8) COMPARE AGAINST ANOTHER RESULTS FILE")
    print()
    print("9) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_input)
