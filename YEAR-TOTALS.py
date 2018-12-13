import os

movie_dir = os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\TEST\MOVIES")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}

movie_years_totals = {}
tv_show_years_totals = {}


def get_movie_years_for_dict():
    for media_movie in movie_dir:
        media_movie_year = int(media_movie.strip()[-5:-1])
        if media_movie_year in movie_years_range:
            if media_movie_year not in movie_years_dict:
                movie_years_dict[media_movie_year] = []
            movie_years_dict[media_movie_year].append(media_movie)


get_movie_years_for_dict()


def display_movie_year_list_totals():
    for year_lists, value in sorted(movie_years_dict.items()):
        print(year_lists)
        print(value)


display_movie_year_list_totals()
