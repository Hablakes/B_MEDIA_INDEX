"""
_________________________________________________________________________

patterns = [
    ('season', '(s?([0-9]{1,2}))[ex]'),
    ('episode', '([ex]([0-9]{2})(?:[^0-9]|$))'),
    ('year', '([\[\(]?((?:19[0-9]|20[01])[0-9])[\]\)]?)'),
]

types = {
    'season': 'integer',
    'episode': 'integer',
    'year': 'integer',
}
_________________________________________________________________________

^    # Titles
      (?P<Titles>[^\(]+)[\s.]
     # Year
      (\((?P<Year>\d{4})\))?
     # Year After Resolution
      (\s\((?P<Year_A_R>\d{4})\))?
     # Resolution
      (\((?P<Res_Standard>\d+x\d+)\))?
     # Resolution After Year
      (\s\((?P<Res_A_Y>\d+x\d+)\))?
     # Old Resolution Standard
      (\((?P<Old_Res_Standard>\d{3,}p)\))?
     # HD_SD Resolution Style Resolution
      (\((?P<HD_SD_Res>[A-Z]D)\))?
     # HD_SD Resolution Style Resolution After Space
      (\s\((?P<HD_SD_Res_A_S>[A-Z]D)\))?
     # Parts
      (\s(?P<Parts>Part\s\d{1}))?
    |# FileType
      (?<=\.)(?P<FileType>[\w]{3,})?

_________________________________________________________________________

YEAR - #\s[0-9][0-9][0-9][0-9]

YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)
_________________________________________________________________________

FILE TYPES - ".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
".xvid", ".srt"
_________________________________________________________________________

USE CAPTURE GROUPS TO MATCH RESOLUTION IN FILENAMES
"""