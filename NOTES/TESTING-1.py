import csv

import pymediainfo

import guessit

print(guessit.guessit("Treme.1x03.Right.Place,.Wrong.Time.HDTV.XviD-NoTV.avi"))

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    for tv_file in tv_index:
        test = pymediainfo.MediaInfo.parse(tv_file[0])
        for track in test.tracks:
            print(track.to_data())


scrape_file_info_from_list()
