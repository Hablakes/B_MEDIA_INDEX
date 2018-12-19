import os

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"

movie_file_results = []


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie in files:
            for extension in [".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm",
                              ".wmv", ".xvid"]:

                if movie.endswith(extension):
                    movie_file_results.append(os.path.join(movie))
"""
                    print(os.path.join(movie_dir, movie))
"""


search_movie_folders_items()

print(sorted(movie_file_results))
