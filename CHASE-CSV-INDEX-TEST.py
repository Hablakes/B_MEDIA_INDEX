import os
import csv

import click


def create_index(media_folders, index_name):

    with open(index_name, 'w') as index_file:
        csv_writer = csv.writer(index_file)
        for media_folder in media_folders:

            for movie_name in os.listdir(media_folder[1]):
                csv_writer.writerow([media_folder[0], movie_name.strip()])

            for tv_name in os.listdir(media_folder[1]):
                csv_writer.writerow([media_folder[0], tv_name.strip()])



def search_index(search_term, index_name):
    """Search Index"""
    movie_results = []
    tv_results = []
    with open(index_name, 'r') as index_file:
        csv_reader = csv.reader(index_file)
        for line in csv_reader:
            #print (line)
            if not line:
                continue
            media_type = line[0]
            media_title = line[1]
            if search_term.lower() in media_title.lower():
                if media_type == "TV":
                    tv_results.append(media_title)
                else:
                    movie_results.append(media_title)

    return tv_results, movie_results


@click.group()
def cli():
    pass


@cli.command()
def rescan():
    print("Rescanning index...")
    media_folders = [
        ["MOVIES", r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/"],
        ["TV", r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV/"],
        ["TV-2", r"/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2/"]
    ]
    create_index(media_folders, "CURRENT-INDEX.txt")


@cli.command()
@click.argument('search-term', nargs=-1)
@click.option('--media-type', type=click.Choice(['all', 'movies', 'tv']), default='all')

def search(search_term, media_type):
    if not search_term:
        search_term = click.prompt('Query?')
    else:
        search_term = ' '.join(search_term)
    tv_results, movie_results = search_index(search_term, "CURRENT-INDEX.txt")

    if media_type.lower() in ['all', 'movies']:
        print("MOVIES")
        for movie in movie_results:
            print('\t' + movie)
    if media_type in ['all', 'tv']:
        print("TV", )
        for tv in tv_results:
            print('\t' + tv)


if __name__ == '__main__':
    cli()