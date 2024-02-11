#!/usr/bin/env python3
""" The interractive cmd for the app """
import cmd
import sys
import subprocess
import os
import re
try:
    from pytube import YouTube, Playlist
    from pytube.cli import on_progress
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
    from pytube import YouTube, Playlist
    from pytube.cli import on_progress

class MediaMagnet(cmd.Cmd):
    intro = "Welcome to MediaMagnet. write help to get assistant"
    prompt = "> "

    def do_EOF(self, line):
        """ Exits the program """
        return True;

    def do_exit(self, line):
        """ Exits the program """
        return True;

    def do_download(self, line):
        """ download LINK [MP4/MP3] [HD/SD/FHD] [PATH]
        downloads the video/playlist at LINK into the given PATH.
        if only the link is given, it'll be downloaded at the curr path
        in MP4 HD"""

        avres = {'sd': '480p', 'hd': '720p', 'fhd': '1080px'} # available resolutions

        input = line.split(" ")
        link = re.match('.*\.(?:com|be)\/(.*)\?.*', input[0])
        type = "mp4"
        res = avres['hd']
        path = None

        if input[0] == "" or not link:
            print("The link is missing")
            return

        if len(input) > 1:
            type = input[1]
            if type in ['mp3', 'MP3', '3']:
                type = 'mp3'
            else:
                type = 'mp4'

        if len(input) > 2:
            res = input[2]
            if res in ['fhd', 'FHD', '1080', '1080p', 'f']:
                res = avres['fhd']
            elif res in ['sd', 'SD', '480', '480p', 's']:
                res = avres['sd']
            else:
                print(f"'{res}' is not recognized, using HD.")
                res = avres['hd']

        if len(input) > 3:
            path = input[3]

        if path != None and not os.path.exists(path):
            print("the given path isn't correct, downloading to the current path")
            path = os.getcwd()

        if link[1] == "playlist":
            pl = Playlist(link[0])
            for vid in pl.video_urls:
                yt = YouTube(vid, on_progress_callback=on_progress)
                print(f"downloading '{yt.title}'...")
                if type == 'mp3':
                    stream = yt.streams.get_audio_only()
                    if stream:
                        try:
                            stream.download(path, filename=f"{yt.title}.mp3")
                        except Exception:
                            print(f"Error downloading {yt.title}")
                else:
                    try:
                        yt.streams.filter(res=res).first().download(path)
                    except Exception:
                        print(f"Error downloading {yt.title}")
            print(f"{yt.title} |")
        else:
            yt = YouTube(link[0], on_progress_callback=on_progress)
            print(f"downloading '{yt.title}'...")
            if type == 'mp3':
                stream = yt.streams.get_audio_only()
                if stream:
                    try:
                        stream.download(path, filename=f"{yt.title}.mp3")
                    except Exception:
                        print(f"Error downloading {yt.title}")
            else:
                try:
                    yt.streams.filter(res=res).first().download(path)
                except Exception:
                    print(f"Error downloading {yt.title}")
            print(f"{yt.title} |")


if __name__ == "__main__":
    MediaMagnet().cmdloop()
