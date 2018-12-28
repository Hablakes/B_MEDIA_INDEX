import csv
import os


""" - WINDOWS (WORK MACHINE)

media_index = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))
media_index_list = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))

movie_files_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))
movie_files_index_list = list(
    csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv')))

movies_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")
tv_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/TV/")

movie_walk_data = os.walk(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")
tv_walk_data = os.walk(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/TV/")

"""

""" - LINUX (HOME MACHINES)

media_index = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))
media_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_files_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))
movie_files_index_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv')))

movies_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")

movie_walk_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")
tv_walk_data = os.walk(r"")

"""