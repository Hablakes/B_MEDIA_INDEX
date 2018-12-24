import csv
import os
import re

movie_data = os.walk(r"/home/bx/Videos/CHASE/TEST/")

movie_walk = []
movie_results = []


def search_movie_folders_items():
    for root, dirs, movie in movie_data:
        re_ext = re.search(
            "(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)|(\.qt)|"
            "(\.webm)|(\.wmv)|(\.xvid)", str(movie))
        print(movie, re_ext)


search_movie_folders_items()

