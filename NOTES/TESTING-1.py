import csv

media_index_test = csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv'))
media_index_test_list = list(csv.reader(open(r'/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv')))

ten_eighty_p = str("1920")

ten_eighty_found_list = []

for res in media_index_test:
    if ten_eighty_p in res[2]:
        ten_eighty_found_list.append(res)

print("-----------------------------------------------------------------------------------------------------------")
print()
print("# OF 1080p MOVIES IN DB:")
print()
print(len(ten_eighty_found_list))
print()
print("-----------------------------------------------------------------------------------------------------------")


