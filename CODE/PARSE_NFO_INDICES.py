import csv


def movie_index_results(username_input):
    movie_nfos = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-FILES-INDEX.csv'))
    movie_nfo_file_results = []

    nfo_file = input("SEARCH:")

    for nfo_files_index in movie_nfos:
        for nfo_files in nfo_files_index:
            if nfo_file in nfo_files:
                movie_nfo_file_results.append(nfo_files)

            if int(len(movie_nfo_file_results)) > 1:
                print("REFINE SEARCH WITH ABOVE RESULTS: SINGLE MATCH NEEDED TO PROCEED")
                movie_index_results(username_input)

            else:
                with open(nfo_files) as f:
                    for line in f:
                        print(line)


movie_index_results(username_input='bx')

