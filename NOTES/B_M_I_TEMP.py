import os

from pathlib import Path


video_test_folder = 'C:/Users/botoole/Downloads/B/B TEST/'


for root, dirs, files in os.walk(video_test_folder):
    for items in files:
        paths = Path(items)
        print(paths)

