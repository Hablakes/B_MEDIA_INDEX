import os

movie_dir = os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\TEST\MOVIES")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}


def get_movie_years_for_dict():
    for media_movie in movie_dir:
        media_movie_year = int(media_movie.strip()[-5:-1])
        if media_movie_year in movie_years_range:
            if media_movie_year not in movie_years_dict:
                movie_years_dict[media_movie_year] = []
            movie_years_dict[media_movie_year].append(media_movie)


get_movie_years_for_dict()


def display_movie_year_list_totals():
    media_year_totals = {}
    for year_values, value in sorted(movie_years_dict.items()):
        media_year_totals[year_values] = len(value)
        #print(year_values)
        #print(len(value))
    print(media_year_totals)


display_movie_year_list_totals()



"""
movie_year_totals = {}
for movie_totals in movie_years_dict:
    movie_year_totals[movie_totals] = movie_year_totals.get(movie_totals, 0) + 1

print(movie_year_totals)
"""
