import csv
import re


def search_resolution_totals_movies(username_input):
    movie_file_index = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-/MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))
    ten_eighty_found_list = []
    seven_twenty_found_list = []
    standard_def_found_list = []
    empty_response_list = []
    movies_total_list = []

    for res in movie_file_index:

        if re.findall("19\d{2}x", res[2]):
            ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[2]):
            seven_twenty_found_list.append(res)
        elif re.findall("'\d{3}x", res[2]):
            standard_def_found_list.append(res)
        else:
            empty_response_list.append(+1)
        movies_total_list.append(+1)

    print()
    print("-------------------------------------------------------------------------------------------------------")
    print()
    print("NUMBER:# OF (1080p) MOVIES IN DB:")
    print()
    print(len(ten_eighty_found_list))
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print()
    print("NUMBER:# OF (720p) MOVIES IN DB:")
    print()
    print(len(seven_twenty_found_list))
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print()
    print("NUMBER:# OF (SD) MOVIES IN DB:")
    print()
    print(len(standard_def_found_list))
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print()
    print("NUMBER:# OF MOVIES WITHOUT A MARKED RESOLUTION:")
    print()
    print(len(empty_response_list))
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------")
    print()
    print("NUMBER:# OF MOVIES TOTAL:")
    print()
    print(len(movies_total_list))
    print()
    print("-------------------------------------------------------------------------------------------------------")
