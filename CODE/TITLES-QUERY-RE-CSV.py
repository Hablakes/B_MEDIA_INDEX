import csv
import re

media_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_string = str("MOVIE")
tv_string = str("TV")


def run_title_search():
    print()
    print("SEARCH TITLES - 1) MOVIES 2) TV SHOWS - 3) EXIT")
    print()
    title_search_type = input("ENTER #")
    title_search_type_lower = int(title_search_type)
    if title_search_type_lower == 1:
        movie_title_search()
    elif title_search_type_lower == 2:
        tv_title_search()
    elif title_search_type_lower == 3:
        exit()


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


while True:
    run_title_search()
