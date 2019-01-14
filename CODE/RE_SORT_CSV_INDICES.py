import csv


def re_sort_csv_indices(username_input):
    movie_results = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "r"))
    sorted_movie_results = sorted(movie_results, key=lambda row: row[0])
    tv_results = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', "r"))
    sorted_tv_results = sorted(tv_results, key=lambda row: row[0])
    movie_results_file = []
    tv_results_file = []

    for line in sorted_movie_results:
        movie_results_file.append(line)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results_file:
            csv_writer.writerow(movie_row)

    for line in sorted_tv_results:
        tv_results_file.append(line)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_results_file:
            csv_writer.writerow(tv_row)


