import csv

import guessit
import pymediainfo

movie_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv"))
tv_index = csv.reader(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX.csv"))


def get_movie_index_results():
    movie_index_file_results = []

    for movie_file in movie_index:

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1])

        title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (title_and_year[-5:-1])

        mv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-RESULTS.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)


def get_tv_show_index_results():
    tv_index_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

        title_and_year = (tv_file[0].rsplit('/')[-2])

        tv_year = (title_and_year[-5:-1])

        tv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                tv_index_file_results.append(
                    [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                     title.get('episode'), title('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


def create_media_files_index_results_csv():
    get_movie_index_results()
    get_tv_show_index_results()


create_media_files_index_results_csv()