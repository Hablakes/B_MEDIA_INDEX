import csv
import re

import matplotlib.pylab as plt
import numpy as np

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")

username_input = [input("ENTER YOUR USERNAME (CASE-SENSITIVE):")]


def resolution_totals_graphs():
    movie_files_results_list = list(
        csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    tv_files_results_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-RESULTS.csv')))

    m_ten_eighty_found_list = []
    m_seven_twenty_found_list = []
    m_standard_def_found_list = []
    m_empty_response_list = []
    movies_total_list = []

    tv_ten_eighty_found_list = []
    tv_seven_twenty_found_list = []
    tv_standard_def_found_list = []
    tv_empty_response_list = []
    tv_total_list = []

    for res in movie_files_results_list:

        if re.findall("19\d{2}x", res[2]):
            m_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[2]):
            m_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[2]):
            m_standard_def_found_list.append(res)
        else:
            m_empty_response_list.append(+1)
        movies_total_list.append(+1)

    movie_data = [float(len(m_ten_eighty_found_list)), float(len(m_seven_twenty_found_list)),
                  float(len(m_standard_def_found_list))]

    for res in tv_files_results_list:

        if re.findall("19\d{2}x", res[5]):
            tv_ten_eighty_found_list.append(res)
        elif re.findall("1[0-8]\d{2}x", res[5]):
            tv_seven_twenty_found_list.append(res)
        elif re.findall("\d{3}x", res[5]):
            tv_standard_def_found_list.append(res)
        else:
            tv_empty_response_list.append(+1)
        tv_total_list.append(+1)

    tv_data = [float(len(tv_ten_eighty_found_list)), float(len(tv_seven_twenty_found_list)),
            float(len(tv_standard_def_found_list))]

    def format_data(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    labels = ['1080p', '720p', 'SD (Below 720p)']

    colors = ['#85c1e9', '#a569bd', '#808b96']

    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

    wedges, texts, autotexts = ax.pie(movie_data, autopct=lambda pct: format_data(pct, movie_data),
                                      shadow=True, colors=colors, textprops=dict(color="black"))

    ax.legend(wedges, labels,
              title="RESOLUTIONS",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=9, weight='bold')
    ax.set_title("MOVIE-RESOLUTION-RESULTS")
    plt.savefig(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-RESOLUTION-RESULTS.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

    wedges, texts, autotexts = ax.pie(tv_data, autopct=lambda pct: format_data(pct, tv_data),
                                      shadow=True, colors=colors, textprops=dict(color="black"))

    ax.legend(wedges, labels,
              title="RESOLUTIONS",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=9, weight='bold')
    ax.set_title("TV-SHOW-RESOLUTION-RESULTS")
    plt.savefig(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-SHOW-RESOLUTION-RESULTS.png')
    plt.show()


resolution_totals_graphs()
