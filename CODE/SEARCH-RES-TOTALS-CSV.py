import csv
import re

media_index_test = csv.reader(open(r'C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\MEDIA-INDEX-TEST.csv'))


def search_resolution_totals_movies():
    ten_eighty_found_list = []
    seven_twenty_found_list = []
    standard_def_found_list = []

    for res in media_index_test:

        if re.findall("19\d{2}x", res[2]):
            ten_eighty_found_list.append(res)
        if re.findall("12\d{2}x", res[2]):
            seven_twenty_found_list.append(res)
        if re.findall("\d{3}x", res[2]):
            standard_def_found_list.append(res)

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


search_resolution_totals_movies()
