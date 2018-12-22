import csv
import os
import re

movie_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")

movie_results = []

extensions = (
    ".3gp", ".avi", ".divx", ".img", ".iso,", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv", ".xvid",
    ".srt")


def search_movie_folders_items():
    for root, dirs, movie in movie_data:
        for extensions in movie:
            movie_results.append(movie)
            movie_year_info = re.findall("\((\d{4})\)", str(movie)),
            movie_res_info = re.findall("\((\d+x\d+)\)", str(movie)),
            movie_hsd_res_standard = re.findall("\((\wD)\)", str(movie)),
            movie_old_res_standard = re.findall("\((\d{3,}p)\)", str(movie)),
            movie_parts = re.findall("Part\s\d{1,2}", str(movie)),
            movie_file_type = re.findall("(?<=\.)([\w]{3,})", str(movie))
            movie_results.append(
                [movie, movie_year_info, movie_res_info, movie_hsd_res_standard, movie_old_res_standard,
                 movie_parts, movie_file_type])
            print(movie, movie_year_info[0], movie_res_info[0], movie_hsd_res_standard[0],
                  movie_old_res_standard[0], movie_parts[0], movie_file_type)


def create_media_index_csv():
    search_movie_folders_items()
    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results:
            csv_writer.writerow(movie_row)


create_media_index_csv()
