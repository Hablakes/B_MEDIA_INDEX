import os


def first_launch_username():
    user_name_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE)")

    os.makedirs(r'/home/' + user_name_input + '/MEDIA-INDEX/', exist_ok=True)

    with open(r'/home/' + user_name_input + '/MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as media_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as movie_files_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tv_files_index_csv:
        pass
    with open(r'/home/' + user_name_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as movie_files_results_csv:
        pass
    with open(r'/home/' + user_name_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tv_files_results_csv:
        pass


first_launch_username()
