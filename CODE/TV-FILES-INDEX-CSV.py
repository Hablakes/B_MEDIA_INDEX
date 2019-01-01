import csv
import os

tv_dir = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"
alt_dirs = r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"

tv_file_results = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")


def search_tv_folders_items():
    for root, dirs, files in os.walk(tv_dir):
        for tv_file in sorted(files):
            if tv_file.endswith(extensions):
                tv_file_results.append([root + '/' + tv_file])

    for root, dirs, files in os.walk(alt_dirs):
        for alt_file in sorted(files):
            if alt_file.endswith(extensions):
                tv_file_results.append([root + '/' + alt_file])


def create_media_files_index():
    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


search_tv_folders_items()
create_media_files_index()
