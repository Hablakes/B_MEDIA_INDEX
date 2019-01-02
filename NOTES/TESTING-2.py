import csv

import pymediainfo

tv_index = csv.reader(list(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX-TEST.csv")))
test = pymediainfo.MediaInfo.parse(
    r"/home/bx/Videos/TEST/Honest Trailers (2012)/Honest Trailers - 801 - Venom.mp4")


def scrape_file_info_from_list():
    tv_file_results = []
    tv_file_other_file_name = []
    tv_file_width = []
    tv_file_height = []
    tv_file_file_extension = []

    for track in test.tracks:
        tv_file_other_file_name.append(track.other_file_name)
        tv_file_width.append(track.width)
        tv_file_height.append(track.height)
        tv_file_file_extension.append(track.file_extension)

    tv_file_results.append(
        [tv_file_other_file_name[0], [tv_file_width[1], tv_file_height[1]], [tv_file_file_extension[0]]])
    print(tv_file_results[0])


scrape_file_info_from_list()
