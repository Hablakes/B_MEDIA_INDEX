import csv
import textwrap
import re


def movie_query_all_results(username_input):
    movie_results = csv.reader(
        open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/MOVIE-RESULTS.csv'))

    movie_found_results = {}

    mv_query_action = input("ENTER SEARCH QUERY (MOVIES):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    mv_query_action_lower = str(mv_query_action.lower())

    for movie_file in sorted(movie_results):
        if mv_query_action_lower in movie_file[1].lower():
            if movie_file[0] not in movie_found_results:
                movie_found_results[str(movie_file[0])] = []
            movie_found_results[str(movie_file[0])].append(movie_file)

    for items in movie_found_results.items():
        print()
        print()
        print("MOVIE FOLDER")
        print()
        print(items[1][0][0])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE TITLE")
        print()
        print(items[1][0][1])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE YEAR")
        print()
        print(items[1][0][2])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE RESOLUTION")
        print()
        print(items[1][0][3])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE FILE-TYPE")
        print()
        print(items[1][0][4])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE RATING")
        print()
        movie_rating = re.findall("<rating>(.*?)</rating>", items[1][0][6])
        print(movie_rating[0])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE RUN-TIME")
        print()
        movie_runtime = re.findall("<runtime>(.*?)</runtime>", items[1][0][7])
        print(movie_runtime[0])
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE PLOT")
        print()
        movie_plot = re.findall("<plot>(.*?)</plot>", items[1][0][5])
        print(textwrap.fill(movie_plot[0], 80))
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


movie_query_all_results(username_input='bx')
