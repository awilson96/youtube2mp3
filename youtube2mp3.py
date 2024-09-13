from __future__ import unicode_literals
import yt_dlp as youtube_dl

class Youtube2Mp3:

    def __init__(self):
        pass

    def youtube2mp3(self):
        """Download an mp3 by providing the Youtube link"""
        print("Insert the link")
        link = input("")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        
if __name__ == "__main__":
    yt = Youtube2Mp3()
    yt.youtube2mp3()


