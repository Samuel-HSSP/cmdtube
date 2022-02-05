# CmdTube
![CmdTube Logo](https://i.ibb.co/DGjDpph/cmdtubelogo.png)

CmdTube is a Python CLI library for searching, downloading, and watching YouTube tutorials.
This library was made with programmers in mind and it's dedicated to every programmer
who watches YouTube videos to become better.


## Table of Contents
##### 1. Installation
##### 2. Features
##### 3. Usage
          3.1. Watch YouTube Videos
          3.2. Get Information about a YouTube Video
          3.3. Search YouTube Videos
          3.4. Download YouTube Videos and Playlists
##### 4. To-Do
##### 5. Other Libraries


## Installation
Use pip/pip3 to install from PyPI
```
$ pip install cmdtube
```
You can also use Python from your command prompt
```
$ python -m pip install cmdtube
```


## Features
1. Search for a YouTube video
2. Watch a YouTube video on your browser
3. Download a YouTube video
4. Download a YouTube playlist
5. Get information about a YouTube video
6. Download a YouTube video as an audio

## Usage
With CmdTube, you can download any YouTube programming tutorial you want, over a few commands.
The following section of the documentation is to guide you on how to use CmdTube.

### Watch YouTube Videos
To watch a YouTube video from your default web browser, use the following syntax:
```
Usage: cmdtube [-w WATCH_URL]

Positional argument:
  -s WATCH_URL, -watch WATCH_URL
                        open YouTube video url (WATCH) in default browser
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
  -i INFO, -info INFO
                        get information about the video using its URL.
```


### Search YouTube Videos
To search YouTube for videos, use the following syntax:
```
Usage: cmdtube [-s SEARCH_QUERY] [-r RESULTS]

Positional arguments:
  -s SEARCH_QUERY, -search SEARCH_QUERY
                        search YouTube for desired query

optional arguments:
  -r RESULTS, --results RESULTS
                        The maximum number of results to display.
                        For now, the default value is 10 and maximum is 19.
```
You can also use the pipeline feature to watch a video from the search results.
```
Usage: cmdtube [-s SEARCH_QUERY] [-r RESULTS] | cmdtube [-w WATCH]

Positional arguments:
  -s SEARCH_QUERY, -search SEARCH_QUERY
                        search YouTube for desired query
  -w WATCH, -watch WATCH
                        the index of the video to watch, from the displayed
                        search result. It should not be more than the total
                        number of videos from the search result.
                        To watch the first video, use 1.
Optional arguments:
  -r RESULTS, --results RESULTS
                        The maximum number of results to display.
                        This determines the index of the video to download. It
                        must not be greater than the maximum number of results.
                        For now, the default value is 10 and maximum is 19
```
If you want to download a video from the search results, follow the syntax below:
```
Usage: cmdtube [-s SEARCH_QUERY] [-r RESULTS] | cmdtube [-d DOWNLOAD]

Positional arguments:
  -s SEARCH_QUERY, -search SEARCH_QUERY
                        search YouTube for desired query
  -d DOWNLOAD, -download DOWNLOAD
                        the index of the video to download, from the displayed
                        search result. It should not be more than the total
                        number of videos from the search result.
                        To download the first video, use 1.
                        Note that it will always download the highest resolution
                        of the video. More functionalities will be added later.
Optional arguments:
  -r RESULTS, --results RESULTS
                        The maximum number of results to display.
                        This determines the index of the video to download. It
                        must not be greater than the maximum number of results.
                        For now, the default value is 10 and maximum is 19
```
Finally, you can get the information about a video from the list of search results.
```
Usage: cmdtube [-s SEARCH_QUERY] [-r RESULTS] | cmdtube [-i INFO]

Positional arguments:
  -s SEARCH_QUERY, -search SEARCH_QUERY
                        search YouTube for desired query
  -d INFO, -info INFO
                        the index of the video from the displayed
                        search result. It should not be more than the total
                        number of videos from the search result.
                        To get information about the second video shown in the
                        search result, use 2.

Optional arguments:
  -r RESULTS, --results RESULTS
                        The maximum number of results to display.
                        This determines the index of the video to download. It
                        must not be greater than the maximum number of results.
                        For now, the default value is 10 and maximum is 19
```


### Download YouTube Videos and Playlists
To download a YouTube video or playlist into the current working directory, follow the syntax below:
```
Usage: cmdtube [-d DOWNLOAD] [-t TYPE] [-f FORMAT] [-res RESOLUTION]

Positional arguments:
  -d DOWNLOAD, -download DOWNLOAD
                        URL for video or playlist to download
  -t TYPE, -type TYPE
                        could be either `video` or `playlist`

Optional arguments:
  -f FORMAT, -format FORMAT
                        video format to download. Could be one of `mp4` and `3gp`.
                        More video formats will be supported in future versions
                        By default, it will download the mp4 format.
  -res RESOLUTION, -resolution RESOLUTION
                        resolution of the video to download.
                        Ex: 360p, 480p, 720p, 1080p, highest, lowest
                        If highest, it will download the video in the highest resolution.
                        Otherwise (if lowest), it will download the video in the lowest
                        resolution.
                        By default, it downloads the video in the highest resolution.
```
You can also download a single video or all the videos in a playlist as audio.
```
Usage: cmdtube [-d DOWNLOAD] [-t TYPE]

Positional arguments:
  -d DOWNLOAD, -download DOWNLOAD
                        URL for video or playlist to download
  -t TYPE, -type TYPE
                        must either be `audio` or `playlist-audio` here
```


### To-Do
- [ ] Download files to specified paths
- [ ] Show progress bars for videos downloading
- [ ] Show more information about commands
- [ ] Proper documentation
- [ ] Command to show full/minimal information about a video
- [ ] Save command output to text file
- [ ] Download captions for videos
- [ ] Add support for more video and audio formats
- [ ] Fix all the bugs, and probably add more


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

PS: This is my first Python library I launched on my birthday, it's not perfect! :)
