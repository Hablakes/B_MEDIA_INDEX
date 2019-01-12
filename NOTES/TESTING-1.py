import guessit
import pymediainfo


def movie_index_results():
    movie_index = [
        "/home/bx/Videos/CHASE/TEST/He-Man and She-Ra - A Christmas Special (1985)/He-Man and She-Ra"
        " - A Christmas Special (1985) (716x480).m4v"]

    movie_index_file_results = []

    for movie_file in movie_index:

        print(movie_file)

        title = guessit.guessit(movie_file.rsplit('/', 1)[-1], options={'type': 'movie'})

        title_to_year = guessit.guessit(movie_file.rsplit('/')[-2])

        mv_title_and_year = (movie_file.rsplit('/')[-2])

        mv_year = (mv_title_and_year[-5:-1])

        mv_title = (mv_title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file)

        for track in test.tracks:

            if track.track_type == 'Video':
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

        print(title)


movie_index_results()
