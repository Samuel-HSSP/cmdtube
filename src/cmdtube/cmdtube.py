# 3:40 PM 20/12/2023
import cmd, json, time, webbrowser, termcolor
from youtube_search import YoutubeSearch
from pytube import YouTube, Playlist
from tqdm import tqdm
from search import Search
from info import Info
from download import Download
from transcript import Transcript
from watch import Watch

class cli(cmd.Cmd): #© doesn't work on the command line, so...
    intro = """
Welcome to CmdTube v0.0.4! A Command Line Interface for programmers who use YouTube (who doesn't?)
Search and download videos and playlists from YouTube over a few commands.
Type `help` for more information
(c) Samuel Ogunleke, 2023.
"""
    prompt = "CMDTube> "
    search_query = ""
    search_results = None
    ARGUMENTS = ["search", "download"]
    recently_searched = False

    def do_exit(self, arg):
        print("Goodbye...see you again!")
        raise SystemExit

    def do_cmdtube(self, arg):
        r"""
#######################################################
Search, watch and download YouTube videos using easy commands.
----------------------------------------------------------------------------------
Are you a programmer and you would love to download YouTube tutorials?
CMDTube is for you! Download YouTube tutorials for free with just a few easy commands.


What you can do:
==============
1. Search for a YouTube video
2. Watch a YouTube video on your browser
3. Download a YouTube video
4. Download a YouTube playlist
5. Get information about a YouTube video
6. Download a YouTube video or a whole playlist as audio
7. Download the subtitles (transcripts/captions) for a YouTube video in almost any language.

Example:
To search YouTube for `Python Programming Tutorials` and display 15 search results:
CmdTube> cmdtube -s "Python Programming Tutorials" -r 15

...
Visit https://github.com/Samuel-HSSP/cmdtube for full documentation
"""
        try:
            if arg.startswith("-s"):
                search = Search(arg)
                self.search_results = search.search_results
            elif arg.startswith("-i"):
                info = Info(arg, search_results=self.search_results)
            elif arg.startswith("-w"):
                watch = Watch(arg, search_results=self.search_results)
            elif arg.startswith("-t"):
                transcript = Transcript(arg, search_results=self.search_results)
            elif arg.startswith("-d"):
                download = Download(arg, search_results=self.search_results)

        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print("Quitting CmdTube...")
            raise SystemExit

def main():
    while True:
        game = cli().cmdloop()

main()