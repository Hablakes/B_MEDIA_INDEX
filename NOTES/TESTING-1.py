import csv

import guessit
import pymediainfo


def movie_index_results():
    index = list(csv.reader(open(r'/home/bx/MEDIA-INDEX/ALT-FILES-INDEX.csv')))

    index_file_results = []

    for movie_file in index:

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1])

        title_to_year = guessit.guessit(movie_file[0].rsplit('/')[-2])

        mv_title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (mv_title_and_year[-5:-1])

        mv_title = (mv_title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:
            print(track.to_data())


movie_index_results()
