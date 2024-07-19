from yt_dlp import YoutubeDL
from io import BytesIO
import os
from pathlib import Path
import random
import string

# only works in production
file_path = Path(__file__).resolve()
parent_directory = file_path.parent
# print(parent_directory)
# print(str(parent_directory.parent) + "/store_temp")
class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    # prints the progress of the download
    # print(d['_percent_str'])
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

def yt_download(link, format, quality="best"):
    link = [link]
    # youtube-dl quality options:
    # option from function that calls this function
    #
    # best: Select the best quality format represented by a single file with video and audio.
    # worst: Select the worst quality format represented by a single file with video and audio.
    # bestvideo: Select the best quality video-only format (e.g. DASH video).
    # worstvideo: Select the worst quality video-only format.
    # bestaudio: Select the best quality audio only-format.
    # worstaudio: Select the worst quality audio only-format.
    # bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio: Select the best quality video format (priority: mp4 container and H.264 video codec) and the best quality audio format (priority: m4a container and AAC audio codec).
    # bestvideo[height<=?1080]+bestaudio/best[height<=?1080]: Select the best quality video format (priority: height of 1080 or less and H.264 video codec) and the best quality audio format.
    # bestvideo[height<=?720]+bestaudio/best[height<=?720]: Select the best quality video format (priority: height of 720 or less and H.264 video codec) and the best quality audio format.
    # bestvideo[height<=?480]+bestaudio/best[height<=?480]: Select the best quality video format (priority: height of 480 or less and H.264 video codec) and the best quality audio format.
    # select the best quality video format priority mp4 and height of 1080 or less and H.264 video codec and the best quality audio format priority m4a and AAC audio codec
    # bestvideo[ext=mp4][height<=?1080]+bestaudio[ext=m4a]/best[height<=?1080]: Select the best quality video format (priority: mp4 container, H.264 video codec and height of 1080 or less) and the best quality audio format (priority: m4a container and AAC audio codec).
    
    # generate a random string to use as the file name
    rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    if format == "audio":
        ydl_options = {
            'path': 'othertools/store_temp', 
            'format': 'bestaudio',
            'audioformat': "mp3",
            'extension': 'mp3',
            'outtmpl': str(parent_directory.parent) + "/store_temp/" + str(rand_string) + '.%(ext)s',
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': False,
            'default_search': 'auto',
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': "mp3",
            }],
        }
    elif format == "video":
        print(quality)
        vidquality = "best"
        # video quality based on pixel height
        if quality == "best":
            vidquality += ""
        elif quality == "1080":
            vidquality += "[height<=1080]"
        elif quality == "720":
            vidquality += "[height<=720]"
        elif quality == "480":
            vidquality += "[height<=480]"
        elif quality == "360":
            vidquality += "[height<=360]"
        elif quality == "240":
            vidquality += "[height<=240]"
        else:
            return "ERROR: INVALID QUALITY"
        
        ydl_options = {
            'path': 'othertools/store_temp',
            'format': vidquality,
            'videoformat': 'mp4',
            'extension': 'mp4',
            'outtmpl': str(parent_directory.parent) + "/store_temp/" + str(rand_string) + '.%(ext)s',
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': False,
            'default_search': 'auto',
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': "mp4",
            }],
        }
    
    print(ydl_options, link)

    with YoutubeDL(ydl_options) as ydl:
        ydl.download(link)
        info = ydl.extract_info(link[0], download=False)
        file_path = ydl.prepare_filename(info).split(".")[0] + "." + ydl_options["extension"]
        # print(file_path)
        video_title = info.get('title', None)

    if format == "audio":
        video_title = video_title + ".mp3"
    elif format == "video":
        video_title = video_title + ".mp4"
    
    # print(video_title)
    # file_name2 = Path(file_path)
    # print("FILE NAME 2",file_name2)
    # with open(file_path, "rb") as f:
    #     data = BytesIO(f.read())
    
    # deprecated, file is deleted in the view using the FileCleanupResponse class which is a subclass of FileResponse
    # try:
    #     os.remove(file_path)
    #     print("DELETED FILE")
    # except Exception as e:
    #     print(e)
    #     # raise Exception("FAILED TO DELETE FILE")
    #     print("FAILED TO DELETE FILE")
    # # print(file_path)
    
    return file_path, video_title

# yt_download("https://www.youtube.com/watch?v=rQxrWxSV9z0","video","480")