import os
import sys
import re
from yt_dlp import YoutubeDL

def validate_url(url):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
    return bool(youtube_regex.match(url))

def download_mp3(link, output_directory="downloads"):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading audio from: {link}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }
            ],
            'postprocessor_args': [
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-b:a', '192k',
                '-strict', 'experimental',
            ],
            'merge_output_format': 'mp4',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"MP4 saved in: {output_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No YouTube link provided.")
        print("Usage: python YouTube_MP3.py <YouTube URL>")
        sys.exit(1)

    youtube_link = sys.argv[1].strip()

    if not validate_url(youtube_link):
        print("Error: The provided link is not a valid YouTube URL.")
        sys.exit(1)

    download_mp3(youtube_link)
