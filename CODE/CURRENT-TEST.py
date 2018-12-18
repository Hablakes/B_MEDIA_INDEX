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
    if title_search_type_lower == 1:
        movie_title_search()
    elif title_search_type_lower == 2:
        tv_title_search()
    elif title_search_type_lower == 3:
        exit()


def movie_title_search():
    for movie_search_result in media_index_list:
        if movie_string in movie_search_result[0]:
            movie_search_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[0]), flags=0)
            movie_search_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[1]), flags=0)
            movie_search_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_search_result[2]), flags=0)
            print(movie_search_title_info[0])



def tv_title_search():
    for tv_search_result in media_index_list:
        if tv_string in tv_search_result:
            tv_search_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[0]), flags=0)
            tv_search_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[1]), flags=0)
            tv_search_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_search_result[2]), flags=0)
            print(tv_search_title_info[0])


print()
print("SEARCH TITLES - 1) MOVIES 2) TV SHOWS - 3) EXIT")
title_search_type = input("ENTER #")
title_search_type_lower = title_search_type.lower()
print()
title_search_action = input("QUERY?")
title_search_action_lower = title_search_action.lower()
print()
movie_title_search()
