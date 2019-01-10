import csv
import os

years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")

username_input = [input("ENTER YOUR USERNAME (CASE-SENSITIVE):")]

movies_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")


def get_movie_years_for_dict():
    media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    movie_years_amount_dict = {}
    movie_totals_query_action = input("ENTER #")
    movie_totals_query_action = int(movie_totals_query_action)
    for media_movie in media_index_list:
        media_movie_year = int(media_movie[2])
        if movie_string in media_movie:
            if media_movie_year in years_range:
                if media_movie_year not in movie_years_amount_dict:
                    movie_years_amount_dict[media_movie_year] = []
                movie_years_amount_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_amount_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    movie_data = sorted(media_movie_year_totals.items())
    for movie_year_query in movie_data:
        if movie_totals_query_action in movie_year_query:
            print(movie_year_query[1])


def get_movie_titles_amount():
    media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print(len(movie_amounts_list))


def get_tv_years_for_dict():
    media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    tv_years_amount_dict = {}
    tv_totals_query_action = input("ENTER #")
    tv_totals_query_action = int(tv_totals_query_action)
    for media_tv in media_index_list:
        media_tv_year = int(media_tv[2])
        if tv_string in media_tv:
            if media_tv_year in years_range:
                if media_tv_year not in tv_years_amount_dict:
                    tv_years_amount_dict[media_tv_year] = []
                tv_years_amount_dict[media_tv_year].append(media_tv)
    media_tv_year_totals = {}
    for tv_year_values, value in sorted(tv_years_amount_dict.items()):
        media_tv_year_totals[tv_year_values] = len(value)
    tv_data = sorted(media_tv_year_totals.items())
    for tv_year_query in tv_data:
        if tv_totals_query_action in tv_year_query:
            print(tv_year_query[1])


def get_tv_titles_amount():
    media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    tv_amounts_list = []
    for counted_tv_title in media_index_list:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)
    print(len(tv_amounts_list))
