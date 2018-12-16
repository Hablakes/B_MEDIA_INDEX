import os
import csv

media_paths = [
    ["MOVIES", r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\MOVIES"],
    ["TV", r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV"],
    ["TV-2", r"C:\Users\botoole\Downloads\B\BTMP\BLAIR\TV2"]
]


def create_index(media_paths, current_index):
    with open(current_index, 'w', newline='') as index_file:
        csv_writer = csv.writer(index_file)
        for media_folder in media_paths:

            for title in os.listdir(media_folder[1]):
                csv_writer.writerow([media_folder[0], title.strip()[0:-7], title.strip()[-5:-1]])


create_index(media_paths, "CURRENT-INDEX.csv")
