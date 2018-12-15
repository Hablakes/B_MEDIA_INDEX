import os

movie_dir = r"C:\Users\botoole\Downloads\B\BTMP\TEST\MOVIES"


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie in files:
            for extension in [".avi", ".divx", ".img", ".iso," ".m4v", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
                              ".xvid"]:

                if movie.endswith(extension):
                    print(os.path.join(movie_dir, movie))


search_movie_folders_items()
