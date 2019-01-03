import csv

import pymediainfo

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    tv_file_results = []
    tv_file_other_file_name = []
    tv_file_width = []
    tv_file_height = []
    tv_file_file_extension = []

    for tv_file in tv_index:

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:
            tv_file_other_file_name.append(track.other_file_name)
            tv_file_width.append(track.width)
            tv_file_height.append(track.height)
            tv_file_file_extension.append(track.file_extension)

    tv_file_results.append(
        [tv_file_other_file_name[0], [tv_file_width[1], tv_file_height[1]], [tv_file_file_extension[0]]])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


scrape_file_info_from_list()
