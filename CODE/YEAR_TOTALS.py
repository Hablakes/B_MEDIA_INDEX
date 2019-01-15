import csv
import re

years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")


def movie_year_totals(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    movie_totals_query_action = input("ENTER #")
    print()
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
            print()
            print("# OF MOVIES IN THIS YEAR:")
            print()
            print(movie_year_query[1])
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()


def movie_decades_totals(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_years_decades_dict = {}
    for media_movie in media_index_list:
        media_movie_year = re.split("(.+) \((\d{4})\)", media_movie[2], flags=0)
        media_movie_year_int = int(media_movie_year[0][:-1] + '0')
        if movie_string in media_movie:
            if media_movie_year_int in years_range:
                if media_movie_year_int not in movie_years_decades_dict:
                    movie_years_decades_dict[media_movie_year_int] = []
                movie_years_decades_dict[media_movie_year_int].append(media_movie)
    media_movie_years_decades_totals = {}

    for movie_year_values, value in sorted(movie_years_decades_dict.items()):
        media_movie_years_decades_totals[movie_year_values] = len(value)
    print()
    print("# OF MOVIES BY DECADE:")
    print()
    print(media_movie_years_decades_totals)
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def movie_titles_amount(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def tv_year_totals(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_amount_dict = {}
    print("ENTER A YEAR:")
    print()
    tv_totals_query_action = input("ENTER #")
    print()
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
            print()
            print("# OF TV SHOWS IN THIS YEAR:")
            print()
            print(tv_year_query[1])
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()


def tv_decades_totals(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_years_decades_amount_dict = {}
    for media_tv in media_index_list:
        media_tv_year = re.split("(.+) \((\d{4})\)", media_tv[2], flags=0)
        media_tv_year_int = int(media_tv_year[0][:-1] + '0')
        if tv_string in media_tv:
            if media_tv_year_int in years_range:
                if media_tv_year_int not in tv_years_decades_amount_dict:
                    tv_years_decades_amount_dict[media_tv_year_int] = []
                tv_years_decades_amount_dict[media_tv_year_int].append(media_tv)
    media_tv_years_decades_totals = {}

    for tv_year_values, value in sorted(tv_years_decades_amount_dict.items()):
        media_tv_years_decades_totals[tv_year_values] = len(value)
    print()
    print("# OF TV SHOWS BY DECADE:")
    print()
    print(media_tv_years_decades_totals)
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def tv_titles_amount(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv')))
    tv_amounts_list = []
    episode_amounts_list = []
    for counted_tv_title in media_index_list:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)

    for counted_episode_title in tv_index_list:
        episode_amounts_list.append(+1)
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
