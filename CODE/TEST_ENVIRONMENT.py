import os


from tkinter import filedialog
from tkinter import *

directory_selected_in_function = []


def get_directory_to_scan():
    print()
    print("-" * 100)
    print("___  _  _    ___ ____ ____ ___    ____ ____ _    ___  ____ ____ ____")
    print("|__]  \/  __  |  |___ [__   |  __ |___ |  | |    |  \ |___ |__/ [__ ")
    print("|__] _/\_     |  |___ ___]  |     |    |__| |___ |__/ |___ |  \ ___]")
    print()
    print("-" * 100)
    print()
    root = Tk()
    root.withdraw()
    root.update()
    selected_directory = filedialog.askdirectory()
    directory_selected_in_function.append(selected_directory)
    root.destroy()
    print("-" * 100)
    print("-" * 100)
    print()
    print()
    print("DIRECTORY INPUT: ", selected_directory)
    print()
    print()
    print("-" * 100)
    print("-" * 100)
    print()


def create_test_folders():
    get_directory_to_scan()

    for items in os.listdir(directory_selected_in_function[0]):
        os.makedirs('/home/bx/Videos/CHASE/TEMP/' + items, exist_ok=True)


create_test_folders()
