# 6:13 PM 2/4/2022
import cmd, json, time, webbrowser, termcolor
from youtube_search import YoutubeSearch
from pprint import pprint
from pytube import YouTube, Playlist
from tqdm import tqdm

class cli(cmd.Cmd): #© doesn't work on the command line, so...
    intro = """
Welcome to CmdTube! A Command Line Interface for programmers who use YouTube (who doesn't?)
Search and download videos and playlists from YouTube over a few commands.
Type `help` for more information
(c) Samuel Ogunleke, 2022.
"""
    prompt = "CMDTube> "
    search_query = ""
    search_results = None
    ARGUMENTS = ["search", "download"]
    recently_searched = False

    def do_exit(self, arg):
        print("Goodbye...see you again!")
        raise SystemExit

    def progress_func(self):
        pass
        #for i in tqdm (range (100), desc="Getting results ready...", ascii=False, ncols=75):
        #    time.sleep(0.01)

    def complete_func(self):
        pass #print("Loaded!")

    def search_youtube(self, search_query, results):
        try:
            self.search_results = YoutubeSearch(search_query, max_results=results).to_dict()
            print("Please wait...")
            time.sleep(0.01)
            for i in tqdm (range (100), desc="Getting results ready...", ascii=False, ncols=75, colour="green"):
                time.sleep(0.01)
            time.sleep(0.5)
            print("================================"+("="*len(search_query)))
            print(f"Here are top {results} results for `{search_query}`:")
            print("================================"+("="*len(search_query)))
            for idx, res in enumerate(self.search_results):
                print(f"{idx+1}: {res['title']}\n   {res['channel']+' • '+res['views']+' • '+res['publish_time']}\n")
            print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Make sure you have a stable internet connection", "yellow"))

    def watch_video_from_searched(self, index):
        link = "https://www.youtube.com/"+self.search_results[index-1]["url_suffix"]
        print(f"Opening {self.search_results[index-1]['title']} on your browser...")
        webbrowser.open(link)
        print(termcolor.colored("Done!", "green"))

    def watch_video(self, url):
        if url.startswith("https://youtube.com") or \
            url.startswith("https://www.youtube.com") or \
            url.startswith("http://youtube.com") or \
            url.startswith("http://www.youtube.com") or \
            url.startswith("youtube.com"):
            print(f"Opening {url} on your browser...")
            webbrowser.open(url)
            print(termcolor.colored("Done!", "green"))
        else:
            print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))

    def download_video_from_searched(self, index):
        try:
            link = "https://www.youtube.com/"+self.search_results[index-1]["url_suffix"]
            download = YouTube(link)
            print(f"Downloading {self.search_results[index-1]['title']} with the highest resolution...")
            download.streams.get_highest_resolution().first().download()
            print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Make sure you have a stable internet connection", "yellow"))

    def download_video(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                download = YouTube(url)
                print("Downloading: ", download.title, "...")
                download.streams.get_highest_resolution().first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
            else:
                print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_video_w_format(self, url, format):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                download = YouTube(url)
                download.streams.filter(file_extension=format).first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_video_w_format_n_resolution(self, url, format, resolution):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                download = YouTube(url)
                if resolution == "highest":
                    download.streams.get_highest_resolution().first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
                elif resolution == "lowest":
                    download.streams.get_lowest_resolution().first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
                else:
                    download.streams.filter(file_extension=format, resolution=resolution).first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_playlist(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                p = Playlist(url)
                for video in p.videos:
                    video.streams.get_highest_resolution().first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_playlist_w_format(self, url, format):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                p = Playlist(url)
                for video in p.videos:
                    video.streams.filter(file_extension=format).first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_playlist_w_format_n_resolution(self, url, format, resolution):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                p = Playlist(url)
                if resolution == "highest":
                    for video in p.videos:
                        video.streams.get_highest_resolution().first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
                elif resolution == "lowest":
                    for video in p.videos:
                        video.streams.get_lowest_resolution().first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
                else:
                    for video in p.videos:
                        video.streams.filter(file_extension=format, resolution=resolution).first().download(filename_prefix="cmdtube-")
                    print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def video_info(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                vid = YouTube(url)
                print("Getting video info...")
                time.sleep(1)
                print(f"Title: {vid.title}\nViews: {vid.views} o Publish Date: {vid.publish_date} o Length: {vid.length}\nAuthor: {vid.author} o Keywords: {vid.keywords}\nChannel URL: {vid.channel_url}\nDescription: {vid.description}")
                print(termcolor.colored("Done!", "green"))
            else:
                print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Check your command and try again"))

    def video_info_from_searched(self, index):
        link = "https://www.youtube.com/"+self.search_results[index-1]["url_suffix"]
        vid = YouTube(link)
        print("Getting video info...")
        time.sleep(1)
        print(f"Title: {vid.title}\nViews: {vid.views} o Publish Date: {vid.publish_date} o Length: {vid.length}\nAuthor: {vid.author} o Keywords: {vid.keywords}\nChannel URL: {vid.channel_url}\nDescription: {vid.description}")
        print(termcolor.colored("Done!", "green"))

    def download_video_as_audio(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                video = YouTube(url)
                video.streams.get_audio_only().first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_playlist_as_audio(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("http://youtube.com") or \
                url.startswith("http://www.youtube.com") or \
                url.startswith("youtube.com"):
                p = Playlist(url)
                for video in p.videos:
                    video.streams.get_audio_only().first().download(filename_prefix="cmdtube-")
                print(termcolor.colored("Done!", "green"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))


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
6. Download a YouTube video as an audio

Available Commands
=================
"""
        try:
            parameters = ["-search", "-download", "-type", "-watch", "-resolution", "-format",
                          "-results", "-s", "-d", "-t", "-w", "-res", "-f", "-r", "-i", "-info"]
            for ar in arg.split():
                if ar in parameters:
                    arg = arg.replace(ar+" ", ar+"*").replace(" "+ar, "*"+ar)
            if "|" in arg:
                arg = arg.replace(" | ", "*|*")

            query = arg.split('*')

            if query[0].lower() == "-search" or query[0].lower() == "-s":
                if len(query) == 2:
                    #print("Searching YouTube for "+"`"+query[1]+"`")
                    self.search_youtube(query[1], 10)
                elif len(query) == 4:
                    #print(query)
                    if query[-2].lower() == "-results" or query[-2].lower() == "-r":
                        if query[-1].isdigit():
                            number_of_results_to_display = int(query[-1])
                            #print("Searching YouTube for "+"`"+query[1]+"`")
                            self.search_youtube(query[1], number_of_results_to_display)
                        else:
                            print(termcolor.colored("Invalid value for -results parameter", "red"))
                    else:
                        print(termcolor.colored(f"Invalid parameter: `{query[-2]}`", "red"))

                elif len(query) == 6:
                    if query[2] == "|":
                        if query[3].lower() == "cmdtube":
                            if query[4].lower() == "-watch" or query[4].lower() == "-w":
                                if query[5].isdigit():
                                    self.search_youtube(query[1], 10)
                                    if int(query[5]) < len(self.search_results):
                                        #print("Opening video in default web browser...")
                                        self.watch_video_from_searched(int(query[5]))
                            elif query[4].lower() == "-download" or query[4].lower() == "-d":
                                if query[5].isdigit():
                                    self.search_youtube(query[1], 10)
                                    if query[5] < len(self.search_results):
                                        #print("Downloading video in highest resolution...")
                                        self.download_video_from_searched(int(query[5]))
                                else:
                                    print(termcolor.colored(f"Invalid value for -download parameter: `{query[5]}`", "red"))
                            elif query[4].lower() == "-info" or query[4].lower() == "-i":
                                if query[5].isdigit():
                                    self.search_youtube(query[1], 10)
                                    if query[5] < len(self.search_results):
                                        #print("Downloading video in highest resolution...")
                                        self.video_info_from_searched(int(query[5]))
                                else:
                                    print(termcolor.colored(f"Invalid value for -info parameter: `{query[5]}`", "red"))
                            else:
                                print(termcolor.colored(f"Invalid parameter: `{query[4]}`", "red"))
                        else:
                            print(termcolor.colored(f"SyntaxError: `{query[3]}`\nDid you mean `cmdtube`?", "red"))
                    else:
                        print(termcolor.colored(f"SyntaxError: `{query[2]}`\nDid you mean `|`?", "red"))

                elif len(query) == 8:
                    if query[2].lower() == "-results" or query[2].lower() == "-r":
                        if query[3].isdigit():
                            number_of_results_to_display = int(query[3])
                            #print("Searching YouTube for "+"`"+query[1]+"`")
                            if query[4] == "|":
                                if query[5].lower() == "cmdtube":
                                    if query[6].lower() == "-watch" or query[6].lower() == "-w":
                                        if query[7].isdigit():
                                            self.search_youtube(query[1], number_of_results_to_display)
                                            if int(query[7]) < len(self.search_results):
                                                #print("Opening video in default web browser...")
                                                self.watch_video_from_searched(int(query[7]))
                                        else:
                                            print(termcolor.colored(f"Invalid value for -watch parameter: `{query[7]}`", "red"))

                                    elif query[6].lower() == "-download" or query[6].lower() == "-d":
                                        if query[7].isdigit():
                                            self.search_youtube(query[1], number_of_results_to_display)
                                            if int(query[7]) < len(self.search_results):
                                                #print("Downloading video in highest resolution...")
                                                self.download_video_from_searched(int(query[7]))
                                        else:
                                            print(termcolor.colored(f"Invalid value for -download parameter: `{query[7]}`", "red"))
                                    elif query[6].lower() == "-info" or query[6].lower() == "-i":
                                        if query[7].isdigit():
                                            self.search_youtube(query[1], 10)
                                            if int(query[7]) < len(self.search_results):
                                                #print("Downloading video in highest resolution...")
                                                self.video_info_from_searched(int(query[5]))
                                        else:
                                            print(termcolor.colored(f"Invalid value for -info parameter: `{query[5]}`", "red"))


                                else:
                                    print(termcolor.colored(f"SyntaxError: `{query[5]}`\nDid you mean `cmdtube`?", "red"))
                            else:
                                print(termcolor.colored(f"SyntaxError: `{query[4]}`\nDid you mean `|`?", "red"))
                        else:
                            print(termcolor.colored(f"Invalid value for -results parameter: `{query[3]}`", "red"))
                    else:
                        print(termcolor.colored(f"Invalid parameter: `{query[-2]}`", "red"))

            elif query[0] == "-watch" or query[0] == "-w":
                if len(query) == 2:
                    if query[1].startswith("https://youtube.com") or \
                        query[1].startswith("https://www.youtube.com") or \
                        query[1].startswith("http://youtube.com") or \
                        query[1].startswith("http://www.youtube.com") or \
                        query[1].startswith("youtube.com"):
                        #print("Opening video in default web browser...")
                        self.watch_video(query[1])
                else:
                    print(termcolor.colored(f"SyntaxError: It seems you have added unwanted information", "red"))
            elif query[0] == "-download" or query[0] == "-d":
                available_resolutions = ["720p", "480p", "360p", "144p", "240p", "1080p"]
                if len(query) == 4:
                    if query[2].lower() == "-type" or query[2].lower() == "-t":
                        if query[3].lower() == "video":
                            #print("Downloading video...")
                            self.download_video(query[1])
                        elif query[3].lower() == "playlist":
                            #print("Downloading playlist...")
                            self.download_playlist(query[1])
                        elif query[3].lower() == "playlist-audio":
                            #print("Downloading playlist...")
                            self.download_playlist_as_audio(query[1])
                        elif query[3].lower() == "audio":
                            #print("Downloading as mp4 audio...")
                            self.download_video_as_audio(query[1])
                        else:
                            print(termcolor.colored("Error: Invalid value for -type parameter\nDid you mean `video` or `playlist` or `audio` or `playlist-audio`?", "red"))
                    else:
                        if query[2].lower() in parameters:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                        else:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` does not exist", "red"))
                elif len(query) == 6:
                    if query[2].lower() == "-type" or query[2].lower() == "-t":
                        if query[3].lower() == "video":
                            if query[4].lower() == "-format" or query[4].lower() == "-f":
                                if query[5].lower() in ("mp4", "3gp"):
                                    self.download_video_w_format(query[1], query[5])
                                else:
                                    print(termcolor.colored(f"FormatError: Invalid value for -format. Can only be one of ['mp4', '3gp', 'mp3']", "red"))
                        elif query[3].lower() == "playlist":
                            #print("Downloading playlist...")
                            if query[4].lower() == "-format" or query[4].lower() == "-f":
                                if query[5].lower() in ("mp4", "3gp"):
                                    self.download_playlist_w_format(query[1], query[5])
                                else:
                                    print(termcolor.colored(f"FormatError: Invalid value for -format. Can only be one of ['mp4', '3gp', 'mp3']", "red"))
                        else:
                            print(termcolor.colored("Error: Invalid value for -type parameter\nDid you mean `video` or `playlist`?", "red"))


                    else:
                        if query[2] in parameters:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                        else:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` does not exist", "red"))
                elif len(query) == 8:
                    if query[2].lower() == "-type" or query[2].lower() == "-t":
                        if query[3].lower() == "video":
                            if query[4].lower() == "-format" or query[4].lower() == "-f":
                                if query[5].lower() in ("mp4", "3gp"):
                                    if query[6].lower() == "-resolution" or \
                                        query[6].lower() == "-res":
                                        if query[7].lower() in available_resolutions:
                                            #print(f"Downloading mp4 video with {query[7]} resolution...")
                                            self.download_video_w_format_n_resolution(query[1], query[5], query[7])
                                        else:
                                            print(termcolor.colored(f"ResolutionError: Invalid value for -resolution, can be one of {available_resolutions}", "red"))
                                    else:
                                        if query[6].lower() in parameters:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                                        else:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` does not exist", "red"))
                                else:
                                    print(termcolor.colored("Invalid format, can only be one of ['mp4', '3gp']", "red"))
                            else:
                                if query[4].lower() in parameters:
                                    print(termcolor.colored(f"ParameterError: Parameter `{query[4]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                                else:
                                    print(termcolor.colored(f"ParameterError: Parameter `{query[4]}` does not exist", "red"))

                        elif query[3].lower() == "playlist":
                            print("Downloading playlist...")
                            if query[4].lower() == "-format" or query[4] == "-f":
                                if query[5].lower() == "mp4":
                                    if query[6].lower() == "-resolution" or \
                                        query[6].lower() == "-res":
                                        if query[7].lower() in available_resolutions:
                                            print(f"Downloading mp4 video with {query[7]} resolution...")
                                        else:
                                            print(termcolor.colored(f"ResolutionError: Invalid value for -resolution, can be one of {available_resolutions}", "red"))
                                    else:
                                        if query[6].lower() in parameters:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                                        else:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` does not exist", "red"))

                                elif query[5].lower() == "3gp":
                                    if query[6].lower() == "-resolution" or \
                                        query[6].lower() == "-res":
                                        if query[7].lower() in available_resolutions:
                                            print(f"Downloading 3gp video with {query[7]} resolution...")
                                        else:
                                            print(termcolor.colored(f"ResolutionError: Invalid value for -resolution, can be one of {available_resolutions}", "red"))
                                    else:
                                        if query[6].lower() in parameters:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                                        else:
                                            print(termcolor.colored(f"ParameterError: Parameter `{query[6]}` does not exist", "red"))

                                else:
                                    print(termcolor.colored(f"FormatError: Invalid value for -format. Can only be one of ['mp4', '3gp']", "red"))
                            else:
                                if query[4].lower() in parameters:
                                    print(termcolor.colored(f"ParameterError: Parameter `{query[4]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                                else:
                                    print(termcolor.colored(f"ParameterError: Parameter `{query[4]}` does not exist", "red"))
                        else:
                            print(termcolor.colored("Error: Invalid value for -type parameter\nDid you mean `video` or `playlist`?", "red"))
                    else:
                        if query[2] in parameters:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` is at the wrong position.\nDid you mean `-type`?", "red"))
                        else:
                            print(termcolor.colored(f"ParameterError: Parameter `{query[2]}` does not exist", "red"))

            elif query[0] == "-info" or query[0] == "-i":
                if len(query) == 2:
                    if query[1].startswith("https://youtube.com") or \
                        query[1].startswith("https://www.youtube.com") or \
                        query[1].startswith("http://youtube.com") or \
                        query[1].startswith("http://www.youtube.com") or \
                        query[1].startswith("youtube.com"):
                        #print("Opening video in default web browser...")
                        self.video_info(query[1])
                else:
                    print(termcolor.colored(f"SyntaxError: It seems you have added unwanted information", "red"))
            else:
                print(termcolor.colored(f"ParameterError: Parameter `{query[0]}` does not exist", "red"))



        except:
            print("Quitting job...")
            raise SystemExit

def main():
    while True:
        game = cli().cmdloop()


if __name__ == "__main__":
    main()
