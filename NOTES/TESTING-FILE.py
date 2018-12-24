import csv

media_index_test = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv'))
media_index_test_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv')))

movie_title = media_index_test_list[0]
movie_year = media_index_test_list[1]
movie_resolution = media_index_test_list[2]
movie_resolution_alt_1 = media_index_test_list[3]
movie_resolution_alt_2 = media_index_test_list[4]
movie_parts = media_index_test_list[5]
movie_file_type = media_index_test_list[6]


def movie_file_query_and_sort():
    mv_query_action = input("ENTER SEARCH QUERY:")
    print()
    mv_query_action_lower = str(mv_query_action.lower())
    for movie_file in media_index_test_list:
        if mv_query_action_lower in movie_file[0].lower():
            print("MOVIE TITLE:")
            print(movie_file[0])
            print()
            print("MOVIE YEAR:")
            print(movie_file[1])
            print()
            print("MOVIE RESOLUTION:")
            print(movie_file[2])
            print()
            print("MOVIE PARTS:")
            print(movie_file[5])
            print()
            print("MOVIE FILE TYPE:")
            print(movie_file[6])
            print()


movie_file_query_and_sort()
