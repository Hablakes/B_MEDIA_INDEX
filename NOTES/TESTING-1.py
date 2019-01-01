import re

import pymediainfo

test = pymediainfo.MediaInfo.parse(
    '/home/bx/Videos/TEST/Sciencephile The Ai (2016)/Sciencephile The AI - Time Traveler\'s Handbook.mp4')

for track in test.tracks:
    print(track.other_file_name, track.codec_id_info, track.other_duration, track.sampled_width, track.sampled_height,
          track.frame_rate,) #track.to_data())


