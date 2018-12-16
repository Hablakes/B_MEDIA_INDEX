import csv
import re

media = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv"))


def get_media_years():
    for info in media:
        media_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(info))
        print(media_info[0])


get_media_years()

