import csv
import os

movies_dir = os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\MOVIES")
tv_dir = os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV")
tv2_dir = os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV2")


def movie_search(lower_title_search, movies_dir):
    for movie_result in movies_dir:
        if lower_title_search in movie_result.lower():
            print(movie_result)
        else:
            continue


def tv_search(lower_title_search, tv_dir):
    for tv_result in tv_dir:
        if lower_title_search in tv_result.lower():
            print(tv_result)
        else:
            continue


def tv2_search(lower_title_search, tv2_dir):
    for tv_result in tv2_dir:
        if lower_title_search in tv_result.lower():
            print(tv_result)
        else:
            continue


media_index = list(csv.reader(open(r'C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\MEDIA-INDEX.csv')))


def get_title_ascending():
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    for item in sorted_title:
        print(item)


def get_title_descending():
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    for item in sorted_title_r:
        print(item)


def get_year_ascending():
    sorted_year = sorted(media_index, key=lambda y: (y[0], y[2]))
    for item in sorted_year:
        print(item)


def get_year_descending():
    sorted_year_r = sorted(media_index, key=lambda y: (y[0], y[2]), reverse=True)
    for item in sorted_year_r:
        print(item)


def run_sort():
    print("___     _  _ ____ ___  _ ____    ____ ____ ____ ___")
    print("|__] __ |\/| |___ |  \ | |__| __ [__  |  | |__/  |")
    print("|__]    |  | |___ |__/ | |  |    ___] |__| |  \  | ")
    print()
    print("SORT METHOD? 1) TITLE ASCENDING 2) TITLE DESCENDING 3) YEAR ASCENDING 4) YEAR DESCENDING 5) EXIT")
    print()
    sort_options = input("ENTER #")
    print()
    sort_options = int(sort_options)
    if sort_options == 1:
        get_title_ascending()
    elif sort_options == 2:
        get_title_descending()
    elif sort_options == 3:
        get_year_ascending()
    elif sort_options == 4:
        get_year_descending()
    elif sort_options == 5:
        launch_media_index()


def movie_listdir():
    return os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\MOVIES")


def tv_listdir():
    return os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV")


def tv2_listdir():
    return os.listdir(r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV2")


found = []

for movie in movie_listdir():
    movie_title = movie.strip()[0:-7]
    movie_year = movie.strip()[-5:-1]
    found.append(["MOVIE", movie_title, movie_year])

for tv in tv_listdir():
    tv_title = tv.strip()[0:-7]
    tv_year = tv.strip()[-5:-1]
    found.append(["TV", tv_title, tv_year])

for tv2 in tv2_listdir():
    tv2_title = tv2.strip()[0:-7]
    tv2_year = tv2.strip()[-5:-1]
    found.append(["TV", tv2_title, tv2_year])

found = sorted(found)


def create_media_index_csv():
    with open(r"C:\Users\botoole\Downloads\B\BPT\B-MEDIA-INDEX\FILES\MEDIA-INDEX.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for row in found:
            csv_writer.writerow(row)


def run_base():
    print()
    print("___     _  _ ____ ___  _ ____    ____ _  _ ____ ____ _   _")
    print("|__] __ |\/| |___ |  \ | |__| __ |  | |  | |___ |__/  \_/")
    print("|__]    |  | |___ |__/ | |  |    |_\| |__| |___ |  \   |   ")
    print()
    print("MEDIA SEARCH:")
    print()
    title_search = input("QUERY?")
    if title_search == str("RESTART-INDEX"):
        launch_media_index()
    print()
    lower_title_search = title_search.lower()
    print()
    print("MOVIES")
    print()
    movie_search(lower_title_search, sorted(movies_dir))
    print()
    print("TV")
    print()
    tv_search(lower_title_search, sorted(tv_dir))
    tv2_search(lower_title_search, sorted(tv2_dir))


def launch_media_index():
    print(" ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print(" |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/")
    print(" |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print("ACTION?  -  1) QUERY INDEX 2) SORT OPTIONS 3) RE-SCAN INDEX 4) EXIT")
    print()
    action = input("ENTER #")
    print()
    action = int(action)
    if action == 1:
        run_base()
    elif action == 2:
        run_sort()
    elif action == 3:
        create_media_index_csv()
    elif action == 4:
        exit()


while True:
    launch_media_index()
