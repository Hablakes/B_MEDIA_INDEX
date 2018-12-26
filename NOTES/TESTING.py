import os

import guessit

movie_dir = sorted(os.listdir(r"/home/bx/Videos/CHASE/MOVIES/"))
tv_dir = sorted(os.listdir(r"/home/bx/Videos/CHASE/TV/"))

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
    for movie in tv_dir:
        print(guessit.guessit(str(movie)))


run()

## TESTING TO GET GUESSIT OPTIONS TO PUSH TO LIST CATEGORIES FOR LATER SORTING / DISPLAY ##


# GET TO IGNORE "Alternate" and "He-", or see as strings, currently show as "Version: Alternate" and "Language: He" #
