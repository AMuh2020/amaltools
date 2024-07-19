from io import BytesIO
from moviepy.editor import *
import tempfile

#Install moviepy
# Load the mp4 file from memory
def mp4TOmp3(buffer):
    # local
    # with tempfile.NamedTemporaryFile(mode='wb', suffix='.mp4', dir="C:/Users/leasu/Desktop/programming/workspace/web/WebTools/AMALTools_app/fileconverters/store_temp") as vid_file, tempfile.NamedTemporaryFile(mode='wb', suffix='.mp3', delete=False, dir="C:/Users/leasu/Desktop/programming/workspace/web/WebTools/AMALTools_app/fileconverters/store_temp") as audio_file:
    #  server
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.mp4',delete=False ,dir="fileconverters/store_temp") as vid_file, tempfile.NamedTemporaryFile(mode='wb', suffix='.mp3', delete=False, dir="fileconverters/store_temp") as audio_file:
    # with open("fileconverters/store_temp/temp_vid.mp4", 'wb') as vid_file, open("fileconverters/store_temp/temp_audio.mp3", 'wb') as audio_file:
        for chunk in buffer.chunks():
            vid_file.write(chunk)
        
        print(vid_file)
        print(vid_file.name)
        video = VideoFileClip(filename=vid_file.name)
        vid_file.close()
    
        print(type(video))
        # Extract audio from video in memory
        audio_array = video.audio
        # vid_file.close()
        
        # gets the file name without the extension
        fn_split = buffer.name.split('.')
        print(fn_split)
        fn=[]
        print(type(audio_file))
        print(audio_file)
        print(audio_file.name)
        
        #des2.close()
        # audio_file = tempfile.NamedTemporaryFile(mode='wb', suffix='.mp3', delete=True, dir="C:/Users/leasu/Desktop/programming/workspace/web/WebTools/AMALTools_app/fileconverters/store_temp")
        audio_array.write_audiofile(filename=audio_file.name)

        
        with open(audio_file.name, 'rb') as f:
            audio2 = BytesIO(f.read())

        
        print(type(audio2))
        print(audio2)
    try:
        vid_file.close()
        audio_file.close()
        # print(vid_file.name)
        os.remove(vid_file.name)
        os.remove(audio_file.name)
        print("DELETED FILE")
    except Exception as e:
        print(e)
        # raise Exception("FAILED TO DELETE FILE")
        print("FAILED TO DELETE FILE")
    return audio2
    
    # Delete the temporary files (not working might be a windows only issue): It was a windows only issue
    try:
        os.remove(vid_file.name)
        print("DELETED FILE")
    except Exception as e:
        print(e)
        # raise Exception("FAILED TO DELETE FILE")
        print("FAILED TO DELETE FILE")
            
    

#start again, write to an actual file, save until tab closed
# WORKED IT OUT, FILE INSTANTLY DOWNLOADED ON USER SIDE USING FILE RESPONSE