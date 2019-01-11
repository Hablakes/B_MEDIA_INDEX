import csv
import re

import matplotlib.pylab as plt

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")


def bar_graph_options_base(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_dict = {}
    movie_decades_dict = {}
    tv_decades_amount_dict = {}
    tv_years_dict = {}
    movie_year_totals = {}
    movie_decades_totals = {}
    tv_year_totals = {}
    tv_decades_totals = {}

    for title_item in media_index_list:
        title_item_year = re.split("(.+) \((\d{4})\)", title_item[2], flags=0)
        title_item_year_int = int(title_item_year[0])
        title_item_decade_int = int(title_item_year[0][:-1] + '0')
        if title_item_year_int in years_range:
            if movie_string in title_item:
                if title_item_year_int not in movie_years_dict:
                    movie_years_dict[title_item_year_int] = []
                movie_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in movie_decades_dict:
                    movie_decades_dict[title_item_decade_int] = []
                movie_decades_dict[title_item_decade_int].append(title_item)
            if tv_string in title_item:
                if title_item_year_int not in tv_years_dict:
                    tv_years_dict[title_item_year_int] = []
                tv_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in tv_decades_amount_dict:
                    tv_decades_amount_dict[title_item_decade_int] = []
                tv_decades_amount_dict[title_item_decade_int].append(title_item)

    for year_values, value in sorted(movie_years_dict.items()):
        movie_year_totals[year_values] = len(value)
    x, y = zip(*sorted(movie_year_totals.items()))
    plt.bar(x, y)
    plt.savefig(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-YEAR-RESULTS.png')
    plt.show()

    for year_values, value in sorted(movie_decades_dict.items()):
        movie_decades_totals[year_values] = len(value)
    x, y = zip(*movie_decades_totals.items())
    plt.bar(x, y, width=5)
    plt.savefig(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-DECADE-RESULTS.png')
    plt.show()

    for year_values, value in sorted(tv_years_dict.items()):
        tv_year_totals[year_values] = len(value)
    x, y = zip(*sorted(tv_year_totals.items()))
    plt.bar(x, y)
    plt.savefig(r'/home/' + username_input + '/MEDIA-INDEX/TV-YEAR-RESULTS.png')
    plt.show()

    for year_values, value in sorted(tv_decades_amount_dict.items()):
        tv_decades_totals[year_values] = len(value)
    x, y = zip(*tv_decades_totals.items())
    plt.bar(x, y, width=5)
    plt.savefig(r'/home/' + username_input + '/MEDIA-INDEX/TV-DECADE-RESULTS.png')
    plt.show()
