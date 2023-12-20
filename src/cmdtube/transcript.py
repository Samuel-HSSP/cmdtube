import argparse, webbrowser, shlex, termcolor, time
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from youtube_transcript_api.formatters import SRTFormatter

class Transcript:
    def __init__(self, query, search_results=None):
        self.query = query
        self.search_results = search_results
    
        parser = argparse.ArgumentParser(
            prog="cmdtube",
        )

        parser.add_argument("-t", "--transcript", type=self.url_or_number, help="The index of the video from the list of search results OR the URL of the video")
        parser.add_argument("-l", "--language", type=str, help="The abbreviated language of the transcript you'd like to download. Ex: 'en' for English")
        parser.add_argument("--show-list", action='store_const', const=True, default=False, help="This flag, if set, lists all the available transcripts")

        args = parser.parse_args(shlex.split(self.query))

        if isinstance(args.transcript, int):
            self.video_transcript_from_searched(
                self.search_results,
                args.transcript,
                args.language,
                args.show_list
            )
        elif isinstance(args.transcript, str):
            self.video_transcript(args.transcript, args.language, args.show_list)
    
    def url_or_number(self, arg):
        if arg.isdigit():
            return int(arg)
        else:
            return arg

    def video_transcript(self, url, lang='en', list_transcripts=False):
        try:
            if lang is None:
                lang = 'en' #default
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("youtube.com"):

                vid = YouTube(url)
                formatter = SRTFormatter()

                url_suffix = vid.watch_url.split("/watch?v=")[-1]
                print(f"Getting video transcripts for `{url_suffix}`...")
                time.sleep(1)
                print(termcolor.colored("Done!", "green"))
                print("\n")

                if list_transcripts:
                    srt = YouTubeTranscriptApi.list_transcripts(
                        url_suffix
                    )
                    print("=====================================\nAvailable Transcripts\n=====================================\n", f"Video Title: {vid.title}")
                    print("\n", srt)
                
                transcript_list = YouTubeTranscriptApi.list_transcripts(url_suffix)

                # iterate over all available transcripts
                for transcript in transcript_list:
                    if transcript.language_code == lang:
                        print(termcolor.colored(f"Found an original transcript for `{lang}`!", "green"))
                        srt_formatted = formatter.format_transcript(transcript.fetch())
                        with open(f'{vid.title}.srt', 'w', encoding='utf-8') as srt_file:
                            srt_file.write(srt_formatted)
                        print(termcolor.colored(f"Subtitle file saved as `(CMDTube)-{vid.title}.srt`", "green"), "\n")

                    elif transcript.language_code != lang:
                        print(termcolor.colored(f"Couldn't find an original transcript for `{lang}`!", "yellow"))
                        print(f"Translating the available transcript from `{transcript.language_code}` to `{lang}`")
                        # print(transcript.translate(lang).fetch())
                        srt_formatted = formatter.format_transcript(transcript.translate(lang).fetch())
                        with open(f'(CMDTube)-{vid.title}.srt', 'w', encoding='utf-8') as srt_file:
                            srt_file.write(srt_formatted)
                        print(termcolor.colored(f"Subtitle file saved as `(CMDTube)-{vid.title}.srt`", "green"), "\n")

            else:
                print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))
            
        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Check your command and try again"))

    def video_transcript_from_searched(self, search_results, index, lang='en', list_transcripts=False):
        link = "https://www.youtube.com/"+search_results[index-1]["url_suffix"]
        try:
            if lang is None:
                lang = 'en' #default

            vid = YouTube(link)
            formatter = SRTFormatter()

            url_suffix = vid.watch_url.split("/watch?v=")[-1]
            print(f"Getting video transcripts for `{url_suffix}`...")
            time.sleep(1)
            print(termcolor.colored("Done!", "green"))
            print("\n")

            if list_transcripts:
                srt = YouTubeTranscriptApi.list_transcripts(
                    url_suffix
                )
                print("=====================================\nAvailable Transcripts\n=====================================\n", f"Video Title: {vid.title}")
                print("\n", srt)
            
            transcript_list = YouTubeTranscriptApi.list_transcripts(url_suffix)

            # iterate over all available transcripts
            for transcript in transcript_list:
                if transcript.language_code == lang:
                    print(termcolor.colored(f"Found an original transcript for `{lang}`!", "green"))
                    srt_formatted = formatter.format_transcript(transcript.fetch())
                    with open(f'{vid.title}.srt', 'w', encoding='utf-8') as srt_file:
                        srt_file.write(srt_formatted)
                    print(termcolor.colored(f"Subtitle file saved as `(CMDTube)-{vid.title}.srt`", "green"), "\n")

                elif transcript.language_code != lang:
                    print(termcolor.colored(f"Couldn't find an original transcript for `{lang}`!", "yellow"))
                    print(f"Translating the available transcript from `{transcript.language_code}` to `{lang}`")
                    # print(transcript.translate(lang).fetch())
                    srt_formatted = formatter.format_transcript(transcript.translate(lang).fetch())
                    with open(f'(CMDTube)-{vid.title}.srt', 'w', encoding='utf-8') as srt_file:
                        srt_file.write(srt_formatted)
                    print(termcolor.colored(f"Subtitle file saved as `(CMDTube)-{vid.title}.srt`", "green"), "\n")

        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Check your command and try again"))
