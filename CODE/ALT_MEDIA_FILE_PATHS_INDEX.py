import csv
import os

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

alt_dir = r"/run/media/bx/HEISENBERG/b"


def search_folder_items_and_save_file_paths():
    file_results = []
    for root, dirs, files in os.walk(alt_dir):
        for file in sorted(files):
            if file.endswith(extensions):
                file_results.append([root + '/' + file])

    with open(r'/home/bx/MEDIA-INDEX/ALT-FILES-INDEX.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for row in sorted(file_results):
            csv_writer.writerow(row)


search_folder_items_and_save_file_paths()
