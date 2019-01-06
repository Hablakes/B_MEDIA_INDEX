import csv

media_index = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv')))


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
    print("SORT METHOD? 1) TITLE ASCENDING 2) TITLE DESCENDING 3) YEAR ASCENDING 4) YEAR DESCENDING")
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


while True:
    run_sort()
