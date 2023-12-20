import argparse, os, shlex, termcolor, time
from tqdm import tqdm
from youtube_search import YoutubeSearch
from pytube import YouTube, Playlist
from io import BytesIO
from threading import Thread

class Download:
    def __init__(self, query, search_results=None):
        self.query = query
        self.search_results = search_results
    
        parser = argparse.ArgumentParser(
            prog="cmdtube",
        )

        parser.add_argument("-d", "--download", type=self.url_or_number, help="The index of the video from the list of search results OR the URL of the video")
        parser.add_argument("-t", "--type", type=str, help="Whether it's a 'video' or 'playlist'.")
        parser.add_argument("-p", "--path", type=str, help="The path or directory where the video should be saved")
        parser.add_argument("-res", "--resolution", type=str, help="The resolution of the video(s) to download. Could be one of ('360p', '480p', '720p', '1080p', 'highest', 'lowest')")
        parser.add_argument("--audio", action='store_const', const=True, default=False, help="This flag, if set, downloads the YouTube video or playlist as an MP3 audio")

        args = parser.parse_args(shlex.split(self.query))

        if isinstance(args.download, int):
            self.download_video_from_searched(
                self.search_results,
                args.download,
                resolution=args.resolution,
                to_path=args.path,
                type=args.type,
                as_audio=args.audio,
            )
        elif isinstance(args.download, str):
            self.download_video(
                args.download,
                resolution=args.resolution, 
                to_path=args.path,
                type=args.type,
                as_audio=args.audio
            )
    
    def url_or_number(self, arg):
        if arg.isdigit():
            return int(arg)
        else:
            return arg

    def download_function(
                            self,
                            video,
                            resolution,
                            type,
                            to_path=None,
                            as_audio=False
                            ):
        if as_audio:
            audio_stream = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()
            file_path = os.path.join(to_path, f"(CMDTube)-{video.title}.mp3") \
                if to_path is not None else f"(CMDTube)-{video.title}.mp3"

            def on_complete(filepath):
                print(termcolor.colored(f"Audio file saved as: {filepath}", "green"))

            print(termcolor.colored(f"Downloading: {video.title}", "blue"))
            ### Na only God and ChatGPT understand this code block
            with tqdm(total=audio_stream.filesize, unit='B', unit_scale=True, ncols=100) as pbar:
                buffer = BytesIO()
                audio_stream.stream_to_buffer(buffer)
                buffer.seek(0)
                with open(file_path, 'wb') as f:
                    f.write(buffer.read())
                    # pbar.update(audio_stream.filesize)
                    Thread(target=pbar.update, args=(audio_stream.filesize,)).start()

            on_complete(file_path)
        else:
            if resolution not in ('highest', 'lowest'):
                video_stream = video.streams.filter(
                    only_video=True,
                    mime_type="video/mp4",
                    res=resolution,
                    file_extension="mp4"
                ).first()
            elif resolution == 'highest':
                video_stream = video.streams.filter(
                    only_video=True,
                    mime_type="video/mp4").get_highest_resolution()
            elif resolution == 'lowest':
                video_stream = video.streams.filter(
                    only_video=True,
                    mime_type="video/mp4").get_lowest_resolution()

            file_path = os.path.join(to_path, f"(CMDTube)-{video.title}.mp4") \
                if to_path is not None else f"(CMDTube)-{video.title}.mp4"

            def on_complete(filepath):
                print(termcolor.colored(f"Video file saved as: {filepath}", "green"))

            print(termcolor.colored(f"Downloading: {video.title}.mp4", "blue"))
            ### Na only God and ChatGPT understand this code block
            with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, ncols=100) as pbar:
                buffer = BytesIO()
                video_stream.stream_to_buffer(buffer)
                buffer.seek(0)
                with open(file_path, 'wb') as f:
                    f.write(buffer.read())
                    Thread(target=pbar.update, args=(video_stream.filesize,)).start()

            on_complete(file_path)

    # Video sample = https://www.youtube.com/watch?v=_nbVTUYVKxg&list=PLlbkyhAZrBl-XJQudaCfoMsGy_Jjau6HE&index=7&pp=iAQB
    # Playlist sample = https://www.youtube.com/playlist?list=PLtIIVgC7Q8mAH9HFQJIEQ02rd7ndExDc8
    def download_video(
                        self,
                        url,
                        resolution,
                        type,
                        to_path=None,
                        as_audio=False
                        ):
        if resolution is None:
            resolution = '480p'
        if type is None:
            type = 'video'
        try:
            if url.startswith("https://youtube.com") or \
                url.startswith("https://www.youtube.com") or \
                url.startswith("youtube.com"):

                if as_audio:
                    if type == 'video':
                        vid = YouTube(url)
                        self.download_function(vid, resolution, type, to_path, as_audio)
                    elif type == 'playlist':
                        print("You are downloading a WHOLE playlist as audio!")
                        playlist = Playlist(url)
                        print(f"The playlist has {playlist.length} videos")
                        for (i, video) in enumerate(playlist.videos):
                            print(termcolor.colored(f"Downloading {i+1} of {playlist.length} videos (as audio)", "blue"))
                            self.download_function(video, resolution, type, to_path, as_audio)

                else:
                    if type == 'video':
                        vid = YouTube(url)
                        download_function(vid, resolution, type, to_path, as_audio)
                    elif type == 'playlist':
                        print("You are downloading a WHOLE playlist!")
                        playlist = Playlist(url)
                        print(f"The playlist has {playlist.length} videos")
                        for (i, video) in enumerate(playlist.videos):
                            print(termcolor.colored(f"Downloading {i+1} of {playlist.length} videos", "blue"))
                            self.download_function(video, resolution, type, to_path, as_audio)
                print("Thanks for using CMDTube!")

            else:
                print(termcolor.colored("SyntaxError: Invalid URL, please input a correct YouTube URL", "red"))

        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Please try again", "yellow"))

    def download_video_from_searched(
                                    self,
                                    search_results,
                                    index,
                                    resolution,
                                    type,
                                    to_path=None,
                                    as_audio=False
                                    ):
        if resolution is None:
            resolution = '480p'
        if type is None:
            type = 'video'
        # try:
        print("Arguments: ", resolution, type, as_audio)

        try:
            link = "https://www.youtube.com/"+search_results[index-1]["url_suffix"]
            if as_audio:
                if type == 'video':
                    vid = YouTube(link)
                    self.download_function(vid, resolution, type, to_path, as_audio)
                elif type == 'playlist':
                    print("You are downloading a WHOLE playlist as audio!")
                    playlist = Playlist(link)
                    print(f"The playlist has {playlist.length} videos")
                    for (i, video) in enumerate(playlist.videos):
                        print(termcolor.colored(f"Downloading {i+1} of {playlist.length} videos (as audio)...", "blue"))
                        self.download_function(video, resolution, type, to_path, as_audio)

            else:
                if type == 'video':
                    vid = YouTube(link)
                    self.download_function(vid, resolution, type, to_path, as_audio)
                elif type == 'playlist':
                    print("You are downloading a WHOLE playlist!")
                    playlist = Playlist(url)
                    print(f"The playlist has {playlist.length} videos")
                    for (i, video) in enumerate(playlist.videos):
                        print(termcolor.colored(f"Downloading {i+1} of {playlist.length} videos", "blue"))
                        self.download_function(video, resolution, type, to_path, as_audio)
            print("Thanks for using CMDTube!")

        except Exception as e:
            print(termcolor.colored(f"{e}", "red"))
            print(termcolor.colored("Suggestion: Make sure you have a stable internet connection", "yellow"))