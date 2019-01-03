import csv

import guessit

tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/INDEX-TEST.csv"))


def scrape_file_info_from_list():
    for tv_file in tv_index:
        title = guessit.guessit(tv_file[0], options={'type': 'episode'})

        print(title)


scrape_file_info_from_list()
