import csv

import guessit
import pymediainfo


def movie_index_results():
    index = list(csv.reader(open(r'/home/bx/MEDIA-INDEX/ALT-FILES-INDEX.csv')))

    index_file_results = []

    for movie_file in index:

        print(movie_file[0])

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1])

        title_to_year = guessit.guessit(movie_file[0].rsplit('/')[-2])

        mv_title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (mv_title_and_year[-5:-1])

        mv_title = (mv_title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

        with open(r'/home/bx/MEDIA-INDEX/ALT-FILES-RESULTS.csv', "w", newline="") as f:
            csv_writer = csv.writer(f)
            for row in index_file_results:
                csv_writer.writerow(row)


movie_index_results()

