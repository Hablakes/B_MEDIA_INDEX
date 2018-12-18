import csv
import re

media_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_string = str("MOVIE")
tv_string = str("TV")

found_info = []


def scrape_movie_info_for_csv():
    for movie_found in media_index_list:
        if movie_string in movie_found[0]:
            movie_scrape_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[0]),
                                                 flags=0)
            movie_scrape_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[1]),
                                               flags=0)
            movie_scrape_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[2]),
                                              flags=0)
            found_info.append([movie_scrape_section_info[0], movie_scrape_title_info[0], movie_scrape_year_info[0]])


def scrape_tv_info_for_csv():
    for tv_found in media_index_list:
        if movie_string in tv_found[0]:
            tv_scrape_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[0]),
                                              flags=0)
            tv_scrape_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[1]),
                                            flags=0)
            tv_scrape_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[2]),
                                           flags=0)
            found_info.append([tv_scrape_section_info[0], tv_scrape_title_info[0], tv_scrape_year_info[0]])


found_info_sorted = sorted(found_info)

with open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    for row in found_info_sorted:
        csv_writer.writerow(row)

