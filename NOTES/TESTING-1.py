import csv


def first_launch_dirs():
    print("____ ___ ____ ____ ___    ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print("[__   |  |__| |__/  |  __ |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/ ")
    print("___]  |  |  | |  \  |     |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global username_input
    username_input = input("ENTER YOUR USERNAME (CASE-SENSITIVE):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    global movie_dir_input, tv_dir_input, movie_alt_dir_input, tv_alt_dir_input
    movie_dir_input = input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):")
    tv_dir_input = input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):")
    movie_alt_dir_input = input("ENTER PATH OF ANY ALTERNATE MOVIE DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
    tv_alt_dir_input = input("ENTER PATH OF ANY ALTERNATE TV SHOW DIRECTORIES, LEAVE BLANK IF NONE (CASE SENSITIVE):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()

    user_info = {'user:': username_input, 'movie_dir:': movie_dir_input, 'tv_dir:': tv_dir_input,
                 'movie_alt_dir:': movie_alt_dir_input, 'tv_alt_dir:': tv_alt_dir_input}

    with open(
            r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/' + username_input + '-USER-INFO.csv',
            'w') as f:
        csv_writer = csv.writer(f)
        for row in user_info.items():
            csv_writer.writerow(row)


first_launch_dirs()
