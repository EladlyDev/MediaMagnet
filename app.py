import cmd
import sys
import subprocess
import os
try:
    from pytube import YouTube, Playlist
    from pytube.cli import on_progress
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
    from pytube import YouTube, Playlist
    from pytube.cli import on_progress
    pass

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
        downloads the video/playlist at LINK in the given PATH.
        if only the link is given, it'll be downloaded at the curr path
        in MP4 HD"""

        input = line.split(" ")
        if input[0] == "":
            print("The link is missing")

if __name__ == "__main__":
    MediaMagnet().cmdloop()
