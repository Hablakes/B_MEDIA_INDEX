import csv


def movie_index_results(username_input):
    movie_nfos = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-FILES-INDEX.csv'))
    movie_nfo_files_results = []
    movie_nfo_result = []

    print()
    nfo_file = input("SEARCH:")
    print()

    for nfo_files_index in movie_nfos:
        for nfo_files in nfo_files_index:
            if nfo_file.lower() in nfo_files.lower():
                movie_nfo_files_results.append(nfo_files)

    if int(len(movie_nfo_files_results)) == 0:
        print("NO MATCHES")
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        exit()

    if int(len(movie_nfo_files_results)) > 1:
        for line in movie_nfo_files_results:
            print(line)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
        print("REFINE SEARCH WITH ABOVE RESULTS: SINGLE MATCH NEEDED TO PROCEED")
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
        movie_index_results(username_input)
    else:
        with open(movie_nfo_files_results[0]) as f:
            for line in f.readlines():
                if '<plot>' in line:
                    movie_nfo_result.append(line.split('.'))
    print("-----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------------------------------------")
    for line in movie_nfo_result[0]:
        print(line + '.')
    print()
    print("-----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------------------------------------")
    print()


movie_index_results(username_input='bx')
