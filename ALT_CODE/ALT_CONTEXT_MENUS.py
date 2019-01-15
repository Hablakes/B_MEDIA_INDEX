from ALT_CODE import ALT_MEDIA_FOLDERS_INDEX
from ALT_CODE import ALT_PARSE_UPDATED_MEDIA_FILES
from ALT_CODE import ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES
from CODE import CONTEXT_MENUS
from CODE import PARSE_MEDIA_FILES


def alt_context_menus():
    print("___  _  _    _ _  _ ___  ____ _  _    ____ ___  ___ _ ____ _  _ ____")
    print("|__]  \/  __ | |\ | |  \ |___  \/  __ |  | |__]  |  | |  | |\ | [__")
    print("|__] _/\_    | | \| |__/ |___ _/\_    |__| |     |  | |__| | \| ___]")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    print("1) CREATE NEW MEDIA INDEX                -  2) UPDATE MEDIA INDEX")
    print()
    print("3) CREATE NEW PARSE-RESULTS INDICES      -  4) UPDATE PARSE-RESULTS INDICES")
    print()
    print("5) CREATE ALL NEW INDICES                -  6) UPDATE ALL INDICES                    - 7) EXIT")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    acmi_input = input("ENTER #")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    acmi_action = int(acmi_input)

    if acmi_action == 1:
        ALT_MEDIA_FOLDERS_INDEX.scrape_media_info_for_csv(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2')
        ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.create_media_files_indices(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2')

    elif acmi_action == 2:
        ALT_MEDIA_FOLDERS_INDEX.scrape_media_info_for_csv(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2')
        ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.compare_old_and_updated_indices_and_create_differences_files(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server='
                            '10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server='
                         '10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server='
                             '10.0.0.3,share=bx-tv-2/TV-2')

    elif acmi_action == 3:
        PARSE_MEDIA_FILES.create_media_files_index_results_csv(username_input='bx')

    elif acmi_action == 4:
        ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.compare_old_and_updated_indices_and_create_differences_files(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server='
                            '10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server='
                         '10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server='
                             '10.0.0.3,share=bx-tv-2/TV-2')
        ALT_PARSE_UPDATED_MEDIA_FILES.create_media_files_index_results_csv(username_input='bx')

    elif acmi_action == 5:
        ALT_MEDIA_FOLDERS_INDEX.scrape_media_info_for_csv(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2')
        PARSE_MEDIA_FILES.create_media_files_index_results_csv(username_input='bx')

    elif acmi_action == 6:
        ALT_MEDIA_FOLDERS_INDEX.scrape_media_info_for_csv(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server=10.0.0.3,share=bx-tv-2/TV-2')
        ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.create_media_files_indices(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server='
                            '10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server='
                         '10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server='
                             '10.0.0.3,share=bx-tv-2/TV-2')
        ALT_UPDATE_AND_COMPARE_MEDIA_FILE_INDICES.compare_old_and_updated_indices_and_create_differences_files(
            username_input='bx',
            movie_dir_input='/run/user/1000/gvfs/smb-share:server='
                            '10.0.0.3,share=bx-movies/MOVIES/',
            movie_alt_dir_input='',
            tv_dir_input='/run/user/1000/gvfs/smb-share:server='
                         '10.0.0.3,share=bx-tv/TV',
            tv_alt_dir_input='/run/user/1000/gvfs/smb-share:server='
                             '10.0.0.3,share=bx-tv-2/TV-2')
        ALT_PARSE_UPDATED_MEDIA_FILES.create_media_files_index_results_csv(username_input='bx')

    elif acmi_action == 7:
        CONTEXT_MENUS.second_launch_lmi()

    CONTEXT_MENUS.second_launch_lmi()
