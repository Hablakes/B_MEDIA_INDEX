import csv

username_input_list = [input("USERNAME:")]


def sort_function_base():

    sort_input_list = [int(input("SORT METHOD, T: 1 A, 2 D - Y: 3 A, 4 D"))]
    media_index = list(csv.reader(open(r'/home/' + username_input_list[0] + '/MEDIA-INDEX/MEDIA-INDEX.csv')))
    sorted_title = sorted(media_index, key=lambda x: (x[0], x[1]))
    sorted_title_r = sorted(media_index, key=lambda x: (x[0], x[1]), reverse=True)
    sorted_year = sorted(media_index, key=lambda x: (x[0], x[2]))
    sorted_year_r = sorted(media_index, key=lambda x: (x[0], x[2]), reverse=True)
    if sort_input_list[0] == 1:
        for title_item in sorted_title:
            print(title_item)
    elif sort_input_list[0] == 2:
        for title_item in sorted_title_r:
            print(title_item)
    elif sort_input_list[0] == 3:
        for title_item in sorted_year:
            print(title_item)
    elif sort_input_list[0] == 4:
        for title_item in sorted_year_r:
            print(title_item)


while True:
    sort_function_base()
