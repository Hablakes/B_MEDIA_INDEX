import csv
import os
import re

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"
tv_dir = (r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/",
          r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/")

movie_file_results = []
tv_file_results = []

extensions = (".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
              ".xvid", ".srt")


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie_file in files:
            if movie_file.endswith(extensions):
                movie_file_info = re.split("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", movie_file, flags=0)
                movie_file_results.append(["MOVIE", movie_file_info])


def create_media_files_index():
    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_file_results:
            csv_writer.writerow(movie_row)


search_movie_folders_items()
create_media_files_index()
