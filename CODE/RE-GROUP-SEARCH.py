import re

regex = r"""
	^   | # Year
	      (\((?P<Year>\d{4})\)
	    )
	    | # Old_Resolution_Standard
	      (\((?P<Old_Resolution_Standard>\d{3,}p)\)
	    )
	    | # Resolution_Standard
	      (\((?P<Resolution_Standard>\d+x\d+)\))
	    | # HD_Resolution Style Resolution (Oldest)
	      (\((?P<HD_Resolution>\wD)\)
	    )
	    | # Parts
	      (?P<Parts>Part\s\d{1}
	    )
	    | # FileType
	      (?<=\.)(?P<FileType>[a-z0-9]{3,}
	    )"""

movie_test = str([
    "Movie with Super Long Unnecessary Title That Even Has Sp3c!al Characters and 0ther Non-Sense (1990) (1080p).avi",
    "Movie (HD).mp4",
    "Movie (HD) (1991).mp4",
    "Movie (1991) (SD).m4a",
    "Movie (720p).avi",
    "Movie.(1995).avi",
    "Movie (2010)",
    "Movie Test 0.divx",
    "Movie Test 1 (2000).avi",
    "Movie Test 2 (2001) (1920x1080) Part 1.mkv",
    "Movie Test 3 (2001) (1920x1080).mkv",
    "Movie Test 4 (2000) (640x480).avi",
    "Movie Test 5 (1990) (1024x768).avi",
    "Movie Test 6 (1996) (960x1600).mp4",
    "Movie Test 7 (1980) Part 2.xvid"])

movies_found = []

matches = re.finditer(regex, movie_test, re.VERBOSE | re.MULTILINE)

for movie_found in movie_test:
    for extension in [".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt",
                      ".webm", ".wmv", ".xvid", ".srt"]:
        movie_matches = matches
        movies_found.append([movie_matches])


print(movies_found)