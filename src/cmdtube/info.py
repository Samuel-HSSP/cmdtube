import argparse, shlex, webbrowser, termcolor, time
from pytube import YouTube

class Info:
    def __init__(self, query, search_results=None):
        self.query = query
        self.search_results = search_results
    
        parser = argparse.ArgumentParser(
            prog="cmdtube",
        )

        parser.add_argument("-i", "--info", type=self.url_or_number, help="The index of the video from the list of search results OR the URL of the video")

        args = parser.parse_args(shlex.split(self.query))

        if isinstance(args.info, int):
            self.video_info_from_searched(self.search_results, args.info)
        elif isinstance(args.info, str):
            self.video_info(args.info)

    def url_or_number(self, arg):
        if arg.isdigit():
            return int(arg)
        else:
            return arg

    def video_info(self, url):
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("youtube.com"):
                vid = YouTube(url)
                print(termcolor.colored("Getting video info...", "blue"))
                time.sleep(1)
                print(f"Title: {vid.title}\nVideo URL: {vid.watch_url}\nViews: {vid.views}\nPublish Date: {vid.publish_date}\nLength: {vid.length} seconds\nAuthor: {vid.author}\nKeywords: {vid.keywords}\nChannel URL: {vid.channel_url}\nDescription: {vid.description}")
                print(termcolor.colored("Done!", "green"))
                print("\n")
            else:
                print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Check your command and try again"))

    def video_info_from_searched(self, search_results, index):
        link = "https://www.youtube.com/"+search_results[index-1]["url_suffix"]
        vid = YouTube(link)
        print(termcolor.colored("Getting video info...", "blue"))
        print(f"Title: {vid.title}\nVideo URL: {vid.watch_url}\nViews: {vid.views}\nPublish Date: {vid.publish_date}\nLength: {vid.length}seconds\nAuthor: {vid.author}\nKeywords: {vid.keywords}\nChannel URL: {vid.channel_url}\nDescription: {vid.description}")
        print(termcolor.colored("Done!", "green"))
        print("\n")
