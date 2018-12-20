import re

movie_data = ""


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

