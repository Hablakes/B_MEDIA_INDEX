import csv
import itertools
import os

import guessit
import pymediainfo


all_extens = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm", ".nfo", ".srt")

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

nfo_extensions = ".nfo"
srt_extensions = ".srt"


def movie_index_all_results(username_input):
    movie_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-INDEX.csv'))

    movie_nfo_results = []

    for items in sorted(movie_index):
        if items[0].endswith(nfo_extensions):
            with open(items[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        movie_nfo_results.append([items[0].rsplit('/')[-2], line.split('.')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-PLOTS-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_nfo_results):
            csv_writer.writerow(movie_row)


def tv_index_all_results(username_input):
    tv_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv'))

    tv_nfo_results = []

    for items in sorted(tv_index):
        if items[0].endswith(nfo_extensions):
            with open(items[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        tv_nfo_results.append([items[0].rsplit('/')[-2], line.split('.')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-PLOTS-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_nfo_results):
            csv_writer.writerow(tv_row)




"""
    group_results = itertools.groupby(groups)

    for item, groups in group_results:
        print(item, list(groups))
"""

movie_index_all_results(username_input='bx')
tv_index_all_results(username_input='bx')
