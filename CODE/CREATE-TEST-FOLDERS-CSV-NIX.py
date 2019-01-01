import csv
import os

media_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))


def create_movie_folders():
    for m_title in media_index_list:
        if str("MOVIE") in m_title:
            os.makedirs('/home/bx/Videos/CHASE/MOVIES/' + m_title[1] + " (" + m_title[2] + ")", exist_ok=True)


def create_tv_folders():
    for tv_title in media_index_list:
        if str("TV") in tv_title:
            os.makedirs('/home/bx/Videos/CHASE/TV/' + tv_title[1] + " (" + tv_title[2] + ")", exist_ok=True)
            

create_movie_folders()
create_tv_folders()
