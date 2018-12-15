import subprocess


def open_crt():
    subprocess.call(['bash', '-c', 'cool-retro-term'])


def run_media_index():
    subprocess.call(['bash', '-c', 'python ~/PycharmProjects/B-MEDIA-INDEX/CODE/MEDIA-INDEX.py | lolcat'])


#open_crt()
run_media_index()