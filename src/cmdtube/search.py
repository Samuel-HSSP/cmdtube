import argparse, shlex, termcolor, time
from tqdm import tqdm
from youtube_search import YoutubeSearch

class Search:
    search_results = []

    def __init__(self, query):
        self.query = query
        parser = argparse.ArgumentParser(
            prog="cmdtube",
        )

        parser.add_argument("-s", "--search", type=str, help="A string argument of your search query")
        parser.add_argument("-r", "--results", type=int, help="The number of results to display")

        args = parser.parse_args(shlex.split(self.query))

        search = args.search
        results = args.results

        # print("Search query: ", search)
        # print("Results: ", results)
        self.search_youtube(search, results)

    def search_youtube(self, search_query, results):
        try:
            search_results = YoutubeSearch(search_query, max_results=results).to_dict()
            print("Please wait...")
            time.sleep(0.01)
            for i in tqdm (range (100), desc="Getting results ready...", ascii=False, ncols=75, colour="green"):
                time.sleep(0.01)
            time.sleep(0.5)
            print("================================"+("="*len(search_query)))
            print(f"Here are top {results} results for `{search_query}`:")
            print("================================"+("="*len(search_query)))
            for idx, res in enumerate(search_results):
                print(f"{idx+1}: {res['title']}\n   {res['channel']+' • '+res['views']+' • '+res['publish_time']}\n")
            print(termcolor.colored("Done!", "green"))
            self.search_results = search_results
        
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Make sure you have a stable internet connection", "yellow"))