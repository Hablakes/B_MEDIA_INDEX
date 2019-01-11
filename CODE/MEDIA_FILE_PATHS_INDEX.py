import csv
import os

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")



def search_folder_items_and_save_file_paths(username_input):
    movie_dir_input = [(input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):"))]
    tv_dir_input = [(input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):"))]
    movie_file_results = []
    for root, dirs, files in os.walk(movie_dir_input[0]):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    tv_show_file_results = []
    for root, dirs, files in os.walk(tv_dir_input[0]):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])

    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)
