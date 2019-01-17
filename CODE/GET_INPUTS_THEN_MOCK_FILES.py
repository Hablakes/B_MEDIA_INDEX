import os


def first_launch_username(username_input):

    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/', exist_ok=True)
    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES', exist_ok=True)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as mi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as mfi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as tfi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as mfr:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as tfr:
        pass
