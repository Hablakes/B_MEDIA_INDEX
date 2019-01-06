import csv

import guessit
import pymediainfo

movie_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/NOTES/INDEX-TEST.csv"))
tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/NOTES/INDEX-TEST.csv"))

files_results = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/NOTES/FILES-RESULTS-TEST.csv'))
files_results_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/NOTES/FILES-RESULTS-TEST.csv')))


def get_tv_show_index_results():
    tv_index_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0], options={'type': 'episode', 'episode-prefer-number': True})

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video' and track not in files_results_list:
                tv_index_file_results.append(
                    [title.get('title'), title.get('episode_title'), title.get('season'), title.get('episode'),
                     title.get('year'), str(track.width) + 'x' + str(track.height), title.get('container')])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/NOTES/FILES-RESULTS-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


get_tv_show_index_results()
