import csv
import os
import re

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


def scrape_media_info_for_csv(username_input, movie_dir_input, movie_alt_dir_input, tv_dir_input, tv_alt_dir_input):
    found_file_info = []

    for movie_found in os.listdir(movie_dir_input):
        movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
        found_file_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])

    if movie_alt_dir_input is not str(''):

        for movie_found in os.listdir(movie_alt_dir_input):
            movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
            found_file_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])

    for tv_found in os.listdir(tv_dir_input):
        tv_scrape_info = re.search("(.+) \((\d{4})\)", str(tv_found), flags=0)
        found_file_info.append(["TV", tv_scrape_info[1], tv_scrape_info[2]])

    if tv_alt_dir_input is not str(''):

        for alt_found in os.listdir(tv_alt_dir_input):
            alt_scrape_info = re.search("(.+) \((\d{4})\)", str(alt_found), flags=0)
            found_file_info.append(["TV", alt_scrape_info[1], alt_scrape_info[2]])

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in sorted(found_file_info):
            csv_writer.writerow(file_row)
