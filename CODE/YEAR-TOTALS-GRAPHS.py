import csv
import re

import matplotlib.pylab as plt

media_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_years_dict = {}

movie_string = str("MOVIE")
tv_string = str("TV")


def get_movie_years_for_dict_and_graph():
    for media_movie in media_index:
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
    for media_tv in media_index:
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


get_movie_years_for_dict_and_graph()
get_tv_years_for_dict_and_graph()
