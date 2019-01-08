import os


def start_up_for_first_launch():
    user_name_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE)")

    os.makedirs(r'/home/' + user_name_input + '/MEDIA-INDEX/', exist_ok=True)

    with open(r'/home/' + user_name_input + '/MEDIA-INDEX.csv', 'w') as media_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/MOVIE-FILES-INDEX.csv', 'w') as movie_files_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/TV-FILES-INDEX.csv', 'w') as tv_files_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/MOVIE-FILES-RESULTS.csv', 'w') as movie_files_results_csv:
        pass
    with open(r'/home/' + user_name_input + '/TV-FILES-RESULTS.csv', 'w') as tv_files_results_csv:
        pass


start_up_for_first_launch()