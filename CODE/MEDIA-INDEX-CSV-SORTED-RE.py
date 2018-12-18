import csv
import re

media_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv'))
media_index_list = list(csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))

movie_string = str("MOVIE")
tv_string = str("TV")

found_info = []


def scrape_movie_info_for_csv():
    for movie_found in media_index_list:
        if movie_string in movie_found:
            movie_scrape_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[0]),
                                                 flags=0)
            movie_scrape_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[1]),
                                               flags=0)
            movie_scrape_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie_found[2]),
                                              flags=0)


found_info_sorted = sorted(found_info)

scrape_movie_info_for_csv()

print(found_info_sorted)

"""
def scrape_tv_info_for_csv():
    for tv_found in media_index_list:
        if movie_string in tv_found:
            tv_scrape_section_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[0]),
                                              flags=0)
            tv_scrape_title_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[1]),
                                            flags=0)
            tv_scrape_year_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(tv_found[2]),
                                           flags=0)
            for line_found_t in tv_found:
                found_info.append([tv_scrape_section_info, tv_scrape_title_info, tv_scrape_year_info])
                
                
def create_media_index_csv():
    with open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for row in found_info_sorted:
            csv_writer.writerow(row)


create_media_index_csv()
"""
