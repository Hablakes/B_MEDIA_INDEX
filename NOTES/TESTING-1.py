import os

import guessit


username_input = 'bx'
#movie_dir_input = [input("ENTER PATH OF MOVIES DIRECTORY (CASE SENSITIVE):")]
#tv_dir_input = [input("ENTER PATH OF TV DIRECTORY (CASE SENSITIVE):")]

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_string = str("MOVIE")
tv_string = str("TV")


def scrape_media_info_for_csv():
    tv_dir_list = os.listdir(r'/home/bx/Videos/CHASE/TV')

    for tv_found in sorted(tv_dir_list):
        tv_scrape_info = guessit.guessit(tv_found)

        title_item_check = ["TV", tv_scrape_info.get('title'), tv_scrape_info.get('year')]

        if len(title_item_check[2]) == 1:
            continue

        elif len(title_item_check[2]) != 1:
            title_item_check.append(title_item_check[2][0])
            title_item_check.remove(title_item_check[2])

        print(title_item_check)


scrape_media_info_for_csv()
