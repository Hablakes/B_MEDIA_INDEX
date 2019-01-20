import csv
import os

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

nfo_extensions = ".nfo"
srt_extensions = ".srt"


def search_folder_items_and_save_file_paths(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                            tv_alt_dir_input):
    movie_file_results = []
    m_nfo_file_results = []
    m_srt_file_results = []
    for root, dirs, files in os.walk(movie_dir_input):
        for movie_file in sorted(files):
            if movie_file.endswith(extensions):
                movie_file_results.append([root + '/' + movie_file])
            elif movie_file.endswith(nfo_extensions):
                m_nfo_file_results.append([root + '/' + movie_file])
            elif movie_file.endswith(srt_extensions):
                m_srt_file_results.append([root + '/' + movie_file])

    if movie_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(movie_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(extensions):
                    movie_file_results.append([root + '/' + alt_file])
                elif alt_file.endswith(nfo_extensions):
                    m_nfo_file_results.append([root + '/' + alt_file])
                elif alt_file.endswith(srt_extensions):
                    m_srt_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)
        for movie_row in sorted(m_nfo_file_results):
            csv_writer.writerow(movie_row)
        for movie_row in sorted(m_srt_file_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(movie_file_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(m_nfo_file_results):
            csv_writer.writerow(movie_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-SRT-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in sorted(m_srt_file_results):
            csv_writer.writerow(movie_row)

    tv_show_file_results = []
    t_nfo_file_results = []
    t_srt_file_results = []
    for root, dirs, files in os.walk(tv_dir_input):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_show_file_results.append([root + '/' + tv_file])
            elif tv_file.endswith(nfo_extensions):
                t_nfo_file_results.append([root + '/' + tv_file])
            elif tv_file.endswith(srt_extensions):
                t_srt_file_results.append([root + '/' + tv_file])

    if tv_alt_dir_input is not str(''):

        for root, dirs, files in os.walk(tv_alt_dir_input):
            for alt_file in sorted(files):
                if alt_file.endswith(extensions):
                    tv_show_file_results.append([root + '/' + alt_file])
                elif alt_file.endswith(nfo_extensions):
                    t_nfo_file_results.append([root + '/' + alt_file])
                elif alt_file.endswith(srt_extensions):
                    t_srt_file_results.append([root + '/' + alt_file])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)
        for tv_row in sorted(t_nfo_file_results):
            csv_writer.writerow(tv_row)
        for tv_row in sorted(t_srt_file_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_show_file_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-NFO-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(t_nfo_file_results):
            csv_writer.writerow(tv_row)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-SRT-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(t_srt_file_results):
            csv_writer.writerow(tv_row)
