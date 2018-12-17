import csv
import re

media = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv"))


def get_media_section():
    for section in media:
        section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(section[0]), flags=0)
        print(section_info)


def get_media_title():
    for title in media:
        title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(title[1]), flags=0)
        print(title_info)


def get_media_year():
    for year in media:
        year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(year[2]), flags=0)
        print(year_info)

# get_media_section()
# get_media_title()
# get_media_year()
