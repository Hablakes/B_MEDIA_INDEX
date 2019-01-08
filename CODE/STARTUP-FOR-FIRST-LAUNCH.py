import os

username_input = []

movie_dir_input = []
tv_dir_input = []


def first_launch_username():
    user_name_input_action = username_input.append(input("ENTER YOUR USERNAME (CASE-SENSITIVE)"))

    os.makedirs(r'/home/' + username_input[0] + '/MEDIA-INDEX/', exist_ok=True)

    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as media_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as movie_files_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tv_files_index_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as movie_files_results_csv:
        pass
    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tv_files_results_csv:
        pass


def first_launch_dirs():
    movie_dir = movie_dir_input.append(input("ENTER PATH OF MOVIES DIRECTORY:"))
    tv_dir = tv_dir_input.append(input("ENTER PATH OF TV DIRECTORY:"))


first_launch_username()
first_launch_dirs()
