import os


def first_launch_username(username_input):

    os.makedirs(r'/home/' + username_input + '/MEDIA-INDEX/', exist_ok=True)
    os.makedirs(r'/home/' + username_input + '/MEDIA-INDEX/FILES', exist_ok=True)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as media_index_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as movie_f_index_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tv_f_index_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv', 'w') as old_movie_f_index_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/OLD-TV-FILES-INDEX.csv', 'w') as old_tv_f_index_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as movie_f_results_csv:
        pass
    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tv_f_results_csv:
        pass
