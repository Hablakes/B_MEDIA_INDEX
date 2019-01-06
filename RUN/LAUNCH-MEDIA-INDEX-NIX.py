import csv
import os
import re

import guessit
import matplotlib.pylab as plt
import numpy as np
import pymediainfo

media_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_files_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))
movie_files_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv')))

tv_files_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv'))
tv_files_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv')))

movie_files_results = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-RESULTS.csv'))
movie_files_results_list = list(
    csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-RESULTS.csv')))

tv_files_results = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS.csv'))
tv_files_results_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS.csv')))

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"
tv_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"
alt_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"

movie_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")
tv_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")
alt_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")

movie_walk_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")
tv_walk_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")
alt_walk_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")


def movie_title_search():
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


def tv_title_search():
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


def get_title_ascending():
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    for item in sorted_title:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_title_descending():
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    for item in sorted_title_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_ascending():
    sorted_year = sorted(media_index, key=lambda y: (y[0], y[2]))
    for item in sorted_year:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_descending():
    sorted_year_r = sorted(media_index, key=lambda y: (y[0], y[2]), reverse=True)
    for item in sorted_year_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_movie_years_for_dict_and_graph():
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

    x, y = zip(*movie_data)

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-YEAR-RESULTS.png')
    plt.show()


def get_tv_years_for_dict_and_graph():
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

    x, y = zip(*tv_data)

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-YEAR-RESULTS.png')
    plt.show()


def get_movie_years_decades_totals_graphs():
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

    x, y = zip(*media_movie_years_decades_totals.items())

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-DECADE-RESULTS.png')
    plt.show()


def get_tv_years_decades_totals_graphs():
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

    x, y = zip(*media_tv_years_decades_totals.items())

    plt.bar(x, y)
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-DECADE-RESULTS.png')
    plt.show()


def search_resolution_totals_movies():
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

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

    labels = ['1080p', '720p', 'SD (Below 720p)']

    data = [float(len(ten_eighty_found_list)), float(len(seven_twenty_found_list)),
            float(len(standard_def_found_list))]

    def format_movie_data(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    colors = ['#85c1e9', '#a569bd', '#808b96']

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: format_movie_data(pct, data),
                                      shadow=True, colors=colors, textprops=dict(color="black"))

    ax.legend(wedges, labels,
              title="RESOLUTIONS",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=9, weight='bold')
    ax.set_title("MOVIE-RESOLUTION-RESULTS")
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-RESOLUTION-RESULTS.png')
    plt.show()


def search_resolution_totals_tv_shows():
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

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

    labels = ['1080p', '720p', 'SD (Below 720p)']

    data = [float(len(ten_eighty_found_list)), float(len(seven_twenty_found_list)),
            float(len(standard_def_found_list))]

    def format_movie_data(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    colors = ['#85c1e9', '#a569bd', '#808b96']

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: format_movie_data(pct, data),
                                      shadow=True, colors=colors, textprops=dict(color="black"))

    ax.legend(wedges, labels,
              title="RESOLUTIONS",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=9, weight='bold')
    ax.set_title("TV-SHOW-RESOLUTION-RESULTS")
    plt.savefig(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-SHOW-RESOLUTION-RESULTS.png')
    plt.show()


def scrape_media_info_for_csv():
    found_movie_info = []
    found_tv_info = []

    for movie_found in movie_dir_list:
        movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
        found_movie_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])

    for tv_found in tv_dir_list:
        tv_scrape_info = re.search("(.+) \((\d{4})\)", str(tv_found), flags=0)
        found_tv_info.append(["TV", tv_scrape_info[1], tv_scrape_info[2]])

    for alt_found in alt_dir_list:
        alt_scrape_info = re.search("(.+) \((\d{4})\)", str(alt_found), flags=0)
        found_tv_info.append(["TV", alt_scrape_info[1], alt_scrape_info[2]])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(found_movie_info):
            csv_writer.writerow(movie_row)

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(found_tv_info):
            csv_writer.writerow(tv_row)


def search_movie_folders_items():
    movie_file_results = []
    for root, dirs, files in os.walk(movie_dir):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)


def search_tv_show_folders_items():
    tv_show_file_results = []
    for root, dirs, files in os.walk(tv_dir):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    for root, dirs, files in os.walk(alt_dir):
        for alt_file in sorted(files):
            if alt_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + alt_file])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)


def get_movie_index_results():
    search_movie_folders_items()
    movie_index_file_results = []

    for movie_file in movie_files_index:

        title = guessit.guessit(movie_file[0], options={'type': 'episode'})

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video' and track not in movie_files_results_list:
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-RESULTS.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)


def get_tv_show_index_results():
    search_tv_show_folders_items()
    tv_index_file_results = []

    for tv_file in tv_files_index:

        title = guessit.guessit(tv_file[0], options={'type': 'episode', 'episode-prefer-number': True})

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video' and track not in tv_files_results_list:
                tv_index_file_results.append(
                    [title.get('title'), title.get('episode_title'), title.get('season'), title.get('episode'),
                     title.get('year'), str(track.width) + 'x' + str(track.height), title.get('container')])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


def create_media_files_index_results_csv():
    get_movie_index_results()
    get_tv_show_index_results()


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
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("TITLE - 1) ASCENDING - 2) DESCENDING - YEAR - 3) ASCENDING - 4) DESCENDING           - 5) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    sort_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
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
    data_query_options = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    data_query_options = int(data_query_options)
    if data_query_options == 1:
        movie_query_action()
    elif data_query_options == 2:
        tv_shows_query_action()
    elif data_query_options == 3:
        launch_media_index()


def movie_query_action():
    mv_query_action = input("ENTER SEARCH QUERY (MOVIES):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    mv_query_action_lower = str(mv_query_action.lower())
    for movie_file in sorted(movie_files_results_list):
        if mv_query_action_lower in movie_file[0].lower():
            print()
            print("MOVIE TITLE:")
            print(movie_file[0])
            print()
            print("MOVIE YEAR:")
            print(movie_file[1])
            print()
            print("MOVIE RESOLUTION:")
            print(movie_file[2])
            print()
            print("MOVIE FILE TYPE:")
            print(movie_file[3])
            print()
            print()
            print("--------------------------------------------------------------------------------------------------")


def tv_shows_query_action():
    tv_show_query_action = input("ENTER SEARCH QUERY (TV SHOWS):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    tv_show_query_action_lower = str(tv_show_query_action.lower())
    for tv_file in sorted(tv_files_results_list):
        if tv_show_query_action_lower in tv_file[0].lower():
            print()
            print("TV SHOW TITLE:")
            print(tv_file[0])
            print()
            print("TV SHOW EPISODE TITLE:")
            print(tv_file[1])
            print()
            print("TV SHOW SEASON #:")
            print(tv_file[2])
            print()
            print("TV SHOW EPISODE #:")
            print(tv_file[3])
            print()
            print("TV SHOW YEAR:")
            print(tv_file[4])
            print()
            print("TV SHOW RESOLUTION:")
            print(tv_file[5])
            print()
            print("TV SHOW FILE-TYPE:")
            print(tv_file[6])
            print()
            print()
            print("--------------------------------------------------------------------------------------------------")


def run_graphs():
    print("___     ____ ____ ____ ___  _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | __ |__/ |__| |__] |__| __ |  | |__]  |  | |  | |\ | [__")
    print("|__]    |__] |  \ |  | |    |  |    |__| |     |  | |__| | \| ___]")
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
        get_movie_years_for_dict_and_graph()
    elif graph_options == 2:
        get_tv_years_for_dict_and_graph()
    elif graph_options == 3:
        get_movie_years_decades_totals_graphs()
    elif graph_options == 4:
        get_tv_years_decades_totals_graphs()
    elif graph_options == 5:
        search_resolution_totals_movies()
    elif graph_options == 6:
        search_resolution_totals_tv_shows()
    elif graph_options == 7:
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
    b_totals_query_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    b_totals_query_action = int(b_totals_query_action)
    if b_totals_query_action == 1:
        get_movie_years_for_dict()
    elif b_totals_query_action == 2:
        get_movie_years_decades_totals()
    elif b_totals_query_action == 3:
        get_movie_titles_amount()
    elif b_totals_query_action == 4:
        get_tv_years_for_dict()
    elif b_totals_query_action == 5:
        get_tv_years_decades_totals()
    elif b_totals_query_action == 6:
        get_tv_titles_amount()
    elif b_totals_query_action == 7:
        launch_media_index()


def get_movie_years_for_dict():
    movie_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    movie_totals_query_action = input("ENTER #")
    print()
    movie_totals_query_action = int(movie_totals_query_action)
    for media_movie in media_index:
        media_movie_year = int(media_movie[2])
        if movie_string in media_movie:
            if media_movie_year in movie_years_range:
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


def get_movie_years_decades_totals():
    movie_years_decades_dict = {}
    for media_movie in media_index:
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
    print()
    print("# OF MOVIES BY DECADE:")
    print()
    print(media_movie_years_decades_totals)
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def get_movie_titles_amount():
    movie_amounts_list = []
    for counted_movie_title in media_index:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def get_tv_years_for_dict():
    tv_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    tv_totals_query_action = input("ENTER #")
    print()
    tv_totals_query_action = int(tv_totals_query_action)
    for media_tv in media_index:
        media_tv_year = int(media_tv[2])
        if tv_string in media_tv:
            if media_tv_year in tv_show_years_range:
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


def get_tv_years_decades_totals():
    tv_years_decades_amount_dict = {}
    for media_tv in media_index:
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
    print()
    print("# OF TV SHOWS BY DECADE:")
    print()
    print(media_tv_years_decades_totals)
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def get_tv_titles_amount():
    tv_amounts_list = []
    for counted_tv_title in media_index:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def create_media_indexes_all():
    print("___     _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__] __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__ ")
    print("|__]    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX FROM DIRECTORIES - 2) CREATE NEW MEDIA INDEX FROM FILES    - 3) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    cmi_action = int(cmi_action)
    if cmi_action == 1:
        scrape_media_info_for_csv()
    elif cmi_action == 2:
        create_media_files_index_results_csv()
    elif cmi_action == 3:
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
    lmi_action = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    lmi_action = int(lmi_action)
    if lmi_action == 1:
        run_query()
    elif lmi_action == 2:
        run_sort()
    elif lmi_action == 3:
        file_query_and_sort()
    elif lmi_action == 4:
        run_graphs()
    elif lmi_action == 5:
        totals_query()
    elif lmi_action == 6:
        create_media_indexes_all()
    elif lmi_action == 0:
        exit()


while True:
    launch_media_index()
