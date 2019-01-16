import csv
import re

years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")


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


def library_total_amount(username_input):
    media_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    tv_index_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv')))
    tv_amounts_list = []
    episode_amounts_list = []
    movie_amounts_list = []
    for counted_movie_title in media_index_list:
        if movie_string in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)

    for counted_tv_title in media_index_list:
        if tv_string in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)

    for counted_episode_title in tv_index_list:
        episode_amounts_list.append(+1)
    print()
    print("TOTAL AMOUNT OF MOVIES:")
    print()
    print(len(movie_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF TV SHOWS:")
    print()
    print(len(tv_amounts_list))
    print()
    print()
    print("TOTAL AMOUNT OF TV EPISODES:")
    print()
    print(len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print()
    print("TOTAL AMOUNT OF ITEMS IN MEDIA-LIBRARY:")
    print()
    print(len(movie_amounts_list) + len(episode_amounts_list))
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()


def total_tv_episodes_in_show_title(username_input):
    tv_results_list = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}

    print()
    tv_total_query_action = input("ENTER TV SHOW TITLE:")
    print()
    print("--------------------------------------------------------------------------------------------------")
    tv_total_query_action_lower = tv_total_query_action.lower()
    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        if tv_total_query_action_lower in found_tv_title.lower():
            tv_show_episodes_found.append(found_tv_title)
            tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)
    for item in tv_show_found.items():
        print()
        print("TITLE NAME: # OF EPISODES")
        print()
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
