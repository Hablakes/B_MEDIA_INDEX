import csv
import os
import re

media_index = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movies_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")

movie_years_range = range(1900, 2100, 1)
tv_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_years_dict = {}

movie_string = str("MOVIE")
tv_string = str("TV")

totals_query_action = input("ENTER #")
totals_query_action = int(totals_query_action)


def get_movie_years_for_dict():
    for media_movie in media_index:
        media_movie_year = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(media_movie), flags=0)
        media_movie_year = int(media_movie[2])
        if movie_string in media_movie:
            if media_movie_year in movie_years_range:
                if media_movie_year not in movie_years_dict:
                    movie_years_dict[media_movie_year] = []
                movie_years_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    #   print(media_movie_year_totals)
    movie_data = sorted(media_movie_year_totals.items())
    for year_query in movie_data:
        if totals_query_action in year_query:
            print(year_query[1])


get_movie_years_for_dict()
