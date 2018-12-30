import csv
import os

import pymediainfo

test = pymediainfo.MediaInfo.parse('/home/bx/Downloads/TV/Vikings (2013)/Vikings - 515 - Hell.mkv')

for track in test.tracks:
    print(track.to_data())
