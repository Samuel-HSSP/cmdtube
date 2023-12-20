# CmdTube
![CmdTube Logo](https://i.ibb.co/DGjDpph/cmdtubelogo.png)

CmdTube is a Python CLI library for searching, downloading, and watching YouTube tutorials.
This library was made with programmers in mind and it's dedicated to every programmer
who watches YouTube videos to become better.
Please visit [here](https://github.com/SamuelHSSP/cmdtube) for a better documentation.


## Table of Contents
- [Installation](https://github.com/Samuel-HSSP/cmdtube/blob/main/README.md#installation)
- [Features](https://github.com/Samuel-HSSP/cmdtube/blob/main/README.md#features)
- [Usage](https://github.com/Samuel-HSSP/cmdtube/blob/main/README.md#usage)
- [To-Do](https://github.com/Samuel-HSSP/cmdtube/blob/main/README.md#to-do)
- [Other Libraries](https://github.com/Samuel-HSSP/cmdtube/blob/main/README.md#other-libraries)


## Installation
Use pip/pip3 to install from PyPI
```
$ pip install cmdtube
```
You can also use Python from your command prompt
```
$ python -m pip install cmdtube
```
Lastly, to install from GitHub (ensuring that Git has been added to PATH), do:
```
$ python -m pip install git+https://www.github.com/Samuel-HSSP/cmdtube
```


## Features
1. Search for a YouTube video
2. Get information about a YouTube video
3. Watch a YouTube video on your browser
4. Download a YouTube video
5. Download a YouTube playlist 
6. Download a YouTube video as audio
7. Download a whole YouTube playlist as audio
8. Download the captions/subtitles for any video in almost any language.

## Usage
With CmdTube, you can download any YouTube programming tutorial you want, over a few commands.
The following section of the documentation is to guide you on how to use CmdTube.
Here is how you should initialize cmdtube (then run the code file):
```python
>>> from cmdtube import cmdtube
...
# To search YouTube for 'How to debug without Stack Overflow' (I hope that's possible)
CMDTube> cmdtube -s "How to debug without Stack Overflow"
```

### Search YouTube Videos
To search YouTube for videos, use the following syntax:
```
Usage: cmdtube [-s SEARCH_QUERY] [-r RESULTS]

Positional arguments:
  -s SEARCH_QUERY (type: str)
                        Search YouTube for desired query. Make sure you put the
                        search query in quotes, else it wouldn't work.

Optional arguments:
  -r RESULTS (type: int)
                        The maximum number of results to display.
                        For now, the default value is 10 and maximum is 19.
```

```python
# The following command displays 5 results from the search.
CMDTube> cmdtube -s "How to make a robot at home" -r 5
```


### Get Information about a YouTube Video
To get information about a YouTube video, use the syntax given below.
This command returns the following information:
1. Title
2. Views
3. Publish Date
4. Length
5. Author
6. Keywords
7. Channel URL
8. Description
```
Usage: cmdtube [-i INFO]

Positional argument:
  -i INFO (type: str or int)
                        Get information about the video using its URL or the index of
                        the video from the list of videos from the search results.
                        Make sure to put the URL in quotes.
                        You can only use the index of the video, only after you've
                        once run a search command.

```
```python
# Gets the info about the third YouTube video from the search results
CMDTube> cmdtube -i 3

# Gets the info about the YouTube video via its link
CMDTube> cmdtube -i "https://www.youtube.com/watch?v=_nbVTUYVKxg"
```

### Watch a YouTube Video or Playlist from the browser
To watch any YouTube video on your default browser, use the following syntax:
```
Usage: cmdtube [-w WATCH]

Positional arguments:
  -w WATCH (type: str or int)
                        Watch a YouTube video with the URL or the index from
                        the search results. Make sure you put the URL in
                        quotes, else it wouldn't work.
                        You can only use the index of the video, only after you've
                        once run a search command.

```
```python
# Opens the second YouTube video from the search results on your browser
CMDTube> cmdtube -w 2

# Opens the YouTube video link on your browser
CMDTube> cmdtube -w "https://www.youtube.com/watch?v=_nbVTUYVKxg"
```

### Download YouTube Videos and Playlists
To download a YouTube video or playlist into the current working directory or a specified path,
follow the syntax below:
```
Usage: cmdtube [-d DOWNLOAD] [-t TYPE] [-p PATH] [-res RESOLUTION] [--audio AUDIO]

Positional arguments:
  -d DOWNLOAD
                        URL for video or playlist to download or the index of the 
                        video from the search results. Make sure you put the URL in
                        quotes, else it wouldn't work.
                        You can only use the index of the video, only after you've
                        once run a search command.

Optional arguments:
  -t TYPE (type: str)
                        Could either be "video" or "playlist". It's set to "video"
                        by default.

  -p PATH (type: str)
                        Path or directory to download the video into. If not set, it saves
                        the video (or audio) to the current working directory.
  
  -res RESOLUTION (type: str)
                        The resolution of the video to download.
                        Ex: "144p", "240p", "360p", "highest", "lowest"
                        If "highest", it will download the video in the highest resolution.
                        Otherwise (if "lowest"), it will download the video in the lowest
                        resolution.
                        By default, it downloads the video in 480p resolution.

  --audio AUDIO (no value)
                        This is a flag, which downloads the video or the whole playlist
                        as audio, if set.
                        Just add --audio to the end of your command and it will download
                        as audio. When downloading as audio, the resolution argument does
                        nothing.
```
```python
# Downloads the second YouTube video (from the search results) to the current directory in 480p
CMDTube> cmdtube -d 2

# Downloads all the videos in the playlist in 360p resolution
CMDTube> cmdtube -d "https://www.youtube.com/playlist?list=PLtIIVgC7Q8mAH9HFQJIEQ02rd7ndExDc8" -t "playlist" -res "360p"

# Downloads all the videos in the playlist as audio
CMDTube> cmdtube -d "https://www.youtube.com/playlist?list=PLtIIVgC7Q8mAH9HFQJIEQ02rd7ndExDc8" -t "playlist" --audio
```

### Download Transcripts for YouTube Videos
To download the transcript for any YouTube video in almost any language, follow the syntax below:
```
Usage: cmdtube [-t TRANSCRIPT] [-l LANGUAGE] [--show-list SHOW_LIST]

Positional arguments:
  -t TRANSCRIPT
                        URL for video transcript (YouTube video link) to download or the index of the 
                        video from the search results. Make sure you put the URL in quotes, else it
                        wouldn't work.
                        You can only use the index of the video, only after you've
                        once run a search command.

Optional arguments:
  -l LANGUAGE (type: str)
                        The language code of the transcript to download. The default language is "en".

  --show-list SHOW_LIST (no value)
                        This is a flag, which shows a list of available transcripts to download, if set.
                        It also shows the list of languages you can translate the transcript to.
                        Just add --show-list to the end of your command and it will show the 
                        required information alongside downloading the transcript in the language you set.
```
```python
# Downloads the transcript for the second YouTube video (from the search results)
CMDTube> cmdtube -t 2

# Downloads the transcript for the video and displays the available transcripts
CMDTube> cmdtube -t "https://www.youtube.com/watch?v=_nbVTUYVKxg" -l "fr" --show-list
```


### To-Do
- [*] Download files to specified paths
- [*] Show progress bars for videos downloading
- [*] Show more information about commands
- [*] Proper documentation
- [ ] Command to show full/minimal information about a video
- [ ] Save command output to text file
- [*] Download captions for videos
- [ ] Add support for more video and audio formats
- [*] Proper organization of code files
- [*] Fix all the bugs, and probably add more


### Other Libraries
[PyTube](https://pypi.org/project/pytube/) - Python 3 library for downloading YouTube Videos.
#### Installation
```
pip install pytube
```
[YoutubeSearch](https://pypi.org/project/youtube-search/) - Perform YouTube video searches without the API
#### Installation
```
pip install youtube-search
```
[YoutubeSearch](https://pypi.org/project/youtube-transcript-api/) - Get transcripts for YouTube videos
#### Installation
```
pip install youtube-transcript-api
```

PS: This is my first Python library I launched on my birthday, it's not perfect!
However, this is the second version released on Christmas day, so it's much better than the older version. :)
