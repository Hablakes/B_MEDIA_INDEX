import csv
import os


def create_movie_folders(username_input):
    media_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    for m_title in media_index_list:
        if str("MOVIE") in m_title:
            os.makedirs('/home/bx/Videos/CHASE/MOVIES/' + m_title[1] + " (" + m_title[2] + ")", exist_ok=True)


def create_tv_folders(username_input):
    media_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
    media_index_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
    for tv_title in media_index_list:
        if str("TV") in tv_title:
            os.makedirs('/home/bx/Videos/CHASE/TV/' + tv_title[1] + " (" + tv_title[2] + ")", exist_ok=True)


create_movie_folders(username_input='bx')
create_tv_folders(username_input='bx')
