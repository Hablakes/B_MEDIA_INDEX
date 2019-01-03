import csv
import re

media_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_years_dict = {}

movie_string = str("MOVIE")
tv_string = str("TV")


def get_movie_years_decade_totals():
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
    print(int(media_movie_year_totals[2019] + media_movie_year_totals[2018] + media_movie_year_totals[2017] +
              media_movie_year_totals[2016] + media_movie_year_totals[2015] + media_movie_year_totals[2014] +
              media_movie_year_totals[2013] + media_movie_year_totals[2012] + media_movie_year_totals[2011] +
              media_movie_year_totals[2010]))



get_movie_years_decade_totals()
