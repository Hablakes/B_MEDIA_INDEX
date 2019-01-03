import csv

import pymediainfo

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    tv_file_results = []

    for tv_file in tv_index:

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:
            print(track.to_data())

scrape_file_info_from_list()
