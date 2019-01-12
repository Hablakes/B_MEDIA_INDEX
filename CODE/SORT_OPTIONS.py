import csv


def sort_function_base(username_input, sort_options_int):

    media_index = list(csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    sorted_year = sorted(media_index, key=lambda x: (x[0], x[2]))
    sorted_year_r = sorted(media_index, key=lambda x: (x[0], x[2]), reverse=True)
    if sort_options_int == 1:
        for title_item in sorted_title:
            print(title_item)
    elif sort_options_int == 2:
        for title_item in sorted_title_r:
            print(title_item)
    elif sort_options_int == 3:
        for title_item in sorted_year:
            print(title_item)
    elif sort_options_int == 4:
        for title_item in sorted_year_r:
            print(title_item)


##################################################################################################################


def get_title_ascending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    for item in sorted_title:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_title_descending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    for item in sorted_title_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_ascending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_year = sorted(media_index, key=lambda y: (y[0], y[2]))
    for item in sorted_year:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_descending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_year_r = sorted(media_index, key=lambda y: (y[0], y[2]), reverse=True)
    for item in sorted_year_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()
