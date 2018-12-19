import csv
import os
import re

media_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movies_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")
tv_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/TV/")

movie_string = str("MOVIE")
tv_string = str("TV")

found_movie_info = []
found_tv_info = []

found_movie_info_sorted = sorted(found_movie_info)
found_tv_info_sorted = sorted(found_tv_info)


def scrape_movie_info_for_csv():
    for movie_found in movies_dir:
        movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
        scraped_movie_title = movie_scrape_info[1]
        scraped_movie_year = movie_scrape_info[2]
        #       print(movie_scrape_info[1], movie_scrape_info[2])
        found_movie_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])


def scrape_tv_info_for_csv():
    for tv_found in tv_dir:
        tv_scrape_info = re.search("(.+) \((\d{4})\)", str(tv_found), flags=0)
        scraped_movie_title = tv_scrape_info[1]
        scraped_movie_year = tv_scrape_info[2]
        #       print(tv_scrape_info[1], tv_scrape_info[2])
        found_movie_info.append(["TV", tv_scrape_info[1], tv_scrape_info[2]])


def create_media_index_csv():
    scrape_movie_info_for_csv()
    scrape_tv_info_for_csv()
    with open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in found_movie_info:
            csv_writer.writerow(movie_row)
        for tv_row in found_tv_info:
            csv_writer.writerow(tv_row)


create_media_index_csv()
