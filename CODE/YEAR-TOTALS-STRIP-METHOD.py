import csv
import os

movie_p_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_p_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")


movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}


def get_movie_years_for_dict():
    for media_movie in movie_p_dir:
        media_movie_year = int(media_movie.strip()[-5:-1])
        if media_movie_year in movie_years_range:
            if media_movie_year not in movie_years_dict:
                movie_years_dict[media_movie_year] = []
            movie_years_dict[media_movie_year].append(media_movie)


def get_tv_years_for_dict():
    for media_tv in tv_p_dir:
        media_tv_year = int(media_tv.strip()[-5:-1])
        if media_tv_year in tv_show_years_range:
            if media_tv_year not in tv_show_years_dict:
                tv_show_years_dict[media_tv_year] = []
            tv_show_years_dict[media_tv_year].append(media_tv)


get_movie_years_for_dict()
get_tv_years_for_dict()


def display_movie_year_list_totals():
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
        # print(movie_year_values)
        # print(len(value))
    print(media_movie_year_totals)


def display_tv_year_list_totals():
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_show_years_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
        # print(tv_year_values)
        # print(len(value))
    print(media_tv_year_totals)


display_movie_year_list_totals()
display_tv_year_list_totals()
