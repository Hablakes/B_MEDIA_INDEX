import csv
import os
import re

movie_data = r"C:/Users/botoole/Downloads/B/BTMP/TEST/MOVIES/"

movie_test = [
    "Movie with Super Long Unnecessary Title That Even Has Sp3c!al Characters and 0ther Non-Sense (1990) (1080p).avi",
    "Movie (HD).mp4",
    "Movie (HD) (1991).mp4",
    "Movie (1991) (SD).m4a",
    "Movie (720p).avi",
    "Movie.(1995).avi",
    "Movie (2010)",
    "Movie Test 0.divx",
    "Movie Test 1 (2000).avi",
    "Movie Test 2 (2001) (1920x1080) Part 1.mkv",
    "Movie Test 3 (2001) (1920x1080).mkv",
    "Movie Test 4 (2000) (640x480).avi",
    "Movie Test 5 (1990) (1024x768).avi",
    "Movie Test 6 (1996) (960x1600).mp4",
    "Movie Test 7 (1980) Part 2.xvid"]

results = []

titles = re.split("(?P<Titles>[^\(]+)[\s.]", movie_data)

titles_wsc = re.split("(?P<Titles_W_S_C>[^\s\-]+)", movie_data)

year = re.split("(\((?P<Year>\d{4})\))?", movie_data)

year_ar = re.split("(\s\((?P<Year_A_R>\d{4})\))?", movie_data)

resolution = re.split("(\((?P<Res_Standard>\d+x\d+)\))?", movie_data)

resolution_ay = re.split("(\s\((?P<Res_A_Y>\d+x\d+)\))?", movie_data)

old_res_standard = re.split("(\((?P<Old_Res_Standard>\d{3,}p)\))?", movie_data)

hd_sd_res_standard = re.split("(\((?P<HD_SD_Res>[A-Z]D)\))?", movie_data)

hd_sd_res_standard_as = re.split("(\s\((?P<HD_SD_Res_A_S>[A-Z]D)\))?", movie_data)

parts = re.split("(\s(?P<Parts>Part\s\d{1,2}))?", movie_data)

file_type = re.split("((?<=\.)(?P<FileType>[\w]{3,}))", movie_data)


def search_movie_folders_items():
    for movie in movie_test:
        for extension in [".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt",
                          ".webm", ".wmv", ".xvid", ".srt"]:
            if movie.endswith(extension):
                movie_year_info = re.match("(\((?P<Year>\d{4})\))", str(movie)),
                movie_res_info = re.match("(\((?P<Res_Standard>\d+x\d+)\))?", str(movie)),
                movie_hsd_res_standard = re.match("(\((?P<HD_SD_Res>[A-Z]D)\))?", str(movie)),
                movie_old_res_standard = re.match("(\((?P<Old_Res_Standard>\d{3,}p)\))?", str(movie)),
                movie_parts = re.match("(\s(?P<Parts>Part\s\d{1,2}))?", str(movie)),
                movie_file_type = re.match("((?<=\.)(?P<FileType>[\w]{3,}))", str(movie))
                results.append([movie, movie_year_info])

    print(results)


search_movie_folders_items()
