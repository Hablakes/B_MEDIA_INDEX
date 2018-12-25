import csv
import os
from guessit import guessit

media_index = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))
media_index_list = list(csv.reader(open(r"C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX.csv")))

media_index_test = csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv'))
media_index_test_list = list(
    csv.reader(open(r'C:/Users/botoole/Downloads/B/BPT/B-MEDIA-INDEX/FILES/MEDIA-INDEX-TEST.csv')))

movies_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")
tv_dir = os.listdir(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/TV/")

movie_data = os.walk(r"C:/Users/botoole/Downloads/B/BTMP/CHASE/MOVIES/")

test_m_dir = os.walk(r"C:/Users/botoole/Downloads/B/BTMP/TEST/MOVIES/")
test_tv_dir = os.walk(r"C:/Users/botoole/Downloads/B/BTMP/TEST/TV/")

movie_test = [
    "Movie 0 with Super Long Unnecessary Title That Even Has Sp3c!al Characters and 0ther Non-Sense (1990) (1080p).3gp",
    "Movie 1 (HD).mp4",
    "Movie 2 (HD) (1991).webm",
    "Movie 3 (1991) (SD).m4a",
    "Movie 4 (720p).avi",
    "Movie.5 (1995).wmv",
    "Movie 6 (2010).mpeg",
    "Movie Test 0.divx",
    "Movie Test 1 (2000).img",
    "Movie Test 2 (2001) (1920x1080) Part 1.mkv",
    "Movie Test 3 (2001) (1920x1080).mov",
    "Movie Test 4 (2000) (640x480).iso",
    "Movie Test 5 (1990) (1024x768).m4v",
    "Movie Test 6 (1996) (960x1600).mp4",
    "Movie Test 7 (1980) Part 2.xvid",
    "Movie 8 (1986).qt",
    "Movie 8 (1986).srt"]


def run():
    for movie in test_m_dir:
        print(guessit(str(movie)))
    for tv in test_tv_dir:
        print(guessit(str(tv)))


run()

