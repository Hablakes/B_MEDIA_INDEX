import csv
import os
import re

import matplotlib.pylab as plt

media_index = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))
media_index_list = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))

movies_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")
tv_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/TV/")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_years_dict = {}

movie_years_amount_dict = {}
tv_years_amount_dict = {}

movie_amounts_list = []
tv_amounts_list = []

found_movie_info = []
found_tv_info = []

found_movie_info_sorted = sorted(found_movie_info)
found_tv_info_sorted = sorted(found_tv_info)

movie_string = str("MOVIE")
tv_string = str("TV")


def movie_title_search():
    print()
    movie_title_search_action = input("QUERY MOVIES:")
    movie_title_search_action = movie_title_search_action.lower()
    print()
    print("SEARCH RESULTS:")
    print()
    print("MOVIES:")
    print()
    for movie_search_result in media_index_list:
        if movie_string in movie_search_result[0]:
            movie_search_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result), flags=0)
            #            print(movie_search_info[0])
            if movie_title_search_action in movie_search_info[0].lower():
                print(movie_search_info[0])


def tv_title_search():
    print()
    tv_title_search_action = input("QUERY TV SHOWS:")
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
            #            print(movie_search_info[0])
            if tv_title_search_action in tv_search_info[0].lower():
                print(tv_search_info[0])


def get_title_ascending():
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    for item in sorted_title:
        print(item)


def get_title_descending():
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    for item in sorted_title_r:
        print(item)


def get_year_ascending():
    sorted_year = sorted(media_index, key=lambda y: (y[0], y[2]))
    for item in sorted_year:
        print(item)


def get_year_descending():
    sorted_year_r = sorted(media_index, key=lambda y: (y[0], y[2]), reverse=True)
    for item in sorted_year_r:
        print(item)


def run_query():
    print()
    print("___     _  _ ____ ___  _ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |\/| |___ |  \ | |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |  | |___ |__/ | |  |    |_\| |__| |___ |  \   |   ")
    print()
    print("SEARCH TITLES - 1) MOVIES - 2) TV SHOWS - 3) EXIT")
    print()
    title_search_type = input("ENTER #")
    title_search_type_lower = int(title_search_type)
    if title_search_type_lower == 1:
        movie_title_search()
    elif title_search_type_lower == 2:
        tv_title_search()
    elif title_search_type_lower == 3:
        launch_media_index()


def run_sort():
    print("___     _  _ ____ ___  _ ____    ____ ____ ____ ___")
    print("|__] __ |\/| |___ |  \ | |__| __ [__  |  | |__/  |")
    print("|__]    |  | |___ |__/ | |  |    ___] |__| |  \  | ")
    print()
    print("TITLE - 1) ASCENDING 2) DESCENDING - YEAR - 3)ASCENDING 4) DESCENDING - 5) EXIT")
    print()
    sort_options = input("ENTER #")
    print()
    sort_options = int(sort_options)
    if sort_options == 1:
        get_title_ascending()
    elif sort_options == 2:
        get_title_descending()
    elif sort_options == 3:
        get_year_ascending()
    elif sort_options == 4:
        get_year_descending()
    elif sort_options == 5:
        launch_media_index()


def scrape_movie_info_for_csv():
    for movie_found in movies_dir:
        movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
        scraped_movie_title = movie_scrape_info[1]
        scraped_movie_year = movie_scrape_info[2]
        #       print(movie_scrape_info[1], movie_scrape_info[2])
        found_movie_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])


def scrape_tv_info_for_csv():
    for tv_found in tv_dir:
        tv_scrape_info = re.search("(.+) \((\d{4})\)", str(tv_found), flags=0)
        scraped_movie_title = tv_scrape_info[1]
        scraped_movie_year = tv_scrape_info[2]
        #       print(tv_scrape_info[1], tv_scrape_info[2])
        found_movie_info.append(["TV", tv_scrape_info[1], tv_scrape_info[2]])


def create_media_index_csv():
    scrape_movie_info_for_csv()
    scrape_tv_info_for_csv()
    with open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in found_movie_info:
            csv_writer.writerow(movie_row)
        for tv_row in found_tv_info:
            csv_writer.writerow(tv_row)


def get_movie_years_for_dict_and_graph():
    for media_movie in media_index:
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

    x, y = zip(*movie_data)

    plt.bar(x, y)
    plt.savefig(r'C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\MOVIE-YEAR-RESULTS.png')
    plt.show()


def get_tv_years_for_dict_and_graph():
    for media_tv in media_index:
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

    x, y = zip(*tv_data)

    plt.bar(x, y)
    plt.savefig(r'C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\TV-YEAR-RESULTS.png')
    plt.show()


def run_graphs():
    print("___     ____ ____ ____ ___  _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | __ |__/ |__| |__] |__| __ |  | |__]  |  | |  | |\ | [__")
    print("|__]    |__] |  \ |  | |    |  |    |__| |     |  | |__| | \| ___]")
    print()
    print("1) MOVIES (TITLES PER YEAR) - 2) TV SHOWS (TITLES PER YEAR) - 3) EXIT")
    print()
    graph_options = input("ENTER #")
    print()
    graph_options = int(graph_options)
    if graph_options == 1:
        get_movie_years_for_dict_and_graph()
    elif graph_options == 2:
        get_tv_years_for_dict_and_graph()
    elif graph_options == 3:
        launch_media_index()


def totals_query():
    print("___     ___ ____ ___ ____ _    ____    ____ _  _ ____ ____ _   _")
    print("|__] __  |  |  |  |  |__| |    [__  __ |  | |  | |___ |__/  \_/ ")
    print("|__]     |  |__|  |  |  | |___ ___]    |_\| |__| |___ |  \   |   ")
    print()
    print("1) MOVIES BY YEAR - 2) MOVIES TOTAL - 3) TV SHOWS BY YEAR 4) TV SHOWS TOTAL - 5) EXIT")
    print()
    b_totals_query_action = input("ENTER #")
    print()
    b_totals_query_action = int(b_totals_query_action)
    if b_totals_query_action == 1:
        get_movie_years_for_dict()
    elif b_totals_query_action == 2:
        get_movie_titles_amount()
    elif b_totals_query_action == 3:
        get_tv_years_for_dict()
    elif b_totals_query_action == 4:
        get_tv_titles_amount()
    elif b_totals_query_action == 5:
        exit()


def get_movie_years_for_dict():
    movie_totals_query_action = input("ENTER #")
    movie_totals_query_action = int(movie_totals_query_action)
    for media_movie in media_index:
        media_movie_year = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(media_movie), flags=0)
        media_movie_year = int(media_movie[2])
        if movie_string in media_movie:
            if media_movie_year in movie_years_range:
                if media_movie_year not in movie_years_amount_dict:
                    movie_years_amount_dict[media_movie_year] = []
                movie_years_amount_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_amount_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    #   print(media_movie_year_totals)
    movie_data = sorted(media_movie_year_totals.items())
    for movie_year_query in movie_data:
        if movie_totals_query_action in movie_year_query:
            print()
            print("# OF MOVIES IN THIS YEAR:")
            print(movie_year_query[1])
            print()


def get_movie_titles_amount():
    for counted_movie_title in media_index:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print(len(movie_amounts_list))
    print()


def get_tv_years_for_dict():
    tv_totals_query_action = input("ENTER #")
    tv_totals_query_action = int(tv_totals_query_action)
    for media_tv in media_index:
        media_tv_year = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(media_tv), flags=0)
        media_tv_year = int(media_tv[2])
        if tv_string in media_tv:
            if media_tv_year in tv_show_years_range:
                if media_tv_year not in tv_years_amount_dict:
                    tv_years_amount_dict[media_tv_year] = []
                tv_years_amount_dict[media_tv_year].append(media_tv)
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_years_amount_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
    #   print(media_tv_year_totals)
    tv_data = sorted(media_tv_year_totals.items())
    for tv_year_query in tv_data:
        if tv_totals_query_action in tv_year_query:
            print()
            print("# OF TV SHOWS IN THIS YEAR:")
            print(tv_year_query[1])
            print()


def get_tv_titles_amount():
    for counted_tv_title in media_index:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print(len(tv_amounts_list))
    print()


def launch_media_index():
    print("___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("|__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/")
    print("|__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("1) QUERY INDEX - 2) SORT OPTIONS - 3) GRAPHS - 4) TOTALS - 5) RE-SCAN INDEX - 6) EXIT")
    print()
    lmi_action = input("ENTER #")
    print()
    lmi_action = int(lmi_action)
    if lmi_action == 1:
        run_query()
    elif lmi_action == 2:
        run_sort()
    elif lmi_action == 3:
        run_graphs()
    elif lmi_action == 4:
        totals_query()
    elif lmi_action == 5:
        create_media_index_csv()
    elif lmi_action == 6:
        exit()


while True:
    launch_media_index()
