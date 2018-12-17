import os

movie_txt_file = "C:/Users/botoole/Downloads/B/BTMP/BLAIR/MOVIES/CURRENT-MOVIES.txt"
tv_txt_file = "C:/Users/botoole/Downloads/B/BTMP/BLAIR/TV/CURRENT-TV.txt"
tv2_txt_file = "C:/Users/botoole/Downloads/B/BTMP/BLAIR/TV2/CURRENT-TV2.txt"


def create_movie_folders():
    for m_title in open(movie_txt_file, 'r'):
        os.makedirs('C:/Users/botoole/Downloads/B/BTMP/BLAIR/MOVIES/' + m_title.strip(), exist_ok=True)


def create_tv_folders():
    for tv_title in open(tv_txt_file, 'r'):
        os.makedirs('C:/Users/botoole/Downloads/B/BTMP/BLAIR/TV/' + tv_title.strip(), exist_ok=True)


def create_tv2_folders():
    for tv2_title in open(tv2_txt_file, 'r'):
        os.makedirs('C:/Users/botoole/Downloads/B/BTMP/BLAIR/TV2/' + tv2_title.strip(), exist_ok=True)


create_movie_folders()
create_tv_folders()
create_tv2_folders()
