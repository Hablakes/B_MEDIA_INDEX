import csv
import os
import pathlib
import textwrap

import re

import guessit
import pyfiglet
import pymediainfo

from ascii_graph import Pyasciigraph
from tkinter import *
from tkinter import filedialog

username_input = None
media_index_folder = '~/{0}_MEDIA_INDEX'

extensions = ('.3gp', '.asf', '.asx', '.avc', '.avi', '.bdmv', '.bin', '.bivx', '.dat', '.disc', '.divx', '.dv',
              '.dvr-ms', '.evo', '.fli', '.flv', '.h264', '.img', '.iso', '.m2ts', '.m2v', '.m4v', '.mkv', '.mov',
              '.mp4', '.mpeg', '.mpg', '.mt2s', '.mts', '.nfo', '.nrg', '.nsv', '.nuv', '.ogm', '.pva', '.qt', '.rm',
              '.rmvb', '.strm', '.svq3', '.ts', '.ty', '.viv', '.vob', '.vp3', '.wmv', '.xvid', '.webm')


def main():
    launch_media_index()
    while True:
        media_index_home()


def compare_results(results_user, results_other):
    output = []

    for line in results_user:
        if line not in results_other:
            output.append('HAVE: ' + line)

    for line in results_other:
        if line not in results_user:
            output.append('DO NOT HAVE: ' + line)

    return output


def change_directory_selection():
    print(pyfiglet.figlet_format('CHANGE_DIRECTORY', font='cybermedium'))
    separator()
    directory_selection()


def create_media_information_indices():
    create_movie_information_index()
    create_tv_information_index()


def create_movie_information_index():
    movie_index = csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MOVIE_VIDEO_FILES_PATHS.csv').format(username_input)), encoding='UTF-8'))
    movie_index_file_results = {}

    for movie_file in sorted(movie_index):
        movie_title_key = movie_file[0].rsplit('/')[-2]
        movie_filename_key = movie_file[0].rsplit('/', 1)[-1]
        if movie_title_key not in movie_index_file_results:
            movie_index_file_results[movie_title_key] = {}
        if movie_filename_key.lower() != '.nfo':
            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})
            try:
                test = pymediainfo.MediaInfo.parse(movie_file[0])
            except OSError as e:
                print('OS ERROR: ', e)
                continue

            for track in test.tracks:
                if track.track_type == 'Video':
                    movie_index_file_results[movie_title_key]['DIRECTORY'] = movie_title_key
                    movie_index_file_results[movie_title_key]['TITLE'] = title.get('title')
                    movie_index_file_results[movie_title_key]['YEAR'] = title.get('year')
                    movie_index_file_results[movie_title_key]['RESOLUTION'] = str(track.width) + 'x' + str(track.height)
                    movie_index_file_results[movie_title_key]['FILE-TYPE'] = title.get('container')
                    movie_index_file_results[movie_title_key]['FILENAME'] = movie_filename_key

        elif movie_file[0].lower().endswith('.nfo'):
            try:
                with open(movie_file[0]) as f:
                    for line_item in f.readlines():
                        if '<plot>' in line_item:
                            movie_index_file_results[movie_title_key]['PLOT'] = line_item

                        if '<rating>' in line_item:
                            movie_index_file_results[movie_title_key]['RATING'] = line_item

                        if '<runtime>' in line_item:
                            movie_index_file_results[movie_title_key]['RUN-TIME'] = line_item
            except Exception as e:
                print('ERROR: ', e)
                print('FILE: ', movie_file[0])
                continue

    with open(os.path.expanduser((media_index_folder + '/MOVIE_INFORMATION_INDEX.csv').format(username_input)), 'w',
              encoding='UTF-8', newline='') as f:

        csv_writer = csv.DictWriter(f, ['DIRECTORY', 'TITLE', 'YEAR', 'RESOLUTION', 'FILE-TYPE', 'PLOT', 'RATING',
                                        'RUN-TIME', 'FILENAME'])
        for movie_row in movie_index_file_results.values():
            csv_writer.writerow(movie_row)


def create_tv_information_index():
    tv_index = csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_VIDEO_FILES_PATHS.csv').format(username_input)), encoding='UTF-8'))
    tv_index_file_results = {}

    for tv_file in sorted(tv_index):
        tv_title_key = tv_file[0].rsplit('/', 1)[-1][:-4]
        tv_folder_title = tv_file[0].rsplit('/')[-2]
        tv_filename_key = tv_file[0].rsplit('/', 1)[-1]
        if tv_title_key not in tv_index_file_results:
            tv_index_file_results[tv_title_key] = {}
        if tv_filename_key.lower() != '.nfo':
            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})
            try:
                test = pymediainfo.MediaInfo.parse(tv_file[0])
            except OSError as e:
                print('OS ERROR: ', e)
                continue

            for track in test.tracks:
                if track.track_type == 'Video':
                    tv_index_file_results[tv_title_key]['DIRECTORY'] = tv_folder_title
                    tv_index_file_results[tv_title_key]['TITLE'] = title.get('title')
                    tv_index_file_results[tv_title_key]['YEAR'] = title.get('year')
                    tv_index_file_results[tv_title_key]['EPISODE TITLE'] = title.get('episode_title')
                    tv_index_file_results[tv_title_key]['SEASON'] = title.get('season')
                    tv_index_file_results[tv_title_key]['EPISODE NUMBER'] = title.get('episode')
                    tv_index_file_results[tv_title_key]['RESOLUTION'] = str(track.width) + 'x' + str(track.height)
                    tv_index_file_results[tv_title_key]['FILE-TYPE'] = title.get('container')
                    tv_index_file_results[tv_title_key]['FILENAME'] = tv_filename_key

        elif tv_file[0].lower().endswith('.nfo') and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':
            if tv_title_key not in tv_index_file_results:
                tv_index_file_results[tv_title_key] = {}
                try:
                    with open(tv_file[0]) as f:
                        for line in f.readlines():
                            if '<plot>' in line:
                                tv_index_file_results[tv_title_key]['PLOT'] = line

                            if '<rating>' in line:
                                tv_index_file_results[tv_title_key]['RATING'] = line

                            if '<runtime>' in line:
                                tv_index_file_results[tv_title_key]['RUN-TIME'] = line
                except Exception as e:
                    print('ERROR: ', e)
                    print('FILE: ', tv_file[0])
                    continue

    with open(os.path.expanduser((media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), 'w',
              encoding='UTF-8', newline='') as f:
        csv_writer = csv.DictWriter(f, ['DIRECTORY', 'TITLE', 'YEAR', 'EPISODE TITLE', 'SEASON', 'EPISODE NUMBER',
                                        'RESOLUTION', 'FILE-TYPE', 'PLOT', 'RATING', 'RUN-TIME', 'FILENAME'])
        for tv_row in tv_index_file_results.values():
            csv_writer.writerow(tv_row)


def directory_selection():
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input

    try:
        user_info_file = os.path.expanduser((media_index_folder + '/{0}_USER_INFO.csv').format(username_input))

        print('ENTER PATH OF MOVIE DIRECTORY, IF NONE HIT CANCEL: ')
        movie_dir_input = tk_gui_file_browser_window()
        print()
        print('ENTER PATH OF TV DIRECTORY, IF NONE HIT CANCEL: ')
        tv_dir_input = tk_gui_file_browser_window()
        print()
        print('ENTER PATH OF ALTERNATE MOVIE DIRECTORY, IF NONE HIT CANCEL: ')
        movie_alt_dir_input = tk_gui_file_browser_window()
        print()
        print('ENTER PATH OF ALTERNATE TV DIRECTORY, IF NONE HIT CANCEL: ')
        tv_alt_dir_input = tk_gui_file_browser_window()
        separator()

        user_info_dict = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                          'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}

        with open(user_info_file, 'w', encoding='UTF-8', newline='') as f:
            csv_writer = csv.writer(f)
            for user_data in user_info_dict.items():
                csv_writer.writerow(user_data)
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)


def divider():
    for items in '\n', '-' * 100:
        print(items)


def launch_media_index():
    print(pyfiglet.figlet_format('MEDIA_INDEX', font='cybermedium'))
    separator()

    global username_input

    username_input = input('ENTER YOUR USERNAME (CASE-SENSITIVE): ')
    separator()
    username_check_and_folder_creation()


def library_total_amount():
    media_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF-8')))
    tv_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_VIDEO_FILES_PATHS.csv').format(username_input)), encoding='UTF-8')))
    tv_amounts_list = []
    episode_amounts_list = []
    movie_amounts_list = []

    for counted_movie_title in media_index_list:
        if str('MOVIE') in counted_movie_title:
            movie_amounts_list.append(counted_movie_title)
    for counted_tv_title in media_index_list:
        if str('TV') in counted_tv_title:
            tv_amounts_list.append(counted_tv_title)
    for _ in tv_index_list:
        episode_amounts_list.append(+1)

    print()
    print('TOTAL AMOUNT OF MOVIES: ')
    print()
    print(len(movie_amounts_list))
    separator()
    print()
    print('TOTAL AMOUNT OF TV SHOWS: ')
    print()
    print(len(tv_amounts_list))
    print()
    print()
    print('TOTAL AMOUNT OF TV EPISODES: ')
    print()
    print(len(episode_amounts_list))
    separator()
    print()
    print('TOTAL AMOUNT OF ITEMS IN MEDIA-LIBRARY: ')
    print()
    print(len(movie_amounts_list) + len(episode_amounts_list))
    separator()


def media_index_home():
    username_check_and_folder_creation()
    print(pyfiglet.figlet_format('MEDIA_INDEX', font='cybermedium'))
    separator()

    print('1) CHANGE DATABASE DIRECTORIES                   2) CREATE PATH INDICES')
    print()
    print('3) CREATE TITLE INDEX                            4) CREATE MEDIA INFORMATION INDICES')
    print()
    print('5) COMPARE TWO USERS INFORMATION INDICES         6) DISPLAY LIBRARY TOTALS')
    print()
    print('7) MEDIA INFORMATION QUERIES                     8) SORT OPTIONS')
    print()
    print('9) TERMINAL GRAPH OPTIONS                        0) EXIT')
    separator()

    try:
        lmi_input = input('ENTER #: ')
        separator()
        lmi_input_action = int(lmi_input)

        if lmi_input_action == 0:
            exit()
        elif lmi_input_action == 1:
            change_directory_selection()
        elif lmi_input_action == 2:
            walk_directories_and_create_indices()
        elif lmi_input_action == 3:
            scrape_media_folders_for_csv()
        elif lmi_input_action == 4:
            create_media_information_indices()
        elif lmi_input_action == 5:
            select_users_indices_to_compare()
        elif lmi_input_action == 6:
            library_total_amount()
        elif lmi_input_action == 7:
            media_queries_sub_menu()
        elif lmi_input_action == 8:
            sort_options_sub_menu()
        elif lmi_input_action == 9:
            terminal_graphs_options_sub_menu()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('PLEASE RETRY YOUR SELECTION USING THE NUMBER KEYS')
        separator()


def media_queries_sub_menu():
    print(pyfiglet.figlet_format('MEDIA_QUERIES', font='cybermedium'))
    separator()

    print('SEARCH FOR TITLES OF:                            1) MOVIES       2) TV SHOWS')
    print()
    print('SEARCH FOR INFORMATION OF:                       3) MOVIES       4) TV SHOWS')
    print()
    print('                                                 0) EXIT')
    separator()

    try:
        title_search_type = int(input('ENTER #: '))
        separator()

        if title_search_type == 0:
            media_index_home()
        elif title_search_type == 1:
            search_titles(title_search_type=1)
        elif title_search_type == 2:
            search_titles(title_search_type=2)
        elif title_search_type == 3:
            query_movie_information_index()
        elif title_search_type == 4:
            query_tv_information_index()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('PLEASE RETRY YOUR SELECTION USING THE NUMBER KEYS')
        separator()


def query_movie_information_index():
    mv_files_results_list = csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MOVIE_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8'))

    try:
        mv_query_action = input('ENTER SEARCH QUERY (MOVIES): ')
        separator()
        mv_query_action_lower = str(mv_query_action.lower())

        for movie_file in mv_files_results_list:
            if mv_query_action_lower in movie_file[1].lower():
                divider()
                print('MOVIE FOLDER: ')
                print()
                print(movie_file[0])
                divider()
                print('MOVIE TITLE: ')
                print()
                print(movie_file[1])
                divider()
                print('MOVIE YEAR: ')
                print()
                print(movie_file[2])
                divider()
                print('MOVIE RESOLUTION: ')
                print()
                print(movie_file[3])
                divider()
                print('MOVIE FILE-TYPE: ')
                print()
                print(movie_file[4])
                divider()
                if int(len(movie_file[7])) != 0:
                    print("RUN-TIME")
                    print()
                    if '</runtime>' not in movie_file[7]:
                        mv_runtime = re.findall("<runtime>(.*?)", movie_file[7])
                        print(mv_runtime[0], ": Minutes")
                        divider()
                    elif '</runtime>' in movie_file[7]:
                        mv_runtime = re.findall("<runtime>(.*?)</runtime>", movie_file[7])
                        print(mv_runtime[0], ": Minutes")
                        divider()
                if int(len(movie_file[6])) != 0:
                    print("RATING")
                    print()
                    if '</rating>' not in movie_file[6]:
                        mv_rating = re.findall("<rating>(.*?)", movie_file[6])
                        print(mv_rating[0])
                        divider()
                    elif '</rating>' in movie_file[6]:
                        mv_rating = re.findall("<rating>(.*?)</rating>", movie_file[6])
                        print(mv_rating[0])
                        divider()
                if int(len(movie_file[5])) != 0:
                    print("PLOT")
                    print()
                    if '</plot>' not in movie_file[5]:
                        mv_plot = re.findall("<plot>(.*?)", movie_file[5])
                        print(textwrap.fill(mv_plot[0], 100))
                        divider()
                    elif '</plot>' in movie_file[5]:
                        mv_plot = re.findall("<plot>(.*?)</plot>", movie_file[5])
                        print(textwrap.fill(mv_plot[0], 100))
                        divider()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('INVALID QUERY, PLEASE RETRY')
        separator()


def query_tv_information_index():
    tv_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))

    try:
        tv_show_query_action = input('ENTER SEARCH QUERY (TV SHOWS): ')
        separator()
        tv_show_query_action_lower = str(tv_show_query_action.lower())

        for tv_file in tv_files_results_list:
            if tv_show_query_action_lower in tv_file[1].lower() or tv_file[3].lower():
                divider()
                print('TV SHOW FOLDER')
                print()
                print(tv_file[0])
                divider()
                print('TV SHOW TITLE')
                print()
                print(tv_file[1])
                divider()
                print('TV SHOW YEAR')
                print()
                print(tv_file[2])
                divider()
                print('TV SHOW EPISODE TITLE')
                print()
                print(tv_file[3])
                divider()
                print('SEASON NUMBER')
                print()
                print(tv_file[4])
                divider()
                print('EPISODE NUMBER')
                print()
                print(tv_file[5])
                divider()
                print('RESOLUTION')
                print()
                print(tv_file[6])
                divider()
                print('FILE-TYPE')
                print()
                print(tv_file[7])
                divider()
                if int(len(tv_file[10])) != 0:
                    print("RUN-TIME")
                    print()
                    if '</runtime>' not in tv_file[10]:
                        tv_runtime = re.findall("<runtime>(.*?)", tv_file[10])
                        print(tv_runtime[0], ": Minutes")
                        divider()
                    elif '</runtime>' in tv_file[10]:
                        tv_runtime = re.findall("<runtime>(.*?)</runtime>", tv_file[10])
                        print(tv_runtime[0], ": Minutes")
                        divider()
                if int(len(tv_file[9])) != 0:
                    print("RATING")
                    print()
                    if '</rating>' not in tv_file[9]:
                        tv_rating = re.findall("<rating>(.*?)", tv_file[9])
                        print(tv_rating[0])
                        divider()
                    elif '</rating>' in tv_file[9]:
                        tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                        print(tv_rating[0])
                        divider()
                if int(len(tv_file[8])) != 0:
                    print("PLOT")
                    print()
                    if '</plot>' not in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)", tv_file[8])
                        print(textwrap.fill(tv_plot[0], 100))
                        divider()
                    elif '</plot>' in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                        print(textwrap.fill(tv_plot[0], 100))
                        divider()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('INVALID QUERY, PLEASE RETRY')
        separator()


def scrape_media_folders_for_csv():
    movie_title_items = []
    tv_title_items = []

    try:
        if movie_dir_input is not str(''):
            movie_dir_list = os.listdir(movie_dir_input)
            for movie_found in sorted(movie_dir_list):
                movie_scrape_info = guessit.guessit(movie_found)
                title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]
                if "," in title_item_check[2]:
                    title_item_check.append(title_item_check[2][-5:-1])
                    title_item_check.remove(title_item_check[2])
                movie_title_items.append(title_item_check)

        if movie_alt_dir_input is not str(''):
            movie_alt_dir_list = os.listdir(movie_alt_dir_input)
            for movie_found in sorted(movie_alt_dir_list):
                movie_scrape_info = guessit.guessit(movie_found)
                title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]
                if "," in title_item_check[2]:
                    title_item_check.append(title_item_check[2][-5:-1])
                    title_item_check.remove(title_item_check[2])
                movie_title_items.append(title_item_check)

        if tv_dir_input is not str(''):
            tv_dir_list = os.listdir(tv_dir_input)
            for tv_found in sorted(tv_dir_list):
                tv_scrape_info = guessit.guessit(tv_found)
                title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]
                if "," in title_item_check[2]:
                    title_item_check.append(title_item_check[2][-5:-1])
                    title_item_check.remove(title_item_check[2])
                tv_title_items.append(title_item_check)

        if tv_alt_dir_input is not str(''):
            tv_alt_dir_list = os.listdir(tv_alt_dir_input)
            for tv_found in sorted(tv_alt_dir_list):
                tv_scrape_info = guessit.guessit(tv_found)
                title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]
                if "," in title_item_check[2]:
                    title_item_check.append(title_item_check[2][-5:-1])
                    title_item_check.remove(title_item_check[2])
                tv_title_items.append(title_item_check)

        with open(os.path.expanduser((media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), 'w',
                  encoding='UTF-8', newline='') as f:
            csv_writer = csv.writer(f)
            for file_row in movie_title_items:
                csv_writer.writerow(file_row)
            for file_row in tv_title_items:
                csv_writer.writerow(file_row)
    except (OSError, TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('INCORRECT DIRECTORY INPUT(S), PLEASE RETRY')
        separator()


def search_file_type_totals(terminal_graph_options_int):
    movie_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MOVIE_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    tv_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    movie_extensions_dict = {}
    movie_extensions_totals = {}
    tv_extensions_dict = {}
    tv_extensions_totals = {}

    for file_type in movie_files_results_list:
        if str(',') not in file_type[4]:
            if file_type[4] not in movie_extensions_dict:
                movie_extensions_dict[file_type[4]] = []
            movie_extensions_dict[file_type[4]].append(file_type[4])
    if terminal_graph_options_int == 7:
        for file_type_values, value in sorted(movie_extensions_dict.items()):
            movie_extensions_totals[file_type_values] = len(value)
        file_type_totals_terminal_graph_list = []
        for key, value in movie_extensions_totals.items():
            file_type_totals_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: FILE-TYPE AMOUNTS: ', file_type_totals_terminal_graph_list):
            print()
            print(line)
        separator()

    for file_type in tv_files_results_list:
        if str(',') not in file_type[7]:
            if file_type[7] not in tv_extensions_dict:
                tv_extensions_dict[file_type[7]] = []
            tv_extensions_dict[file_type[7]].append(file_type[7])
    if terminal_graph_options_int == 8:
        for file_type_values, value in sorted(tv_extensions_dict.items()):
            tv_extensions_totals[file_type_values] = len(value)
        file_type_totals_terminal_graph_list = []
        for key, value in tv_extensions_totals.items():
            file_type_totals_terminal_graph_list.append((str(key), value))

        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: FILE-TYPE AMOUNTS: ', file_type_totals_terminal_graph_list):
            print()
            print(line)
        separator()


def search_titles(title_search_type):
    media_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF-8')))

    if title_search_type == 1:
        try:
            movie_title_search_action = input('QUERY MOVIES: ')
            separator()
            movie_title_search_action = movie_title_search_action.lower()

            print('SEARCH RESULTS: ')
            print()
            print('MOVIES: ')
            print()

            for movie_search_result in media_index_list:
                if str('MOVIE') in movie_search_result[0]:
                    movie_search_info = re.split('(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)', str(movie_search_result), flags=0)
                    if movie_title_search_action in movie_search_info[0].lower():
                        print(movie_search_info[0])
            separator()
        except (TypeError, ValueError) as e:
            print('INPUT ERROR: ', e)
            print()
            print('INVALID INPUT, PLEASE RETRY')
            separator()

    elif title_search_type == 2:
        try:
            tv_title_search_action = input('QUERY TV SHOWS: ')
            separator()
            tv_title_search_action = tv_title_search_action.lower()

            print()
            print()
            print('SEARCH RESULTS: ')
            print()
            print('TV SHOWS: ')
            print()

            for tv_search_result in media_index_list:
                if str('TV') in tv_search_result[0]:
                    tv_search_info = re.split('(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)', str(tv_search_result), flags=0)
                    if tv_title_search_action in tv_search_info[0].lower():
                        print(tv_search_info[0])
            separator()
        except (TypeError, ValueError) as e:
            print('INPUT ERROR: ', e)
            print()
            print('INVALID INPUT, PLEASE RETRY')
            separator()


def search_plots():
    movie_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MOVIE_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    tv_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    plots_list = []

    try:
        print('SEARCH PLOTS OF:                                 1) MOVIES       2) TV SHOWS')
        print()

        plot_search = input('KEYWORD(S): ')
        plot_search_lower = plot_search.lower()
        separator()

        for plot in movie_files_results_list:
            plots_list.append('MOVIE' + ' - ' + plot[0] + ' - ' + plot[5])
        for plot in tv_files_results_list:
            plots_list.append('TV SHOW' + ' - ' + plot[0] + ' - ' + plot[8])
        for items in plots_list:
            if plot_search_lower in items.lower():
                print()
                print(textwrap.fill(items, 100))
        separator()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('INVALID INPUT, PLEASE RETRY')
        separator()


def select_users_indices_to_compare():
    try:
        print()
        print('SELECT THE MOVIE_INFORMATION_INDICES TO COMPARE: ')
        separator()
        print('SELECT USER MOVIE INFORMATION INDEX: ')
        m_0 = tk_gui_file_selection_window()
        print('SELECT COMPARISON MOVIE INFORMATION INDEX: ')
        m_1 = tk_gui_file_selection_window()
        print('SELECT USER TV INFORMATION INDEX: ')
        t_0 = tk_gui_file_selection_window()
        print('SELECT COMPARISON TV INFORMATION INDEX: ')
        t_1 = tk_gui_file_selection_window()
        separator()

        with open(m_0, 'r', encoding='UTF-8') as movies_0, open(m_1, 'r', encoding='UTF-8') as movies_1:
            user_movie_results = movies_0.readlines()
            comparison_movie_results = movies_1.readlines()
            with open(os.path.expanduser(
                    (media_index_folder + '/FILES/MOVIE_COMPARISON_INDEX.csv').format(username_input)),
                    'w', encoding='UTF-8', newline='') as outFile_m:
                for line in compare_results(user_movie_results, comparison_movie_results):
                    outFile_m.write(line)

        with open(t_0, 'r', encoding='UTF-8') as tv_0, open(t_1, 'r', encoding='UTF-8') as tv_1:
            user_tv_results = tv_0.readlines()
            comparison_tv_results = tv_1.readlines()
            with open(os.path.expanduser(
                    (media_index_folder + '/FILES/TV_COMPARISON_INDEX.csv').format(username_input)),
                    'w', encoding='UTF-8', newline='') as outFile_t:
                for line in compare_results(user_tv_results, comparison_tv_results):
                    outFile_t.write(line)
    except (OSError, TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        separator()


def separator():
    for items in '\n', '-' * 100, '\n':
        print(items)


def sort_function_base(sort_options_int):
    media_index = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF-8')))

    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    sorted_year = sorted(media_index, key=lambda x: (x[0], x[2]))
    sorted_year_r = sorted(media_index, key=lambda x: (x[0], x[2]), reverse=True)

    if sort_options_int == 1:
        for title_item in sorted_title:
            print()
            print(title_item)
        separator()
    elif sort_options_int == 2:
        for title_item in sorted_title_r:
            print()
            print(title_item)
        separator()
    elif sort_options_int == 3:
        for title_item in sorted_year:
            print()
            print(title_item)
        separator()
    elif sort_options_int == 4:
        for title_item in sorted_year_r:
            print()
            print(title_item)
        separator()


def sort_options_sub_menu():
    print(pyfiglet.figlet_format('SORT_OPTIONS', font='cybermedium'))
    separator()

    print('SORT MOVIE & TV SHOW TITLES BY:      TITLES:     1) ASCENDING    2) DESCENDING')
    print()
    print('                                     YEARS:      3) ASCENDING    4) DESCENDING')
    print()
    print()
    print('SORT TV SHOW EPISODE(S) BY:          TITLES:     5) ASCENDING    6) DESCENDING')
    print()
    print('                                     EPISODES:   7) ASCENDING    8) DESCENDING')
    print()
    print('0) EXIT')
    separator()

    try:
        sort_input = input('ENTER #: ')
        separator()
        sort_options_int = int(sort_input)

        if sort_options_int == 0:
            media_index_home()
        elif sort_options_int == 1:
            sort_function_base(sort_options_int=1)
        elif sort_options_int == 2:
            sort_function_base(sort_options_int=2)
        elif sort_options_int == 3:
            sort_function_base(sort_options_int=3)
        elif sort_options_int == 4:
            sort_function_base(sort_options_int=4)
        elif sort_options_int == 5:
            tv_episodes_sort_function(sort_options_int=5)
        elif sort_options_int == 6:
            tv_episodes_sort_function(sort_options_int=6)
        elif sort_options_int == 7:
            tv_episodes_sort_function(sort_options_int=7)
        elif sort_options_int == 8:
            tv_episodes_sort_function(sort_options_int=8)
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('PLEASE RETRY YOUR SELECTION USING THE NUMBER KEYS')
        separator()


def terminal_graph_options_advanced(terminal_graph_options_int):
    movie_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MOVIE_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    tv_files_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    m_ten_eighty_found_list = []
    m_seven_twenty_found_list = []
    m_standard_def_found_list = []
    m_empty_response_list = []
    movies_total_list = []
    tv_ten_eighty_found_list = []
    tv_seven_twenty_found_list = []
    tv_standard_def_found_list = []
    tv_empty_response_list = []
    tv_total_list = []

    for res in movie_files_results_list:
        if re.findall('19\d{2}x', res[3]):
            m_ten_eighty_found_list.append(res)
        elif re.findall('1[0-8]\d{2}x', res[3]):
            m_seven_twenty_found_list.append(res)
        elif re.findall('\d{3}x', res[3]):
            m_standard_def_found_list.append(res)
        else:
            m_empty_response_list.append(+1)
        movies_total_list.append(+1)
    movies_graph_terminal_results = [('1080p', float(len(m_ten_eighty_found_list))),
                                     ('720p', float(len(m_seven_twenty_found_list))),
                                     ('SD (Below 720p)', float(len(m_standard_def_found_list)))]

    for res in tv_files_results_list:
        if re.findall('19\d{2}x', res[6]):
            tv_ten_eighty_found_list.append(res)
        elif re.findall('1[0-8]\d{2}x', res[6]):
            tv_seven_twenty_found_list.append(res)
        elif re.findall('\d{3}x', res[6]):
            tv_standard_def_found_list.append(res)
        else:
            tv_empty_response_list.append(+1)
        tv_total_list.append(+1)
    tv_shows_graph_terminal_results = [('1080p', float(len(tv_ten_eighty_found_list))),
                                       ('720p', float(len(tv_seven_twenty_found_list))),
                                       ('SD (Below 720p)', float(len(tv_standard_def_found_list)))]

    if terminal_graph_options_int == 5:
        graph = Pyasciigraph()
        for line in graph.graph('MOVIES: RESOLUTION PERCENTAGES: ', movies_graph_terminal_results):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 6:
        graph = Pyasciigraph()
        for line in graph.graph('TV SHOWS: RESOLUTION PERCENTAGES: ', tv_shows_graph_terminal_results):
            print()
            print(line)
        separator()


def terminal_graph_options_base(terminal_graph_options_int):
    media_index_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/MEDIA_TITLE_INDEX.csv').format(username_input)), encoding='UTF-8')))
    movie_years_dict = {}
    movie_decades_dict = {}
    tv_years_dict = {}
    tv_decades_amount_dict = {}
    movie_year_totals_dict = {}
    movie_decades_totals_dict = {}
    tv_year_totals_dict = {}
    tv_decades_totals_dict = {}

    for title_item in media_index_list:
        title_item_year = re.split('(.+) \((\d{4})\)', title_item[2], flags=0)
        title_item_year_int = int(title_item_year[0])
        title_item_decade_int = int(title_item_year[0][:-1] + '0')

        if title_item_year_int in range(1900, 2100, 1):
            if str('MOVIE') in title_item:
                if title_item_year_int not in movie_years_dict:
                    movie_years_dict[title_item_year_int] = []
                movie_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in movie_decades_dict:
                    movie_decades_dict[title_item_decade_int] = []
                movie_decades_dict[title_item_decade_int].append(title_item)
            if str('TV') in title_item:
                if title_item_year_int not in tv_years_dict:
                    tv_years_dict[title_item_year_int] = []
                tv_years_dict[title_item_year_int].append(title_item)
                if title_item_decade_int not in tv_decades_amount_dict:
                    tv_decades_amount_dict[title_item_decade_int] = []
                tv_decades_amount_dict[title_item_decade_int].append(title_item)

    if terminal_graph_options_int == 1:
        for movie_year_values, value in sorted(movie_years_dict.items()):
            movie_year_totals_dict[movie_year_values] = len(value)
        movie_data = sorted(movie_year_totals_dict.items())
        movie_years_terminal_graph_list = []
        for key, value in movie_data:
            movie_years_terminal_graph_list.append((str(key), value))
        graph = Pyasciigraph()

        for line in graph.graph('MOVIES: YEAR AMOUNTS: ', movie_years_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 2:
        for tv_year_values, value in sorted(tv_years_dict.items()):
            tv_year_totals_dict[tv_year_values] = len(value)
        tv_data = sorted(tv_year_totals_dict.items())
        tv_years_terminal_graph_list = []
        for key, value in tv_data:
            tv_years_terminal_graph_list.append((str(key), value))
        graph = Pyasciigraph()

        for line in graph.graph('TV SHOWS: YEAR AMOUNTS: ', tv_years_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 3:
        for movie_year_values, value in sorted(movie_decades_dict.items()):
            movie_decades_totals_dict[movie_year_values] = len(value)
        movie_decades_terminal_graph_list = []
        for key, value in movie_decades_totals_dict.items():
            movie_decades_terminal_graph_list.append((str(key), value))
        graph = Pyasciigraph()

        for line in graph.graph('MOVIES: DECADE AMOUNTS: ', movie_decades_terminal_graph_list):
            print()
            print(line)
        separator()

    if terminal_graph_options_int == 4:
        for tv_year_values, value in sorted(tv_decades_amount_dict.items()):
            tv_decades_totals_dict[tv_year_values] = len(value)
        tv_decades_terminal_graph_list = []
        for key, value in tv_decades_totals_dict.items():
            tv_decades_terminal_graph_list.append((str(key), value))
        graph = Pyasciigraph()

        for line in graph.graph('TV SHOWS: DECADE AMOUNTS: ', tv_decades_terminal_graph_list):
            print()
            print(line)
        separator()


def terminal_graphs_options_sub_menu():
    print(pyfiglet.figlet_format('TERMINAL_GRAPHS', font='cybermedium'))
    separator()

    print('1) MOVIES (TITLES PER YEAR)                      2) TV SHOWS (TITLES PER YEAR)')
    print()
    print('3) MOVIES (TITLES PER DECADE)                    4) TV SHOWS (TITLES PER DECADE)')
    print()
    print('5) MOVIES (RESOLUTIONS PERCENTAGES)              6) TV SHOWS (RESOLUTIONS PERCENTAGES)')
    print()
    print('7) MOVIES (FILE-TYPE AMOUNTS)                    8) TV SHOWS (FILE-TYPE AMOUNTS)')
    print()
    print('0) MAIN MENU')
    separator()

    try:
        terminal_graph_options = input('ENTER #: ')
        separator()
        terminal_graph_options_int = int(terminal_graph_options)

        if terminal_graph_options_int == 1:
            terminal_graph_options_base(terminal_graph_options_int=1)
        elif terminal_graph_options_int == 2:
            terminal_graph_options_base(terminal_graph_options_int=2)
        elif terminal_graph_options_int == 3:
            terminal_graph_options_base(terminal_graph_options_int=3)
        elif terminal_graph_options_int == 4:
            terminal_graph_options_base(terminal_graph_options_int=4)
        elif terminal_graph_options_int == 5:
            terminal_graph_options_advanced(terminal_graph_options_int=5)
        elif terminal_graph_options_int == 6:
            terminal_graph_options_advanced(terminal_graph_options_int=6)
        elif terminal_graph_options_int == 7:
            search_file_type_totals(terminal_graph_options_int=7)
        elif terminal_graph_options_int == 8:
            search_file_type_totals(terminal_graph_options_int=8)
        elif terminal_graph_options_int == 0:
            media_index_home()
    except (TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('PLEASE RETRY YOUR SELECTION USING THE NUMBER KEYS')
        separator()


def tk_gui_file_browser_window():
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    root.destroy()
    return selected_directory


def tk_gui_file_selection_window():
    root = Tk()
    root.withdraw()
    root.update()
    selected_file = filedialog.askopenfilename()
    root.destroy()
    return selected_file


def tv_episodes_sort_function(sort_options_int):
    tv_results_list = list(csv.reader(open(os.path.expanduser(
        (media_index_folder + '/TV_INFORMATION_INDEX.csv').format(username_input)), encoding='UTF-8')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}

    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        tv_show_episodes_found.append(found_tv_title)
        tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)

    sorted_by_key_d = sorted(tv_show_found.items(), key=lambda kv: kv[0])
    sorted_by_key_a = sorted(tv_show_found.items(), key=lambda kv: kv[0], reverse=True)
    sorted_by_value_d = sorted(tv_show_found.items(), key=lambda kv: kv[1])
    sorted_by_value_a = sorted(tv_show_found.items(), key=lambda kv: kv[1], reverse=True)

    if sort_options_int == 5:
        for item in sorted_by_key_d:
            print()
            print(item)
        separator()
    if sort_options_int == 6:
        for item in sorted_by_key_a:
            print()
            print(item)
        separator()
    if sort_options_int == 7:
        for item in sorted_by_value_d:
            print()
            print(item)
        separator()
    if sort_options_int == 8:
        for item in sorted_by_value_a:
            print()
            print(item)
        separator()


def username_check_and_folder_creation():
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input

    try:
        user_info_file = os.path.expanduser((media_index_folder + '/{0}_USER_INFO.csv').format(username_input))

        if os.path.isfile(user_info_file):
            user_info_file_check = list(csv.reader(open(user_info_file)))
            movie_dir_input = user_info_file_check[1][1]
            tv_dir_input = user_info_file_check[2][1]
            movie_alt_dir_input = user_info_file_check[3][1]
            tv_alt_dir_input = user_info_file_check[4][1]
        else:
            os.makedirs(os.path.expanduser((media_index_folder + '/').format(username_input)), exist_ok=True)
            os.makedirs(os.path.expanduser((media_index_folder + '/FILES').format(username_input)), exist_ok=True)
            directory_selection()
    except (OSError, TypeError, ValueError) as e:
        print('INPUT ERROR: ', e)
        print()
        print('INVALID INPUT, PLEASE RETRY')
        separator()
        main()


def walk_directories_and_create_indices():
    movie_video_files_results = []

    if movie_dir_input is not str(''):
        for root, dirs, files in os.walk(movie_dir_input):
            for movie_file in sorted(files):
                if movie_file.lower().endswith(extensions):
                    movie_video_files_results.append([(pathlib.Path(root) / movie_file).as_posix()])
    if movie_alt_dir_input is not str(''):
        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(extensions):
                    movie_video_files_results.append([(pathlib.Path(root) / alt_file).as_posix()])

    with open(os.path.expanduser((media_index_folder + '/MOVIE_VIDEO_FILES_PATHS.csv').format(username_input)), 'w',
              encoding='UTF-8', newline='') as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_video_files_results):
            csv_writer.writerow(movie_row)

    tv_show_video_files_results = []

    if tv_dir_input is not str(''):
        for root, dirs, files in os.walk(tv_dir_input):
            for tv_file in sorted(files):
                if tv_file.lower().endswith(extensions):
                    tv_show_video_files_results.append([(pathlib.Path(root) / tv_file).as_posix()])
    if tv_alt_dir_input is not str(''):
        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.lower().endswith(extensions):
                    tv_show_video_files_results.append([(pathlib.Path(root) / alt_file).as_posix()])

    with open(os.path.expanduser((media_index_folder + '/TV_VIDEO_FILES_PATHS.csv').format(username_input)), 'w',
              encoding='UTF-8', newline='') as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_video_files_results):
            csv_writer.writerow(tv_row)


if __name__ == '__main__':
    main()
