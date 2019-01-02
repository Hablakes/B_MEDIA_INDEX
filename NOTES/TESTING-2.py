import csv

import pymediainfo

tv_index = csv.reader(list(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX-TEST.csv")))
test = pymediainfo.MediaInfo.parse(
    r"/home/bx/Videos/TEST/Honest Trailers (2012)/Honest Trailers - 801 - Venom.mp4")


def scrape_file_info_from_list():
    tv_file_results = []
    tv_file_other_file_name = []
    tv_file_file_extension = []
    tv_file_width = []
    tv_file_height = []

    for track in test.tracks:
        track.to_data()


scrape_file_info_from_list()
