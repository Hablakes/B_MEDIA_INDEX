import csv
import os
import re

movie_data = r"C:/Users/botoole/Downloads/B/BTMP/TEST/MOVIES/"

movie_test = [
    "Movie 0 with Super Long Unnecessary Title That Even Has Sp3c!al Characters and 0ther Non-Sense (1990) (1080p).3gp",
    "Movie 1 (HD).mp4",
    "Movie 2 (HD) (1991).webm",
    "Movie 3 (1991) (SD).m4a",
    "Movie 4 (720p).avi",
    "Movie.5 (1995).wmv",
    "Movie 6 (2010).mpeg",
    "Movie Test 0.divx",
    "Movie Test 1 (2000).img",
    "Movie Test 2 (2001) (1920x1080) Part 1.mkv",
    "Movie Test 3 (2001) (1920x1080).mov",
    "Movie Test 4 (2000) (640x480).iso",
    "Movie Test 5 (1990) (1024x768).m4v",
    "Movie Test 6 (1996) (960x1600).mp4",
    "Movie Test 7 (1980) Part 2.xvid",
    "Movie 8 (1986).qt",
    "Movie 8 (1986).srt"]

movie_results = []


def search_movie_folders_items():
    for movie in movie_test:
        for extension in [".3gp", ".avi", ".divx", ".img", ".iso", ".m4a", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg",
                          ".qt", ".webm", ".wmv", ".xvid", ".srt"]:
            if movie.endswith(extension):
                movie_year_info = re.findall("\((\d{4})\)", movie),
                movie_res_info = re.findall("\((\d+x\d+)\)", movie),
                movie_hsd_res_standard = re.findall("\((\wD)\)", movie),
                movie_old_res_standard = re.findall("\((\d{3,}p)\)", movie),
                movie_parts = re.findall("Part\s\d{1,2}", movie),
                movie_file_type = re.findall("(?<=\.)([\w]{3,})", movie)
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
