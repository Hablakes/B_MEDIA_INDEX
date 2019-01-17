import os

from CODE import FILE_TOTALS
from CODE import FILE_TYPE_TOTALS
from CODE import GRAPHS_BAR
from CODE import GRAPHS_PIE
from CODE import GRAPHS_TERMINAL
from CODE import MEDIA_FILE_INDEX
from CODE import QUERY_MEDIA_FILES_INDICES
from CODE import QUERY_MEDIA_FOLDERS_INDEX
from CODE import PARSE_MEDIA_FILES
from CODE import PARSE_UPDATED_MEDIA_FILES
from CODE import RE_SORT_CSV_INDICES
from CODE import MEDIA_FOLDERS_INDEX
from CODE import SORT_OPTIONS
from CODE import UPDATE_AND_COMPARE_MEDIA_FILE_INDICES
from CODE import YEAR_TOTALS

username_input = None


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
    first_lmi_input_action_lower = first_lmi_input_action.lower()
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    if int(first_lmi_input_action_lower) == 1:
        first_launch_dirs()
    elif int(first_lmi_input_action_lower) == 2:
        second_launch_lmi()
    elif int(first_lmi_input_action_lower) == 3:
        exit()


def first_launch_dirs():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global username_input
    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input
    movie_dir_input = input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):")
    tv_dir_input = input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):")
    movie_alt_dir_input = input("ENTER PATH OF ANY ALTERNATE MOVIE DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
    tv_alt_dir_input = input("ENTER PATH OF ANY ALTERNATE TV SHOW DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()

    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/', exist_ok=True)
    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES', exist_ok=True)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as mi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as mfi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tfi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv', 'w') as om:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/OLD-TV-FILES-INDEX.csv', 'w') as ot:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as mfr:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tfr:
        pass
    launch_media_index()


def second_launch_lmi():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global username_input
    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
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
        QUERY_MEDIA_FOLDERS_INDEX.movie_title_search(username_input)
    elif title_search_type_lower == 2:
        QUERY_MEDIA_FOLDERS_INDEX.tv_title_search(username_input)
    elif title_search_type_lower == 3:
        launch_media_index()


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
        SORT_OPTIONS.sort_function_base(username_input, sort_options_int=1)
    elif sort_options_int == 2:
        SORT_OPTIONS.sort_function_base(username_input, sort_options_int=2)
    elif sort_options_int == 3:
        SORT_OPTIONS.sort_function_base(username_input, sort_options_int=3)
    elif sort_options_int == 4:
        SORT_OPTIONS.sort_function_base(username_input, sort_options_int=4)
    elif sort_options_int == 5:
        SORT_OPTIONS.total_tv_episodes_sort_function_base(username_input, sort_options_int=5)
    elif sort_options_int == 6:
        SORT_OPTIONS.total_tv_episodes_sort_function_base(username_input, sort_options_int=6)
    elif sort_options_int == 7:
        SORT_OPTIONS.total_tv_episodes_sort_function_base(username_input, sort_options_int=7)
    elif sort_options_int == 8:
        SORT_OPTIONS.total_tv_episodes_sort_function_base(username_input, sort_options_int=8)
    elif sort_options_int == 9:
        launch_media_index()


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
        QUERY_MEDIA_FILES_INDICES.movie_files_info_query(username_input)
    elif data_query_int == 2:
        QUERY_MEDIA_FILES_INDICES.tv_files_info_query(username_input)
    elif data_query_int == 3:
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
        GRAPHS_BAR.bar_graph_options_base(username_input, picture_graph_options_int=1)
    elif picture_graph_options_int == 2:
        GRAPHS_BAR.bar_graph_options_base(username_input, picture_graph_options_int=2)
    elif picture_graph_options_int == 3:
        GRAPHS_BAR.bar_graph_options_base(username_input, picture_graph_options_int=3)
    elif picture_graph_options_int == 4:
        GRAPHS_BAR.bar_graph_options_base(username_input, picture_graph_options_int=4)
    elif picture_graph_options_int == 5:
        GRAPHS_PIE.pie_chart_options_base(username_input, picture_graph_options_int=5)
    elif picture_graph_options_int == 6:
        GRAPHS_PIE.pie_chart_options_base(username_input, picture_graph_options_int=6)
    elif picture_graph_options_int == 7:
        FILE_TYPE_TOTALS.search_file_type_totals_movies(username_input, picture_graph_options_int=7,
                                                        terminal_graph_options_int='', b_totals_query_input_int='')
    elif picture_graph_options_int == 8:
        FILE_TYPE_TOTALS.search_file_type_totals_tv(username_input, picture_graph_options_int=8,
                                                    terminal_graph_options_int='', b_totals_query_input_int='')
    elif picture_graph_options_int == 9:
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
        GRAPHS_TERMINAL.terminal_graph_options_base_0(username_input, terminal_graph_options_int=1)
    elif terminal_graph_options_int == 2:
        GRAPHS_TERMINAL.terminal_graph_options_base_0(username_input, terminal_graph_options_int=2)
    elif terminal_graph_options_int == 3:
        GRAPHS_TERMINAL.terminal_graph_options_base_0(username_input, terminal_graph_options_int=3)
    elif terminal_graph_options_int == 4:
        GRAPHS_TERMINAL.terminal_graph_options_base_0(username_input, terminal_graph_options_int=4)
    elif terminal_graph_options_int == 5:
        GRAPHS_TERMINAL.terminal_graph_options_base_1(username_input, terminal_graph_options_int=5)
    elif terminal_graph_options_int == 6:
        GRAPHS_TERMINAL.terminal_graph_options_base_1(username_input, terminal_graph_options_int=6)
    elif terminal_graph_options_int == 7:
        FILE_TYPE_TOTALS.search_file_type_totals_movies(username_input, terminal_graph_options_int=7,
                                                        picture_graph_options_int='', b_totals_query_input_int='')
    elif terminal_graph_options_int == 8:
        FILE_TYPE_TOTALS.search_file_type_totals_tv(username_input, terminal_graph_options_int=8,
                                                    picture_graph_options_int='', b_totals_query_input_int='')
    elif terminal_graph_options_int == 9:
        launch_media_index()


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
        YEAR_TOTALS.movie_year_totals(username_input)
    elif b_totals_query_input_int == 2:
        YEAR_TOTALS.tv_year_totals(username_input)
    elif b_totals_query_input_int == 3:
        FILE_TOTALS.movie_titles_amount(username_input)
    elif b_totals_query_input_int == 4:
        FILE_TOTALS.tv_titles_amount(username_input)
    elif b_totals_query_input_int == 5:
        YEAR_TOTALS.movie_decades_totals(username_input)
    elif b_totals_query_input_int == 6:
        YEAR_TOTALS.tv_decades_totals(username_input)
    elif b_totals_query_input_int == 7:
        FILE_TYPE_TOTALS.search_file_type_totals_movies(username_input, b_totals_query_input_int=7,
                                                        picture_graph_options_int='', terminal_graph_options_int='')
    elif b_totals_query_input_int == 8:
        FILE_TYPE_TOTALS.search_file_type_totals_tv(username_input, b_totals_query_input_int=8,
                                                    picture_graph_options_int='', terminal_graph_options_int='')
    elif b_totals_query_input_int == 9:
        FILE_TOTALS.total_tv_episodes_in_show_title(username_input)
    elif b_totals_query_input_int == 10:
        FILE_TOTALS.library_total_amount(username_input)
    elif b_totals_query_input_int == 11:
        launch_media_index()


def create_media_indices_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX                -  2) UPDATE MEDIA INDEX")
    print()
    print("3) CREATE NEW PARSE-RESULTS INDICES      -  4) UPDATE PARSE-RESULTS INDICES")
    print()
    print("5) CREATE ALL NEW INDICES                -  6) UPDATE ALL INDICES                    - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_input)
    if cmi_action == 1:
        MEDIA_FOLDERS_INDEX.scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                                              movie_alt_dir_input, tv_alt_dir_input)
        MEDIA_FILE_INDEX.search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input,
                                                                 movie_alt_dir_input, tv_alt_dir_input)
    elif cmi_action == 2:
        UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.compare_old_and_updated_indices_and_create_differences_files(
            username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
    elif cmi_action == 3:
        PARSE_MEDIA_FILES.create_media_files_index_results_csv(username_input)
    elif cmi_action == 4:
        PARSE_UPDATED_MEDIA_FILES.create_media_files_index_results_csv(username_input)
        RE_SORT_CSV_INDICES.re_sort_csv_indices(username_input)
    elif cmi_action == 5:
        MEDIA_FOLDERS_INDEX.scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                                              movie_alt_dir_input, tv_alt_dir_input)
        MEDIA_FILE_INDEX.search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input,
                                                                 movie_alt_dir_input, tv_alt_dir_input)
        PARSE_MEDIA_FILES.create_media_files_index_results_csv(username_input)
    elif cmi_action == 6:
        MEDIA_FOLDERS_INDEX.scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input,
                                                              movie_alt_dir_input, tv_alt_dir_input)
        UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.compare_old_and_updated_indices_and_create_differences_files(
            username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input)
        PARSE_UPDATED_MEDIA_FILES.create_media_files_index_results_csv(username_input)
        RE_SORT_CSV_INDICES.re_sort_csv_indices(username_input)
    elif cmi_action == 7:
        launch_media_index()
