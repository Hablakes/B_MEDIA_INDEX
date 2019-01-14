import csv
import os

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


def rename_existing_movie_and_tv_indices_for_update_search(username_input='bx'):
    for index_file in os.listdir(r'/home/' + username_input + '/MEDIA-INDEX/'):
        if index_file.startswith('MOVIE-FILES-I'):
            os.rename(r'/home/' + username_input + '/MEDIA-INDEX/' + index_file,
                      r'/home/' + username_input + '/MEDIA-INDEX/' + 'OLD-' + index_file)
        if index_file.startswith('TV-FILES-I'):
            os.rename(r'/home/' + username_input + '/MEDIA-INDEX/' + index_file,
                      r'/home/' + username_input + '/MEDIA-INDEX/' + 'OLD-' + index_file)


def update_search_folder_items_and_save_file_paths():
    movie_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"
    tv_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"
    alt_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"
    movie_file_results = []
    tv_show_file_results = []

    for root, dirs, files in os.walk(movie_dir):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    with open(r"/home/bx/MEDIA-INDEX/MOVIE-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    for root, dirs, files in os.walk(tv_dir):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    for root, dirs, files in os.walk(alt_dir):
        for alt_file in sorted(files):
            if alt_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + alt_file])

    with open(r"/home/bx/MEDIA-INDEX/TV-FILES-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)


def compare_old_and_updated_indices_and_create_differences_files(username_input):
    rename_existing_movie_and_tv_indices_for_update_search(username_input='bx')
    update_search_folder_items_and_save_file_paths()

    with open(r'/home/' + username_input + '/MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv', 'r') as mi_0, open(
              r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'r') as mi_1:
        old_movie_index = mi_0.readlines()
        new_movie_index = mi_1.readlines()

    with open(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv','w') as outFile:
        for line in new_movie_index:
            if line not in old_movie_index:
                outFile.write(line)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/OLD-TV-FILES-INDEX.csv', 'r') as ti_0, open(
            r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv', 'r') as ti_1:
        old_tv_index = ti_0.readlines()
        new_tv_index = ti_1.readlines()

    with open(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv', 'w') as outFile:
        for line in new_tv_index:
            if line not in old_tv_index:
                outFile.write(line)


compare_old_and_updated_indices_and_create_differences_files(username_input='bx')
