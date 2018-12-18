import csv
import re

media_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_string = str("MOVIE")
tv_string = str("TV")

movie_section_results = []
movie_title_results = []
movie_year_results = []
tv_section_results = []
tv_title_results = []
tv_year_results = []


def run_title_search():
    print()
    print("SEARCH TITLES - 1) MOVIES 2) TV SHOWS - 3) EXIT")
    title_search_type = input("ENTER #")
    title_search_type_lower = title_search_type.lower()
    if title_search_type_lower == 1:
        movie_title_search()
    elif title_search_type_lower == 2:
        tv_title_search()
    elif title_search_type_lower == 3:
        exit()


def movie_title_search():
    print()
    movie_title_search_action = input("QUERY MOVIES:")
    movie_title_search_action_lower = movie_title_search_action.lower()
    print()
    print("SEARCH RESULTS:")
    print()
    print("MOVIES:")
    print()
    for movie_search_result in media_index_list:
        if movie_string in movie_search_result[0]:
            movie_search_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[0]),
                                                 flags=0)
            movie_search_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[1]),
                                               flags=0)
            movie_search_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[2]),
                                              flags=0)
            movie_section_results.append(movie_search_section_info[0])
            #            movie_section_results_sorted = sorted(movie_section_results)
            movie_title_results.append(movie_search_title_info[0])
            #            movie_title_results_sorted = sorted(movie_title_results)
            movie_year_results.append(movie_search_year_info[0])
    #            movie_year_results_sorted = sorted(movie_year_results)
    for movie_title_searched in movie_title_results:
        if movie_title_search_action_lower in movie_title_searched:
            print(movie_title_searched)


def tv_title_search():
    print()
    tv_title_search_action = input("QUERY TV SHOWS:")
    tv_title_search_action_lower = tv_title_search_action.lower()
    print()
    print("SEARCH RESULTS:")
    print()
    print("TV SHOWS:")
    print()
    for tv_search_result in media_index_list:
        if tv_string in tv_search_result:
            tv_search_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[0]), flags=0)
            tv_search_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[1]), flags=0)
            tv_search_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[2]), flags=0)
            print(tv_search_title_info[0])
            tv_section_results.append(tv_search_section_info[0])
            #            tv_section_results_sorted = sorted(tv_section_results)
            tv_title_results.append(tv_search_title_info[0])
            #            tv_title_results_sorted = sorted(tv_title_results)
            tv_year_results.append(tv_search_year_info[0])
    #            tv_year_results_sorted = sorted(tv_year_results)
    for tv_title_searched in tv_title_results:
        if tv_title_search_action_lower in tv_title_searched:
            print(tv_title_searched)
