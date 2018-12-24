import csv
import os
import re

movie_data = os.walk(r"/home/bx/Videos/CHASE/TEST/")

movie_walk = []
movie_results = []


def search_movie_folders_items():
    for root, dirs, movie in movie_data:
        re_ext = re.findall(
            "(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)|(\.qt)|"
            "(\.webm)|(\.wmv)|(\.xvid)", str(movie))
        for found_movie_file in re_ext:
            found_movie_file_format = re.search(
                "(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)|(\.qt)|"
                "(\.webm)|(\.wmv)|(\.xvid)", str(found_movie_file))

            print([movie, [found_movie_file_format[0]]])


search_movie_folders_items()

"""
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
"""