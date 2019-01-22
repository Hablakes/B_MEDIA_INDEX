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

        if title_key not in movie_index_file_results:
            movie_index_file_results[title_key] = {}

        if movie_file[0].lower().endswith(extensions):

            title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

            test = pymediainfo.MediaInfo.parse(movie_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':
                    movie_index_file_results[title_key]["DIRECTORY"] = title_key
                    movie_index_file_results[title_key]["TITLE"] = title.get('title')
                    movie_index_file_results[title_key]["YEAR"] = title.get('year')
                    movie_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    movie_index_file_results[title_key]["FILE TYPE"] = title.get('container')

        elif movie_file[0].lower().endswith(nfo_extensions):
            with open(movie_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        movie_index_file_results[title_key]["PLOT"] = line

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.DictWriter(f, ["DIRECTORY", "TITLE", "YEAR", "RESOLUTION", "FILE TYPE", "PLOT"])
        for movie_row in movie_index_file_results.values():
            csv_writer.writerow(movie_row)


def tv_index_all_results(username_input):
    tv_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-INDEX.csv'))

    tv_file_results = []

    for tv_file in sorted(tv_index):

        title_key = tv_file[0].rsplit('/', 1)[-1][:-4]

        folder_title = tv_file[0].rsplit('/')[-2]

        tv_index_file_results = {}

        if tv_file[0].lower().endswith(extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

            title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

            test = pymediainfo.MediaInfo.parse(tv_file[0])

            for track in test.tracks:

                if track.track_type == 'Video':
                    tv_index_file_results[title_key]["DIRECTORY"] = folder_title
                    tv_index_file_results[title_key]["TITLE"] = title.get('title')
                    tv_index_file_results[title_key]["YEAR"] = title.get('year')
                    tv_index_file_results[title_key]["EPISODE TITLE"] = title.get('episode_title')
                    tv_index_file_results[title_key]["SEASON"] = title.get('season')
                    tv_index_file_results[title_key]["EPISODE NUMBER"] = title.get('episode')
                    tv_index_file_results[title_key]["RESOLUTION"] = str(track.width) + 'x' + str(track.height)
                    tv_index_file_results[title_key]["FILE TYPE"] = title.get('container')

        elif tv_file[0].lower().endswith(nfo_extensions) and tv_file[0].rsplit('/', 1)[-1].lower() != 'tvshow.nfo':

            if title_key not in tv_index_file_results:
                tv_index_file_results[title_key] = {}

            with open(tv_file[0]) as f:
                for line in f.readlines():
                    if '<plot>' in line:
                        tv_index_file_results[title_key].update({"PLOT": line})

        for items in tv_index_file_results.items():
            print(items)


movie_index_all_results(username_input='bx')
#tv_index_all_results(username_input='bx')


"""
        for items in tv_index_file_results.items():
            tv_file_results.append(items)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-RESULTS.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f, ["DIRECTORY", "TITLE", "YEAR", "EPISODE TITLE", "SEASON", "EPISODE NUMBER",
                                    "RESOLUTION", "FILE TYPE", "PLOT"])
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)
"""
