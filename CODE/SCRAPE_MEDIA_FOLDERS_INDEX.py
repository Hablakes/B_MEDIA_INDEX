import csv
import os

import guessit

username_input = ['bx']

movie_string = str("MOVIE")
tv_string = str("TV")


def scrape_media_folders_info_for_csv():

    movie_dir_list = os.listdir(r'/home/bx/Videos/CHASE/MOVIES')
    tv_dir_list = os.listdir(r'/home/bx/Videos/CHASE/TV')

    movie_title_items = []
    tv_title_items = []

    for movie_found in sorted(movie_dir_list):
        movie_scrape_info = guessit.guessit(movie_found)

        title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]

        if "," in title_item_check[2]:
            title_item_check.append(title_item_check[2][-5:-1])
            title_item_check.remove(title_item_check[2])

        movie_title_items.append(title_item_check)

    for tv_found in sorted(tv_dir_list):
        tv_scrape_info = guessit.guessit(tv_found)

        title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]

        if "," in title_item_check[2]:
            title_item_check.append(title_item_check[2][-5:-1])
            title_item_check.remove(title_item_check[2])

        tv_title_items.append(title_item_check)

    with open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MEDIA-FOLDERS-INDEX.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in movie_title_items:
            csv_writer.writerow(file_row)
        for file_row in tv_title_items:
            csv_writer.writerow(file_row)


scrape_media_folders_info_for_csv()
