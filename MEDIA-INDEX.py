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


def run_base():
    print()
    print(" ___     _  _ ____ ___  _ ____    _ _  _ ___  ____ _  _")
    print(" |__] __ |\/| |___ |  \ | |__| __ | |\ | |  \ |___  \/")
    print(" |__]    |  | |___ |__/ | |  |    | | \| |__/ |___ _/\_")
    print()
    print()
    print("MEDIA SEARCH:")
    print()
    title_search = input("QUERY?")
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


while True:
    run_base()
    print()
    print()
