import csv
import re

import matplotlib.pyplot as plt

movie_file_index = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))


def search_resolution_totals_movies():
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
    labels = ['1080p', '720p', 'SD (Below 720p)', 'NONE']
    sizes = [float(len(ten_eighty_found_list)), float(len(seven_twenty_found_list)),
             float(len(standard_def_found_list)), float(len(empty_response_list))]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.savefig(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MOVIE-RESOLUTION-RESULTS.png')
    plt.show()


search_resolution_totals_movies()

