"""

TITLES -

(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)(\.qt)(\.webm)(\.wmv)|
(\.xvid)|(\.srt)

______________________________________________________________________________________________________________________

TYPES -

patterns = [
    ('season', '(s?([0-9]{1,2}))[ex]'),
    ('episode', '([ex]([0-9]{2})(?:[^0-9]|$))'),
    ('year', '([\[\(]?((?:19[0-9]|20[01])[0-9])[\]\)]?)'),]

types = {
    'season': 'integer',
    'episode': 'integer',
    'year': 'integer',}
______________________________________________________________________________________________________________________

MY RE -

^     # Titles
      (?P<Titles>[^\(]+)[\s.]
    | # Year
      (\((?P<Year>\d{4})\))
    | # Old_Resolution_Standard
      (\((?P<Old_Resolution_Standard>\d{3,}p)\))
    | # Resolution_Standard
      (\((?P<Resolution_Standard>\d+x\d+)\))
    | # HD_SD_Resolution Style Resolution
      (\((?P<HD_SD_Resolution>\wD)\))
    | # Parts
      (?P<Parts>Part\s\d{1})
    | # FileType
      (?<=\.)(?P<FileType>[a-z0-9]{3,})

titles = re.split("(?P<Titles>[^\(]+)[\s.]", movie_data)
titles_wsc = re.split("(?P<Titles_W_S_C>[^\s\-]+)", movie_data)
year = re.split("(\((?P<Year>\d{4})\))?", movie_data)
year_ar = re.split("(\s\((?P<Year_A_R>\d{4})\))?", movie_data)
resolution = re.split("(\((?P<Res_Standard>\d+x\d+)\))?", movie_data)
resolution_ay = re.split("(\s\((?P<Res_A_Y>\d+x\d+)\))?", movie_data)
old_res_standard = re.split("(\((?P<Old_Res_Standard>\d{3,}p)\))?", movie_data)
hd_sd_res_standard = re.split("(\((?P<HD_SD_Res>[A-Z]D)\))?", movie_data)
hd_sd_res_standard_as = re.split("(\s\((?P<HD_SD_Res_A_S>[A-Z]D)\))?", movie_data)
parts = re.split("(\s(?P<Parts>Part\s\d{1,2}))?", movie_data)
file_type = re.split("((?<=\.)(?P<FileType>[\w]{3,}))", movie_data)
______________________________________________________________________________________________________________________

YEAR - #\s[0-9][0-9][0-9][0-9]
YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)
______________________________________________________________________________________________________________________

FILE TYPES - ".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
".xvid", ".srt"
______________________________________________________________________________________________________________________

TESTING -

.+(?<=...)\.|(\.3gp)|(\.avi)|(\.divx)|(\.img)|(\.iso)|(\.m4a)|(\.m4v)|(\.mkv)|(\.mov)|(\.mp4)|(\.mpeg)|(\.qt)|(\.webm)
|(\.wmv)|(\.xvid)|
______________________________________________________________________________________________________________________
"""
