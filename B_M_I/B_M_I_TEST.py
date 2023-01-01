import csv
import json
import os
import pathlib
import re
import textwrap
import time

import guessit
import pyfiglet
import pymediainfo

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from datetime import datetime
from difflib import SequenceMatcher
from tkinter import filedialog, Tk

date_string = str(datetime.today().strftime('%Y_%m_%d'))

extensions = ('.3gp', '.asf', '.asx', '.avc', '.avi', '.bdmv', '.bin', '.bivx', '.dat', '.disc', '.divx', '.dv',
              '.dvr-ms', '.evo', '.fli', '.flv', '.h264', '.img', '.iso', '.m2ts', '.m2v', '.m4v', '.mkv', '.mov',
              '.mp4', '.mpeg', '.mpg', '.mt2s', '.mts', '.nfo', '.nrg', '.nsv', '.nuv', '.ogm', '.pva', '.qt', '.rm',
              '.rmvb', '.strm', '.svq3', '.ts', '.ty', '.viv', '.vob', '.vp3', '.wmv', '.xvid', '.webm')

username = "BXB"
user_info = '{0}_USER_INFO.json'

index_folder = '~/{0}_MEDIA_INDEX/'
files_folder = '~/{0}_MEDIA_INDEX/FILES/'
results_folder = '~/{0}_MEDIA_INDEX/RESULTS/'

movies_comparison = 'MOVIE_COMPARISON_INDEX.csv'
tv_comparison = 'TV_COMPARISON_INDEX.csv'

titles_index = 'MEDIA_TITLE_INDEX.csv'

movie_plots_index = 'MOVIE_PLOTS_INDEX.csv'
tv_episode_plots_index = 'TV_EPISODE_PLOTS_INDEX.csv'
tv_show_plots_index = 'TV_SHOW_PLOTS_INDEX.csv'

new_user_movies_dirs = 'FILES/NEW_MOVIE_VIDEO_FILES_PATHS.csv'
new_user_tv_dirs = 'FILES/NEW_TV_VIDEO_FILES_PATHS.csv'
new_user_movies_index = 'FILES/NEW_MOVIE_INFORMATION_INDEX.csv'
new_user_tv_index = 'FILES/NEW_TV_INFORMATION_INDEX.csv'

user_movies_dirs = 'MOVIE_VIDEO_FILES_PATHS.csv'
user_tv_dirs = 'TV_VIDEO_FILES_PATHS.csv'
user_movies_index = 'MOVIE_INFORMATION_INDEX.csv'
user_tv_index = 'TV_INFORMATION_INDEX.csv'

search_term_1 = "space"
search_term_2 = "hacker"

plots_list = []
multiple_search_terms_list = []

with open(os.path.expanduser(
        (index_folder + movie_plots_index).format(username)), encoding='UTF-8') as m_p_i:
    movie_files_results_list = list(csv.reader(m_p_i))
with open(os.path.expanduser(
        (index_folder + tv_episode_plots_index).format(username)), encoding='UTF-8') as t_e_p:
    tv_episodes_results_list = list(csv.reader(t_e_p))
with open(os.path.expanduser(
        (index_folder + tv_show_plots_index).format(username)), encoding='UTF-8') as t_s_p:
    tv_show_plots_list = list(csv.reader(t_s_p))

    for plot in movie_files_results_list:
        plots_list.append('MOVIE' + ' - ' + plot[0] + ' - ' + plot[1])

    for plot in tv_show_plots_list:
        plots_list.append('TV SHOW' + ' - ' + plot[0] + ' - ' + plot[1])

    for items in plots_list:
        if search_term_1.lower() in items.lower():
            multiple_search_terms_list.append(items)

    for items in multiple_search_terms_list:
        if search_term_2.lower() in items.lower():
            p1 = ''.join(items.split('<plot>'))
            p2 = ''.join(p1.split('</plot>'))
            print('\n', textwrap.fill(p2, 100))
