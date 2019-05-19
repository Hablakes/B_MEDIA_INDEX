import os

from pathlib import Path


video_test_folder = 'C:/Users/botoole/Downloads/B/B TEST/'


for root, dirs, files in os.walk(video_test_folder):
    print(Path(root).resolve())
    print(os.path.normpath(os.path.expanduser(root)))


"""
Just replace all backslashes with forward slashes?
"""