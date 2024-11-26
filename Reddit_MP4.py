import os
import sys
import re
from yt_dlp import YoutubeDL

def validate_url(url):
    reddit_regex = re.compile(r'(https?://)?(www\.)?reddit\.com/r/.+/comments/.+/.*|https?://v\.redd\.it/.*')
    return bool(reddit_regex.match(url))

def download_mp4(link, output_directory="downloads"):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading Reddit Video from: {link}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"MP4 saved in: {output_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No Reddit link provided.")
        print("Usage: python Reddit_MP4.py <Reddit URL>")
        sys.exit(1)

    reddit_link = sys.argv[1].strip()

    if not validate_url(reddit_link):
        print("Error: The provided link is not a valid Reddit URL.")
        sys.exit(1)

    download_mp4(reddit_link)
