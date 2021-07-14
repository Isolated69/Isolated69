from playsound import playsound
import os
from time import sleep

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'



def play_song(song_index, loc, song_list):
        try:
            playsound(fr'{loc}\{song_list[song_index]}')
        except Exception as e:
            print(fr'A problem occurred in initializing MCI. (Try the .wav version)')
            sleep(2)

ask = True
if __name__ == '__main__':
    while True:
        if ask:
            user = input('Enter folder name [Desktop]:\n>> ')
            save = input('Save directory for entire runtime [Y/N]:\n>> ').lower()

        if save == 'y':
            ask = False

        try:
            loc = fr'{os.environ["USERPROFILE"]}\Desktop\{user}'
            music_dict = {name: index for name, index in enumerate(os.listdir(loc))}
        except:
            ask = True
            print(fr'No folder "{user}" found')
            continue

        mp3 = False
        mp3_count = 0
        for index in music_dict:
            print(f'{index}) {music_dict[index]}')
            if os.path.splitext(music_dict[index])[1] == '.mp3':
                mp3_count += 1

        if mp3_count > 0:
            print(f'{bcolors.WARNING}{mp3_count} mp3 file(s) detected, errors may happen please convert to .wav{bcolors.ENDC}')
        
        choice = int(input(f'Play song [1-{index}]:\n>> '))

        play_song(choice, loc, music_dict)

