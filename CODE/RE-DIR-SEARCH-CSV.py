import csv
import os
import re

movie_data = os.walk(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")

movie_walk = []
movie_results = []


def search_movie_folders_items():
    for root, dirs, movie in sorted(movie_data):
        for found_movie_file in movie:
            if found_movie_file.endswith(("3gp", "avi", "divx", "img", "iso", "m4a", "m4v", "mkv", "mov", "mp4",
                                          "mpeg", "qt", "webm", "wmv", "xvid")):
                movie_walk.append([found_movie_file])
    for movie_match in movie_walk:
        movie_year_info = re.findall("\((\d{4})\)", str(movie_match)),
        movie_res_info = re.findall("\((\d+x\d+)\)", str(movie_match)),
        movie_hsd_res_standard = re.findall("\((\wD)\)", str(movie_match)),
        movie_old_res_standard = re.findall("\((\d{3,}p)\)", str(movie_match)),
        movie_parts = re.findall("Part\s\d{1,2}", str(movie_match)),
        movie_file_type = re.finditer(
            "(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)|(\.qt)|"
            "(\.webm)|(\.wmv)|(\.xvid)", str(movie_match))
        for found_movie_match in movie_file_type:
            movie_results.append(
                [movie_match, movie_year_info[0], movie_res_info[0], movie_hsd_res_standard[0],
                 movie_old_res_standard[0], movie_parts[0], [found_movie_match[0]]])


def create_media_index_csv():
    search_movie_folders_items()
    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results:
            csv_writer.writerow(movie_row)


create_media_index_csv()
