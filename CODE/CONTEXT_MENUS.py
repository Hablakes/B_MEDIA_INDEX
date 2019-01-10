import os

from CODE import GRAPHS_BAR
from CODE import GRAPHS_PIE
from CODE import GRAPHS_TERMINAL
from CODE import MEDIA_FILE_PATHS_INDEX
from CODE import QUERY_MEDIA_FILES_INDICES
from CODE import QUERY_MEDIA_FOLDERS_INDEX
from CODE import PARSE_MEDIA_FILES
from CODE import SCRAPE_MEDIA_FOLDERS_INDEX
from CODE import SORT_OPTIONS
from CODE import YEAR_TOTALS


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
        first_launch_dirs()
    elif first_lmi_input_action_lower == 2:
        second_launch_lmi()
    elif first_lmi_input_action_lower == 3:
        exit()


def first_launch_dirs():
    username_input = []
    movie_dir_input = []
    tv_dir_input = []
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    username_input.append(input("ENTER YOUR USERNAME (CASE-SENSITIVE):"))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    movie_dir_input.append(input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):"))
    tv_dir_input.append(input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):"))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()

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
    launch_media_index()


def second_launch_lmi():
    username_input = []
    movie_dir_input = []
    tv_dir_input = []
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    username_input.append(input("ENTER YOUR USERNAME (CASE-SENSITIVE):"))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
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
        run_query()
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
        QUERY_MEDIA_FOLDERS_INDEX.movie_title_search()
    elif title_search_type_lower == 2:
        QUERY_MEDIA_FOLDERS_INDEX.tv_title_search()
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
    sort_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    sort_options = int(sort_input)
    if sort_options == 1:
        SORT_OPTIONS.get_title_ascending()
    elif sort_options == 2:
        SORT_OPTIONS.get_title_descending()
    elif sort_options == 3:
        SORT_OPTIONS.get_year_ascending()
    elif sort_options == 4:
        SORT_OPTIONS.get_year_descending()
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
    data_query_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    data_query_options = int(data_query_input)
    if data_query_options == 1:
        QUERY_MEDIA_FILES_INDICES.movie_files_info_query()
    elif data_query_options == 2:
        QUERY_MEDIA_FILES_INDICES.tv_files_info_query()
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
    graph_options_int = int(graph_options)
    if graph_options_int == 1:
        GRAPHS_BAR.bar_graph_options_base()
        GRAPHS_PIE.pie_chart_options_base()
    elif graph_options_int == 2:
        GRAPHS_TERMINAL.terminal_graph_options_base_0()
        GRAPHS_TERMINAL.terminal_graph_options_base_1()
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
    print("5) MOVIES (RESOLUTIONS PERCENTAGES) - 6) TV SHOWS (RESOLUTIONS PERCENTAGES)          - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    graph_options_int = int(graph_options)
    if graph_options_int == 1:
        pass
    elif graph_options_int == 2:
        pass
    elif graph_options_int == 3:
        pass
    elif graph_options_int == 4:
        pass
    elif graph_options_int == 5:
        pass
    elif graph_options_int == 6:
        pass
    elif graph_options_int == 7:
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
    graph_options_int = int(graph_options)
    if graph_options_int == 1:
        pass
    elif graph_options_int == 2:
        pass
    elif graph_options_int == 3:
        pass
    elif graph_options_int == 4:
        pass
    elif graph_options_int == 5:
        pass
    elif graph_options_int == 6:
        pass
    elif graph_options_int == 7:
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
    b_totals_query_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    b_totals_query_action = int(b_totals_query_input)
    if b_totals_query_action == 1:
        YEAR_TOTALS.movie_year_totals()
    elif b_totals_query_action == 2:
        YEAR_TOTALS.movie_decades_totals()
    elif b_totals_query_action == 3:
        YEAR_TOTALS.movie_titles_amount()
    elif b_totals_query_action == 4:
        YEAR_TOTALS.tv_year_totals()
    elif b_totals_query_action == 5:
        YEAR_TOTALS.tv_decades_totals()
    elif b_totals_query_action == 6:
        YEAR_TOTALS.tv_titles_amount()
    elif b_totals_query_action == 7:
        launch_media_index()


def create_media_indices_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX FROM FOLDERS   -  2) CREATE NEW MEDIA INDEX FROM FILES")
    print()
    print("3) CREATE NEW MOVIE PARSE-RESULTS INDEX  -  4) CREATE NEW TV-SHOWS PARSE-RESULTS INDEX")
    print()
    print("5) CREATE ALL NEW INDICES                -  6) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_input)
    if cmi_action == 1:
        MEDIA_FILE_PATHS_INDEX.search_folder_items_and_save_file_paths()
    elif cmi_action == 2:
        SCRAPE_MEDIA_FOLDERS_INDEX.scrape_media_folders_info_for_csv()
    elif cmi_action == 3:
        PARSE_MEDIA_FILES.movie_index_results()
    elif cmi_action == 4:
        PARSE_MEDIA_FILES.tv_show_index_results()
    elif cmi_action == 6:
        MEDIA_FILE_PATHS_INDEX.search_folder_items_and_save_file_paths()
        SCRAPE_MEDIA_FOLDERS_INDEX.scrape_media_folders_info_for_csv()
        PARSE_MEDIA_FILES.create_media_files_index_results_csv()
    elif cmi_action == 6:
        launch_media_index()


first_launch_media_index()
