import csv
import os


def movie_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")


def tv_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")


def tv2_listdir():
    return os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")


found = []

for movie in movie_listdir():
    movie_title = movie.strip()[0:-7]
    movie_year = movie.strip()[-5:-1]
    found.append(["MOVIE", movie_title, movie_year])

for tv in tv_listdir():
    tv_title = tv.strip()[0:-7]
    tv_year = tv.strip()[-5:-1]
    found.append(["TV", tv_title, tv_year])

for tv2 in tv2_listdir():
    tv2_title = tv2.strip()[0:-7]
    tv2_year = tv2.strip()[-5:-1]
    found.append(["TV", tv2_title, tv2_year])

found = sorted(found)

with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    for row in found:
        csv_writer.writerow(row)
