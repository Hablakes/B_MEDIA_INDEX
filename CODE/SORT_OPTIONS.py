import csv


def sort_function_base(username_input, sort_options_int):
    media_index = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv')))
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


def get_title_ascending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    for item in sorted_title:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_title_descending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    for item in sorted_title_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_ascending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_year = sorted(media_index, key=lambda y: (y[0], y[2]))
    for item in sorted_year:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def get_year_descending(username_input):
    media_index = csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv'))
    sorted_year_r = sorted(media_index, key=lambda y: (y[0], y[2]), reverse=True)
    for item in sorted_year_r:
        print(item)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def total_tv_episodes_sort_function_base(username_input, sort_options_int):
    tv_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    tv_amounts = []
    tv_show_episodes_found = []
    tv_show_found = {}
    for tv_title in tv_results_list:
        tv_amounts.append(tv_title[0])
    for found_tv_title in tv_amounts:
        tv_show_episodes_found.append(found_tv_title)
        tv_show_found[found_tv_title] = tv_show_episodes_found.count(found_tv_title)
    sorted_by_key_d = sorted(tv_show_found.items(), key=lambda kv: kv[0])
    sorted_by_key_a = sorted(tv_show_found.items(), key=lambda kv: kv[0], reverse=True)
    sorted_by_value_d = sorted(tv_show_found.items(), key=lambda kv: kv[1])
    sorted_by_value_a = sorted(tv_show_found.items(), key=lambda kv: kv[1], reverse=True)
    if sort_options_int == 5:
        for item in sorted_by_key_d:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 6:
        for item in sorted_by_key_a:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 7:
        for item in sorted_by_value_d:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
    if sort_options_int == 8:
        for item in sorted_by_value_a:
            print(item)
            print()
            print("--------------------------------------------------------------------------------------------------")
            print()
