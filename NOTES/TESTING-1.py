import os

import guessit

username_input = 'bx'

movie_string = str("MOVIE")
tv_string = str("TV")


def scrape_media_info_for_csv():
    tv_dir_list = os.listdir(r'/home/bx/Videos/CHASE/TEST')

    for tv_found in sorted(tv_dir_list):
        tv_scrape_info = guessit.guessit(tv_found)

        title_item_check = ['TV', tv_scrape_info.get('title'), tv_scrape_info.get('year')]

        if len(title_item_check[2]) == 1:
            continue

        elif len(title_item_check[2]) != 1:
            title_item_check.append(title_item_check[2][-1])
            title_item_check.remove(title_item_check[2])

        print(title_item_check)


scrape_media_info_for_csv()
