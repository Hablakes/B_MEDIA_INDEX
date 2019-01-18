

def compare_results_files_and_create_differences_files(username_input, username_input_alt):

    username_input_alt = input("ENTER USERNAME FOR RESULTS LISTS TO COMPARE:")

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv',
              'r') as mr_0, open(
        r'/home/' + username_input + '/' + username_input_alt + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'r') as mr_1:
        movie_results = mr_0.readlines()
        alt_movie_results = mr_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-COMPARISON-RESULTS.csv',
                  'w') as outFile:
            for line in movie_results:
                if line not in alt_movie_results:
                    outFile.write(line)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv',
              'r') as tr_0, open(
        r'/home/' + username_input + '/' + username_input_alt + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'r') as tr_1:
        tv_results = tr_0.readlines()
        alt_tv_results = tr_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-COMPARISON-RESULTS.csv',
                  'w') as outFile:
            for line in tv_results:
                if line not in alt_tv_results:
                    outFile.write(line)


compare_results_files_and_create_differences_files(username_input='bx', username_input_alt='xx')
