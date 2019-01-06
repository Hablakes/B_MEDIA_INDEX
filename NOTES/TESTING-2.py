import csv

import guessit
import pymediainfo

movie_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv"))
tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv"))

movie_files_results_list = list(
    csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-RESULTS.csv')))

tv_files_results_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS.csv')))


print(sorted(movie_files_results_list))