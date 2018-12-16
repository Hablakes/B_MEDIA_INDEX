import csv
import itertools
import os

import matplotlib.pylab as plt

movie_p_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_p_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")

movies_dir = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")
tv_dir = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")
tv2_dir = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}

media_index = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

found = []
found = sorted(found)


def movie_search(lower_title_search, movies_dir):
    for movie_result in movies_dir:
        if lower_title_search in movie_result.lower():
            print(movie_result)
        else:
            continue


def tv_search(lower_title_search, tv_dir):
    for tv_result in tv_dir:
        if lower_title_search in tv_result.lower():
            print(tv_result)
        else:
            continue


def tv2_search(lower_title_search, tv2_dir):
    for tv_result in tv2_dir:
        if lower_title_search in tv_result.lower():
            print(tv_result)
        else:
            continue


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


def run_base():
    print()
    print("___     _  _ ____ ___  _ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |\/| |___ |  \ | |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |  | |___ |__/ | |  |    |_\| |__| |___ |  \   |   ")
    print()
    print("MEDIA SEARCH:")
    print()
    title_search = input("QUERY?")
    if title_search == str("RESTART-INDEX"):
        launch_media_index()
    print()
    lower_title_search = title_search.lower()
    print()
    print("MOVIES")
    print()
    movie_search(lower_title_search, sorted(movies_dir))
    print()
    print("TV")
    print()
    tv_search(lower_title_search, sorted(tv_dir))
    tv2_search(lower_title_search, sorted(tv2_dir))


def run_sort():
    print("___     _  _ ____ ___  _ ____    ____ ____ ____ ___")
    print("|__] __ |\/| |___ |  \ | |__| __ [__  |  | |__/  |")
    print("|__]    |  | |___ |__/ | |  |    ___] |__| |  \  | ")
    print()
    print("METHOD? - TITLE - 1) ASCENDING 2) DESCENDING - YEAR - 3)ASCENDING 4) DESCENDING - 5) EXIT")
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


def movie_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")


def tv_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")


def tv2_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")


def create_media_index_csv():
    for movie in movie_listdir():
        movie_title = movie.strip()[0:-7]
        movie_year = movie.strip()[-5:-1]
        found.append(["MOVIE", movie_title, movie_year])

    for tv in tv_listdir():
        tv_title = tv.strip()[0:-7]
        tv_year = tv.strip()[-5:-1]
        found.append(["TV", tv_title, tv_year])

    for tv2 in tv2_listdir():
        tv2_title = tv2.strip()[0:-7]
        tv2_year = tv2.strip()[-5:-1]
        found.append(["TV", tv2_title, tv2_year])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for row in found:
            csv_writer.writerow(row)


def get_movie_years_for_dict():
    for media_movie in movie_p_dir:
        media_movie_year = int(media_movie.strip()[-5:-1])
        if media_movie_year in movie_years_range:
            if media_movie_year not in movie_years_dict:
                movie_years_dict[media_movie_year] = []
            movie_years_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    # print(media_movie_year_totals)
    movie_data = sorted(media_movie_year_totals.items())

    x, y = zip(*movie_data)

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-YEAR-RESULTS.png')
    plt.show()


def get_tv_years_for_dict():
    for media_tv in tv_p_dir:
        media_tv_year = int(media_tv.strip()[-5:-1])
        if media_tv_year in tv_show_years_range:
            if media_tv_year not in tv_show_years_dict:
                tv_show_years_dict[media_tv_year] = []
            tv_show_years_dict[media_tv_year].append(media_tv)
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_show_years_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
    tv_data = sorted(media_tv_year_totals.items())

    x, y = zip(*tv_data)

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-YEAR-RESULTS.png')
    plt.show()


def run_graphs():
    print("___     ____ ____ ____ ___  _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | __ |__/ |__| |__] |__| __ |  | |__]  |  | |  | |\ | [__")
    print("|__]    |__] |  \ |  | |    |  |    |__| |     |  | |__| | \| ___]")
    print()
    print("ACTION? - 1) MOVIES (TITLES PER YEAR) - 2) TV SHOWS (TITLES PER YEAR) - 3) EXIT")
    print()
    graph_options = input("ENTER #")
    print()
    graph_options = int(graph_options)
    if graph_options == 1:
        get_movie_years_for_dict()
    elif graph_options == 2:
        get_tv_years_for_dict()
    elif graph_options == 3:
        launch_media_index()


def launch_media_index():
    print(" ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print(" |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/")
    print(" |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("ACTION? - 1) QUERY INDEX - 2) SORT OPTIONS - 3) GRAPHS - 4) RE-SCAN INDEX - 5) EXIT")
    print()
    action = input("ENTER #")
    print()
    action = int(action)
    if action == 1:
        run_base()
    elif action == 2:
        run_sort()
    elif action == 3:
        run_graphs()
    elif action == 4:
        create_media_index_csv()
    elif action == 5:
        exit()


while True:
    launch_media_index()

