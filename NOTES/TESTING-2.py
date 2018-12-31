import csv
import re

import numpy as np
import matplotlib.pyplot as plt

movie_file_index = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MOVIE-FILES-INDEX.csv'))

fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))


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

    data = [float(len(ten_eighty_found_list)), float(len(seven_twenty_found_list)),
            float(len(standard_def_found_list)), float(len(empty_response_list))]

    def format_movie_data(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: format_movie_data(pct, data),
                                      textprops=dict(color="black"))

    ax.legend(wedges, labels,
              title="RESOLUTIONS",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=9, weight='bold')

    ax.set_title("MOVIE-FILE-RESOLUTION-RESULTS")

    plt.show()


search_resolution_totals_movies()
