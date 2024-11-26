import os
import sys
import re
from yt_dlp import YoutubeDL

def validate_url(url):
    tiktok_regex = re.compile(r'(https?://)?(www\.)?(m\.)?(vm\.)?tiktok\.com/.*')
    return bool(tiktok_regex.match(url))

def download_mp4(link, output_directory="downloads"):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading TikTok from: {link}")
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"MP4 saved in: {output_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No TikTok link provided.")
        print("Usage: python TikTok_MP4.py <TikTok URL>")
        sys.exit(1)

    tiktok_link = sys.argv[1].strip()

    if not validate_url(tiktok_link):
        print("Error: The provided link is not a valid TikTok URL.")
        sys.exit(1)

    download_mp4(tiktok_link)
