import csv
import os
import re

from ascii_graph import Pyasciigraph
import guessit
import matplotlib.pylab as plt
import pyfiglet
import numpy as np
import pymediainfo

from CODE import CONTEXT_MENUS
from CODE import GET_INPUTS_THEN_MOCK_FILES
from CODE import GRAPHS_BAR
from CODE import GRAPHS_PIE
from CODE import GRAPHS_TERMINAL
from CODE import MEDIA_FILE_PATHS_INDEX
from CODE import PARSE_MEDIA_FILES
from CODE import QUERY_MEDIA_FILES_INDICES
from CODE import QUERY_MEDIA_FOLDERS_INDEX
from CODE import RESOLUTION_TOTALS
from CODE import SCRAPE_MEDIA_FOLDERS_INDEX
from CODE import SORT_OPTIONS
from CODE import YEAR_TOTALS


username_input = []
movie_dir_input = []
tv_dir_input = []

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")


CONTEXT_MENUS.launch_media_index()

