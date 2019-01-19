def compare_movie_results_file_and_create_differences_files(username_input):
    username_input_x = input("ENTER USERNAME FOR THE RESULTS LISTS TO COMPARE:")

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv',
              'r') as m_0, open(
              r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'r') as m_1:
        movie_results = m_0.readlines()
        alt_movie_results = m_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-MOVIE-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_m:
            for line in compare_results(movie_results, alt_movie_results):
                outFile_m.write(line)


def compare_tv_results_file_and_create_differences_files(username_input):
    username_input_x = input("ENTER USERNAME FOR THE RESULTS LISTS TO COMPARE:")

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv',
              'r') as t_0, open(
              r'/home/' + username_input + '/' + username_input_x + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'r') as t_1:
        tv_results = t_0.readlines()
        alt_tv_results = t_1.readlines()

        with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input_x +
                  '-TV-FILES-COMPARISON-RESULTS.csv', 'w') as outFile_t:
            for line in compare_results(tv_results, alt_tv_results):
                outFile_t.write(line)


def compare_results(results_u, results_a):
    output = []
    for line in results_u:
        if line not in results_a:
            output.append('HAVE: ' + line)

    for line in results_a:
        if line not in results_u:
            output.append('DO NOT HAVE: ' + line)

    return output


compare_movie_results_file_and_create_differences_files('bx')
compare_tv_results_file_and_create_differences_files('bx')
