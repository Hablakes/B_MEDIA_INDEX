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


def title_search():
    for search_result in media_index_list:
        search_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(search_result[0]), flags=0)
        search_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(search_result[1]), flags=0)
        search_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(search_result[2]), flags=0)
        print()






