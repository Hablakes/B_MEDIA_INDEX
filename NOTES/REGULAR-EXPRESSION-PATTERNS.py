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

COMPLETE (In Progress) -

^(
  (?P<ShowNameA>.*[^ (_.]) # Show name
    [ (_.]+
    ( # Year with possible Season and Episode
      (?P<ShowYearA>\d{4})
      ([ (_.]+S(?P<SeasonA>\d{1,2})E(?P<EpisodeA>\d{1,2}))?
    | # Season and Episode only
      (?<!\d{4}[ (_.])
      S(?P<SeasonB>\d{1,2})E(?P<EpisodeB>\d{1,2})
    | # Alternate format for episode
      (?P<EpisodeC>\d{3})
    )
|
  # Show name with no other information
  (?P<ShowNameB>.+)
)

_________________________________________________________________________

MY OWN (In Progress) -

^
      # Title


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
      (?P<Parts>(Part\s\d{1})
    )
    | # FileType
      (?P<FileType>\.[a-z0-9]{3,}
    )
    |

_________________________________________________________________________

YEAR - #\s[0-9][0-9][0-9][0-9]

YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)

_________________________________________________________________________

FILE TYPES - (".avi"),(".divx"),(".flv"),(".img"),(".iso"),(".m4v"),
(".mov"),(".mp4"),(".mpeg"),(".qt"),(".webm"),(".wmv"),(".xvid")

_________________________________________________________________________

USE CAPTURE GROUPS TO MATCH RESOLUTION IN FILENAMES
"""