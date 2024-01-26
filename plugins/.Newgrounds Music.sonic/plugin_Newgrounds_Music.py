import requests
import os
from bs4 import BeautifulSoup


def get_newgrounds_music_title(track_id):
    url = f"https://www.newgrounds.com/audio/listen/{track_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")

    if title_tag:
        # Extract the title from the webpage title
        title = title_tag.text.split(" - Newgrounds.com")[0]
        return title

    return None


def download_newgrounds_music_by_id(track_id, output_dir="."):
    title = get_newgrounds_music_title(track_id)
    if title is None:
        print(f"Failed to get the title for track {track_id}")
        return

    base_url = "https://www.newgrounds.com/audio/download/"
    url = f"{base_url}{track_id}"
    output_path = os.path.join(output_dir, f"{title}.mp3")

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"Downloaded track {track_id} as '{title}.mp3'")


if __name__ == "__main__":
    track_id = "1237698"
    download_newgrounds_music_by_id(track_id)
