import argparse, shlex, webbrowser, termcolor

class Watch:
    def __init__(self, query, search_results=None):
        self.query = query
        self.search_results = search_results
        
        parser = argparse.ArgumentParser(
            prog="cmdtube",
        )

        parser.add_argument("-w", "--watch", type=self.url_or_number, help="The index of the video from the list of search results OR the URL of the video")

        args = parser.parse_args(shlex.split(self.query))

        if isinstance(args.watch, int):
            self.watch_video_from_searched(self.search_results, args.watch)
        elif isinstance(args.watch, str):
            self.watch_video(args.watch)

        print("Index of the video: ", args.watch)
    
    def url_or_number(self, arg):
        if arg.isdigit():
            return int(arg)
        else:
            return arg

    def watch_video_from_searched(self, search_results, index):
        link = "https://www.youtube.com/"+search_results[index-1]["url_suffix"]
        print(termcolor.colored(f"Opening {search_results[index-1]['title']} on your browser...", "white"))
        webbrowser.open(link)
        print(termcolor.colored("Done!", "green"))

    def watch_video(self, url):
        if url.startswith("https://youtube.com") or \
            url.startswith("https://www.youtube.com") or \
            url.startswith("youtube.com"):
            print(termcolor.colored(f"Opening {url} on your browser...", "white"))
            webbrowser.open(url)
            print(termcolor.colored("Done!", "green"))
        else:
            print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))