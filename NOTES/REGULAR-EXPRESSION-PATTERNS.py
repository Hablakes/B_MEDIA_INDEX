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

^     # Titles
      ((?P<Titles>[^\(]+)[\s.]+)
    | # Year
      (\((?P<Year>\d{4})\)
    )
    | # Old_Resolution_Standard
      (\((?P<Old_Resolution_Standard>\d{3,}p)\)
    )
    | # Resolution_Standard
      (?P<Resolution_Standard>\d+x\d+
    )
    | # HD_Resolution Style Resolution (Oldest)
      (\((?P<HD_Resolution>\wD)\)
    )
    | # Parts
      (?P<Parts>Part\s\d{1}
    )
    | # FileType
      (?<=\.)(?P<FileType>[a-z0-9]{3,}
    )

=========================================================================

^    # Titles
      (?P<Titles>[^\(]+)[\s.]
     # Year
      (\((?P<Year>\d{4})\))?
     # Resolution
      (?P<Resolution_Standard>\(\d+x\d+\))?
     # Old_Resolution_Standard
      (\((?P<Old_Resolution_Standard>\d{3,}p)\))?
     # SD_Resolution Style Resolution (Oldest)
      (?P<SD_Resolution>\(SD\))?

_________________________________________________________________________

YEAR - #\s[0-9][0-9][0-9][0-9]

YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)
_________________________________________________________________________

FILE TYPES - ".3gp", ".avi", ".divx", ".img", ".iso," ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".qt", ".webm", ".wmv",
".xvid", ".srt"
_________________________________________________________________________

USE CAPTURE GROUPS TO MATCH RESOLUTION IN FILENAMES
"""