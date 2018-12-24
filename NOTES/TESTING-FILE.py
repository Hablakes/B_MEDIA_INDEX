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
    for movie_file in media_index_test_list:
        print(movie_file)


movie_file_query_and_sort()


