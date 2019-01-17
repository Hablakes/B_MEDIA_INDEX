import csv
import os

import guessit


def scrape_media_folders_info_for_csv(username_input, movie_dir_input, tv_dir_input, movie_alt_dir_input,
                                      tv_alt_dir_input):
    movie_dir_list = os.listdir(movie_dir_input)
    tv_dir_list = os.listdir(tv_dir_input)
    movie_alt_dir_list = os.listdir(movie_alt_dir_input)
    tv_alt_dir_list = os.listdir(tv_alt_dir_input)

    movie_title_items = []
    tv_title_items = []

    for movie_found in sorted(movie_dir_list):
        movie_scrape_info = guessit.guessit(movie_found)

        title_item_check = ['MOVIE', movie_scrape_info.get('title'), str(movie_scrape_info.get('year'))]

        if "," in title_item_check[2]:
            title_item_check.append(title_item_check[2][-5:-1])
            title_item_check.remove(title_item_check[2])

    if movie_alt_dir_input is not str(''):

        for movie_found in sorted(movie_alt_dir_list):
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

    if tv_alt_dir_input is not str(''):

        for tv_found in sorted(tv_alt_dir_list):
            tv_scrape_info = guessit.guessit(tv_found)

            title_item_check = ['TV', tv_scrape_info.get('title'), str(tv_scrape_info.get('year'))]

            if "," in title_item_check[2]:
                title_item_check.append(title_item_check[2][-5:-1])
                title_item_check.remove(title_item_check[2])

            tv_title_items.append(title_item_check)

    with open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MEDIA-INDEX.csv', "w",
              newline="") as f:
        csv_writer = csv.writer(f)
        for file_row in movie_title_items:
            csv_writer.writerow(file_row)
        for file_row in tv_title_items:
            csv_writer.writerow(file_row)
