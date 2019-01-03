import csv

import guessit

import pymediainfo

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    tv_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0], options={'type': 'episode'})

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:
            if track.track_type == 'Video':
                tv_file_results.append(
                    [title['title'], title['episode_title'], title['season'], title['episode'],
                     str(track.width) + 'x' + str(track.height), title['year'], title['container']])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


scrape_file_info_from_list()
