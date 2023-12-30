#!/usr/bin/env python3
import validators
from pytube import YouTube, Playlist
import os
from pytube.cli import on_progress

logo = """
  __  __          _ _       __  __                        _   
 |  \/  |        | (_)     |  \/  |                      | |  
 | \  / | ___  __| |_  __ _| \  / | __ _  __ _ _ __   ___| |_ 
 | |\/| |/ _ \/ _` | |/ _` | |\/| |/ _` |/ _` | '_ \ / _ \ __|
 | |  | |  __/ (_| | | (_| | |  | | (_| | (_| | | | |  __/ |_ 
 |_|  |_|\___|\__,_|_|\__,_|_|  |_|\__,_|\__, |_| |_|\___|\__|
                                          __/ |               
                                         |___/                
"""

def validate(choice, choices):
    while 1:
        try:
            choice = int(choice)
            if choice > len(choices) - 1:
                raise ValueError
        except (ValueError, TypeError):
            print("please enter a  valid option")
            choice = input(f"{choices}: ")
        else:
            break

    return choice



def main():
    """ an entry point """

    # welcome
    print(f"{'welcome to' : ^55}{logo}{'Here u can download and do another useful stuff' : ^60}\n\n")

    available = ['tools', 'downloader']
    ans1 = input(f"{available}?: ")
    while ans1[0] not in f"{available[0][0]}{available[1][0]}":
        ans1 = input(f"Please choose a valid option\n{available}?: ")
    else:
        if ans1[0] == f"{available[0][0]}":
            print(f"\n\nwelcome to the tools\nwhat do u wanna do?\n")
            ans1 = 0
        elif ans1[0] == f"{available[1][0]}":
            print(f"\n\nwelcome to the downloader\nwhat do u wanna download?\n")
            ans1 = 1

    if ans1 == 1:                # the downloader
        platforms = ['(0) Youtube']
        platform = input(f"choose the platform {platforms}: ")
        platform = validate(platform, platforms)

        if platform == 0:        # Youtube
            ytchoices = ["(0) video", "(1) playList", "(2) vide as audio",
                         "(3) playlist as audio"]
            ytchoice = input(f"what do u wanna download? {ytchoices}: ")
            ytchoice = validate(ytchoice, ytchoices)

            url = input("enter the url: ")
            while not validators.url(url):
                print("please enter a valid url")
                url = input("enter the url: ")

            if ytchoice == 0 or ytchoice == 2:   # video or audio
                yt = YouTube(url, on_progress_callback=on_progress)
                print(f"downloading '{yt.title}'...")
                if ytchoice == 0:
                    yt.streams.filter(res="720p").first().download(os.getcwd())
                elif ytchoice == 2:
                    stream = yt.streams.filter(only_audio=True).first()
                    stream.download(filename=f"{video.title}.mp3")
                print(f"{yt.title}")
            elif ytchoice == 1 or ytchoice == 3: # playlist
                print("downloading the playlist...")
                pl = Playlist(url)
                for vid in pl.video_urls:
                    ytvid = YouTube(vid, on_progress_callback=on_progress)
                    if (ytchoice == 1):
                        stream = ytvid.streams.filter(res="720p").first()
                        if stream:
                            stream.download(filename=f"{ytvid.title}.mp4")
                    elif ytchoice == 3:
                        stream = ytvid.streams.filter(only_audio=True).first()
                        if stream:
                            stream.download(filename=f"{ytvid.title}.mp3")
                    print(f"{ytvid.title} ")

main()
