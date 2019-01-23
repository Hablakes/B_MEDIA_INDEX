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
        print(movie_runtime[0], "- Minutes")
        print("--------------------------------------------------------------------------------------------------")
        print()
        print("MOVIE PLOT")
        print()
        movie_plot = re.findall("<plot>(.*?)</plot>", items[1][0][5])
        print(textwrap.fill(movie_plot[0], 80))
        print()
        print("--------------------------------------------------------------------------------------------------")
        print()


def tv_query_all_results(username_input):
    tv_files_results_list = list(
        csv.reader(open(r'/home/' + username_input + '/' + username_input + '-MEDIA-INDEX/TV-RESULTS.csv')))

    tv_show_query_action = input("ENTER SEARCH QUERY (TV SHOWS):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    tv_show_query_action_lower = str(tv_show_query_action.lower())

    for tv_file in tv_files_results_list:

        if tv_show_query_action_lower in tv_file[1].lower():

            print()
            print()
            print("TV SHOW FOLDER")
            print()
            print(tv_file[0])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW TITLE")
            print()
            print(tv_file[1])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW YEAR")
            print()
            print(tv_file[2])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW EPISODE TITLE")
            print()
            print(tv_file[3])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("SEASON NUMBER")
            print()
            print(tv_file[4])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("EPISODE NUMBER")
            print()
            print(tv_file[5])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("RESOLUTION")
            print()
            print(tv_file[6])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("FILE-TYPE")
            print()
            print(tv_file[7])
            print("--------------------------------------------------------------------------------------------------")
            print()
            if int(len(tv_file[9])) != 0:

                print("RATING")
                print()
                tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                print(tv_rating[0])
                print()
                print("-------------------------------------------------"
                      "-------------------------------------------------")
                print()

            if int(len(tv_file[8])) != 0:

                    print("PLOT")
                    print()
                    if '</plot>' not in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)", tv_file[8])
                        print(tv_plot)
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

                    elif "</plot>" in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                        print(tv_plot[0])
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

        elif tv_show_query_action_lower in tv_file[3].lower():

            print()
            print()
            print("TV SHOW FOLDER")
            print()
            print(tv_file[0])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW TITLE")
            print()
            print(tv_file[1])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW YEAR")
            print()
            print(tv_file[2])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("TV SHOW EPISODE TITLE")
            print()
            print(tv_file[3])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("SEASON NUMBER")
            print()
            print(tv_file[4])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("EPISODE NUMBER")
            print()
            print(tv_file[5])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("RESOLUTION")
            print()
            print(tv_file[6])
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("FILE-TYPE")
            print()
            print(tv_file[7])
            print("--------------------------------------------------------------------------------------------------")
            print()
            if int(len(tv_file[9])) != 0:

                print("RATING")
                print()
                tv_rating = re.findall("<rating>(.*?)</rating>", tv_file[9])
                print(tv_rating[0])
                print()
                print("-------------------------------------------------"
                      "-------------------------------------------------")
                print()

            if int(len(tv_file[8])) != 0:

                    print("PLOT")
                    print()
                    if '</plot>' not in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)", tv_file[8])
                        print(tv_plot)
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()

                    elif "</plot>" in tv_file[8]:
                        tv_plot = re.findall("<plot>(.*?)</plot>", tv_file[8])
                        print(tv_plot[0])
                        print("-------------------------------------------------"
                              "-------------------------------------------------")
                        print()


#movie_query_all_results(username_input='bx')
tv_query_all_results(username_input='bx')
