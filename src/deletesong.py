import os
import glob

def emptysongsfolder():
    songs = glob.glob('D:\....Coding\discordnightcorebot\songs\*')
    for s in songs:
        os.remove(s)


if __name__ == "__main__":
    emptysongsfolder()