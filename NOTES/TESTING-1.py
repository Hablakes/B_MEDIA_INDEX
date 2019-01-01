import pymediainfo

test = pymediainfo.MediaInfo.parse(
    "/home/bx/Videos/TEST/Sciencephile The Ai (2016)/Sciencephile The AI - Time Traveler's Handbook.mp4")


def scrape_file_info_from_list():
    file_titles = []
    file_codecs = []
    file_resolutions = []
    file_frame_rates = []

    for track in test.tracks:
        file_titles.append(track.other_file_name)
        file_codecs.append(track.codec_id_info)
        file_resolutions.append([track.sampled_width, track.sampled_height])
        file_frame_rates.append(track.frame_rate)

    print(file_titles)
    print(file_codecs)
    print(file_resolutions)
    print(file_frame_rates)


scrape_file_info_from_list()
