import csv
import os
import re

media_index = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}

movie_string = str("MOVIE")
tv_string = str("TV")


def get_movie_years_for_dict():
    for movie_year_string in media_index:
        if movie_string in movie_year_string:
            media_movie_year = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_year_string[2]), flags=0)
            print(media_movie_year[0])


def get_tv_years_for_dict():
    for tv_year_string in media_index:
        if tv_string in tv_year_string:
            media_tv_year = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_year_string[2]), flags=0)
            print(media_tv_year)


get_movie_years_for_dict()
get_tv_years_for_dict()
