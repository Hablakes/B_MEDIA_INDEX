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

    movie_index_file_results = {}

    for movie_file in sorted(movie_index):

        title_key = movie_file[0].rsplit('/')[-2]

        if movie_file[0].lower().endswith(extensions):

            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

            test = pymediainfo.MediaInfo.parse(movie_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':

                    if title_key not in movie_index_file_results:
                        movie_index_file_results[title_key] = []
                    movie_index_file_results[str(title_key)].append(
                        [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                         title.get('container')])

        elif movie_file[0].lower().endswith(nfo_extensions):
            if title_key not in movie_index_file_results:
                movie_index_file_results[title_key] = []
            with open(movie_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        movie_index_file_results[str(title_key)].insert(1, [line.split('.')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results.items():
            csv_writer.writerow(movie_row)


def tv_index_all_results(username_input):
    tv_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv'))

    tv_index_file_results = {}

    for tv_file in sorted(tv_index):

        title_key = tv_file[0].rsplit('/')[-2]

        if tv_file[0].lower().endswith(extensions):

            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

            title_and_year = (tv_file[0].rsplit('/')[-2])

            test = pymediainfo.MediaInfo.parse(tv_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':

                    if title_key not in tv_index_file_results:
                        tv_index_file_results[title_key] = []
                        tv_index_file_results[title_key].append(
                        [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                         title.get('episode'), title.get('year'), str(track.width) + 'x' + str(track.height),
                         title.get('container')])

        elif tv_file[0].lower().endswith(nfo_extensions):
            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = []
            with open(tv_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        tv_index_file_results[title_key].insert(1, [line.split('.')])

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results.items():
            csv_writer.writerow(tv_row)


movie_index_all_results(username_input='bx')
#tv_index_all_results(username_input='bx')
