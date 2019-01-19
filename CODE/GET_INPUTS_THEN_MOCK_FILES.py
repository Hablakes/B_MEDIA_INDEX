import os


def first_launch_username(username_input):
    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/', exist_ok=True)
    os.makedirs(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/FILES', exist_ok=True)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', 'w') as mi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-INDEX.csv', 'w') as mi:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-INDEX.csv', 'w') as ti:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-NFO-FILES-INDEX.csv') as mn:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-NFO-FILES-INDEX.csv') as tn:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', 'w') as m:
        pass
    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv', 'w') as t:
        pass
