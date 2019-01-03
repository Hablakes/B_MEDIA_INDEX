import csv

import pymediainfo

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    tv_file_results = []

    for tv_file in tv_index:

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:
            tv_file_results.append([track.other_file_name, [track.width, track.height], [track.file_extension]])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


scrape_file_info_from_list()
