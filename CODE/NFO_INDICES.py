import csv
import os

extensions = (".nfo")


def search_folder_nfos_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                           tv_alt_dir_input):
    movie_file_results = []
    for root, dirs, files in os.walk(movie_dir_input):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for movie_file in sorted(files):
                if movie_file.endswith(extensions):
                    movie_file_results.append([root + '/' + movie_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    tv_show_file_results = []
    for root, dirs, files in os.walk(tv_dir_input):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(extensions):
                    tv_show_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-NFO-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)
