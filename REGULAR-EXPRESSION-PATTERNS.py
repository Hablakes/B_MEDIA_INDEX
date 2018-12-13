"""

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



YEAR - #\s[0-9][0-9][0-9][0-9]

YEAR + RES - (.+) \((\d{4})\) \((.+)x(.+)\)\.(.+)

FILE TYPES - (".avi"),(".divx"),(".flv"),(".img"),(".iso"),(".m4v"),
(".mov"),(".mp4"),(".mpeg"),(".qt"),(".webm"),(".wmv"),(".xvid")




USE CAPTURE GROUPS TO MATCH RESOLUTION IN FILENAMES
"""