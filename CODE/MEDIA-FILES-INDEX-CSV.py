import csv
import os

movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"
tv_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"
alt_dirs = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"

movie_file_results = []
tv_show_file_results = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


def search_movie_folders_items():
    for root, dirs, files in os.walk(movie_dir):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)


def search_tv_show_folders_items():
    for root, dirs, files in os.walk(tv_dir):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    for root, dirs, files in os.walk(alt_dirs):
        for alt_file in sorted(files):
            if alt_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + alt_file])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)


# search_movie_folders_items()
search_tv_show_folders_items()
