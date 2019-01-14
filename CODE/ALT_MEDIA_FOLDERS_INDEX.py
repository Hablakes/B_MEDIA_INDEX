import csv
import os
import re

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


def scrape_media_info_for_csv():
    movie_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/")
    tv_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/")
    alt_dir_list = os.listdir(r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")
    found_file_info = []

    for movie_found in movie_dir_list:
        movie_scrape_info = re.search("(.+) \((\d{4})\)", str(movie_found), flags=0)
        found_file_info.append(["MOVIE", movie_scrape_info[1], movie_scrape_info[2]])

    for tv_found in tv_dir_list:
        tv_scrape_info = re.search("(.+) \((\d{4})\)", str(tv_found), flags=0)
        found_file_info.append(["TV", tv_scrape_info[1], tv_scrape_info[2]])

    for alt_found in alt_dir_list:
        alt_scrape_info = re.search("(.+) \((\d{4})\)", str(alt_found), flags=0)
        found_file_info.append(["TV", alt_scrape_info[1], alt_scrape_info[2]])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in sorted(found_file_info):
            csv_writer.writerow(file_row)
