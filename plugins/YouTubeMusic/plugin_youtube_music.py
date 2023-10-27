import yt_dlp
from random import randint

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title')

def download_video(url):
    video_title = False
    # video_title = get_video_info(url)
    if video_title:
        print(f"Downloading video: {video_title}")
    else:
        print("Video title not found.")
        video_title = f"unknown-{str(randint(100000000000, 999999999999))}"

    ydl_opts = {
        'outtmpl': f'%(title)s.mp3',
        'format': 'bestaudio',
        'extract_audio': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return video_title

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    video_title = download_video(video_url)
    print(f"Downloaded {video_title}")
