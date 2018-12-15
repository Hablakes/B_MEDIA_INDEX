import csv
import re

media = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/CURRENT-INDEX.csv"))


def get_media_years():
    for title in media:
        media_year_split = re.split("([0-9][0-9][0-9][0-9])", str(title))
        media_year = media_year_split[1]
        print(media_year)


get_media_years()

