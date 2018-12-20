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

MY RE -

^   #| # Title_No_Space
      (?P<Title_No_Space>\w{0,}\s
      )
    | # Year
      (?P<Year>\(\d{4}\)
    )
    | # Old_Resolution
      (?P<Old_Resolution>\(\d{3,}p\)
    )
    | # Resolution
      (?P<Resolution>\d+x\d+
    )
    | # HD Style Resolution (Oldest)
      (?P<HD>\(HD\)
    )
    | # Parts
      (?P<Parts>Part\s\d{1}
    )
    | # FileType
      (?<=\.)(?P<FileType>[a-z0-9]{3,}
    )
    |
_________________________________________________________________________

YEAR - #\s[0-9][0-9][0-9][0-9]

YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)
_________________________________________________________________________

FILE TYPES - ".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
".xvid", ".srt"
_________________________________________________________________________

USE CAPTURE GROUPS TO MATCH RESOLUTION IN FILENAMES
"""