import os
import re

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"

movie_file_results_dict = {}


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie in files:
            for extension in [".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt",
                              ".webm", ".wmv", ".xvid", ".srt"]:
                if movie.endswith(extension):
                    movie_file_info = re.search("(.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)", str(movie), flags=0)
                    print(movie_file_info)


search_movie_folders_items()
