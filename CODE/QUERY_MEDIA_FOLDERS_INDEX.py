import csv
import re

movie_string = str("MOVIE")
tv_string = str("TV")


def movie_title_search(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/MEDIA-INDEX.csv')))
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


def tv_title_search(username_input):
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/MEDIA-INDEX.csv')))
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
