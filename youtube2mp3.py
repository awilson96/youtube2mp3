from __future__ import unicode_literals
import yt_dlp as youtube_dl
from mutagen.mp3 import MP3
import os

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

    def calculate_total_music_duration(self, directory):
        """Calculate total duration of all mp3 files in a directory and print in hours, minutes, and seconds"""
        total_duration = 0  # total duration in seconds

        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".mp3"):
                file_path = os.path.join(directory, filename)
                
                # Use mutagen to get the duration of the mp3 file
                audio = MP3(file_path)
                total_duration += audio.info.length

        # Convert total seconds to hours, minutes, and seconds
        hours, remainder = divmod(total_duration, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Total music duration in {directory}: \t\t{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
        return total_duration

        
if __name__ == "__main__":
    yt = Youtube2Mp3()
    yt.youtube2mp3()


