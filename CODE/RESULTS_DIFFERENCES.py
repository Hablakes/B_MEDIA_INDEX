def compare_movie_results_file_and_create_differences_files(username_input):
    username_input_x = input("ENTER USERNAME FOR THE RESULTS LISTS TO COMPARE:")

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv',
              'r') as mr_0, open(
            r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'r') as mr_1:

        movie_results = mr_0.readlines()
        alt_movie_results = mr_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-MOVIE-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_m:
            for line in movie_results:
                if line not in alt_movie_results:
                    outFile_m.write('HAVE: ' + line)

            for line in alt_movie_results:
                if line not in movie_results:
                    outFile_m.write('DO NOT HAVE: ' + line)


def compare_tv_results_file_and_create_differences_files(username_input):
    username_input_x = input("ENTER USERNAME FOR THE RESULTS LISTS TO COMPARE:")

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv',
              'r') as tr_0, open(
            r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'r') as tr_1:

        tv_results = tr_0.readlines()
        alt_tv_results = tr_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-TV-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_t:
            for line in tv_results:
                if line not in alt_tv_results:
                    outFile_t.write('HAVE: ' + line)

            for line in alt_tv_results:
                if line not in tv_results:
                    outFile_t.write('DO NOT HAVE: ' + line)


compare_movie_results_file_and_create_differences_files(username_input='bx')
compare_tv_results_file_and_create_differences_files(username_input='bx')
