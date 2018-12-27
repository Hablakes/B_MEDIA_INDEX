import csv
import re

media_index_test = csv.reader(open(r'C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\MEDIA-INDEX-TEST.csv'))


def search_resolution_totals_movies():
    ten_eighty_found_list = []
    seven_twenty_found_list = []
    standard_def_found_list = []
    empty_response_list = []
    movies_total_list = []

    for res in media_index_test:

        if re.findall("19\d{2}x", res[2]):
            ten_eighty_found_list.append(res)
        if re.findall("1[0-8]\d{2}x", res[2]):
            seven_twenty_found_list.append(res)
        if re.findall("'\d{3}x", res[2]):
            standard_def_found_list.append(res)
        if str("x") not in res[2]:
            empty_response_list.append(+1)
        if str() in res[2]:
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


search_resolution_totals_movies()
