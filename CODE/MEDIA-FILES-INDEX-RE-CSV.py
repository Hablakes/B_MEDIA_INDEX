import csv
import os
import re

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"
tv_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"
alt_dirs = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"

movie_file_results = []
tv_file_results = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
                     ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv",
                     ".mov", ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt",
                     ".rm", ".rmvb", ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid",
                     ".webm")


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie_file in files:
            if movie_file.endswith(extensions):
                movie_file_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", movie_file, flags=0)
                movie_file_results.append(["MOVIE", movie_file_info])


def search_tv_folders_items():
    for root, dirs, files in os.walk(tv_dir):
        for tv_file in files:
            if tv_file.endswith(extensions):
                tv_file_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", tv_file, flags=0)
                tv_file_results.append(["TV", tv_file_info])

    for root, dirs, files in os.walk(alt_dirs):
        for tv_file in files:
            if tv_file.endswith(extensions):
                alt_file_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", tv_file, flags=0)
                tv_file_results.append(["TV", alt_file_info])


def create_media_files_index():
    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-RE.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_file_results:
            csv_writer.writerow(movie_row)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


search_movie_folders_items()
search_tv_folders_items()
create_media_files_index()
