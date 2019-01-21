import csv

import guessit
import pymediainfo

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

nfo_extensions = ".nfo"
srt_extensions = ".srt"


def movie_index_all_results(username_input):
    movie_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-INDEX.csv'))

    movie_index_file_results = []
    movie_nfo_results = []
    movie_srt_results = []

    for movie_file in sorted(movie_index):

        if movie_file[0].endswith(extensions):

            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

            test = pymediainfo.MediaInfo.parse(movie_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':
                    movie_index_file_results.append(
                        [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                         title.get('container')])

        elif movie_file[0].endswith(nfo_extensions):
            with open(movie_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        movie_nfo_results.append([movie_file[0].rsplit('/')[-2], '', '', '', '', '', '', '', '', '',
                                                  line.split('.')])

        elif movie_file[0].endswith(srt_extensions):
            movie_srt_results.append([movie_file[0].rsplit('/')[-2], '', '', '', '', '', '', '', '', "SRT AVAILABLE"])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)
        for movie_row in movie_nfo_results:
            csv_writer.writerow(movie_row)
        for movie_row in movie_srt_results:
            csv_writer.writerow(movie_row)


def tv_index_all_results(username_input):
    tv_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv'))

    tv_index_file_results = []
    tv_nfo_results = []
    tv_srt_results = []

    for tv_file in sorted(tv_index):

        if tv_file[0].endswith(extensions):

            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

            title_and_year = (tv_file[0].rsplit('/')[-2])

            test = pymediainfo.MediaInfo.parse(tv_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':
                    tv_index_file_results.append(
                        [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                         title.get('episode'), title.get('year'), str(track.width) + 'x' + str(track.height),
                         title.get('container')])

        elif tv_file[0].endswith(nfo_extensions):
            with open(tv_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        tv_nfo_results.append([tv_file[0].rsplit('/')[-2], '', '', '', '', '', '', '', '', '',
                                                  line.split('.')])

        elif tv_file[0].endswith(srt_extensions):
            tv_srt_results.append([tv_file[0].rsplit('/')[-2], '', '', '', '', '', '', '', '', "SRT AVAILABLE"])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in sorted(tv_index_file_results):
            csv_writer.writerow(tv_row)
        for tv_row in sorted(tv_nfo_results):
            csv_writer.writerow(tv_row)
        for tv_row in sorted(tv_srt_results):
            csv_writer.writerow(tv_row)


movie_index_all_results(username_input='bx')
#tv_index_all_results(username_input='bx')
