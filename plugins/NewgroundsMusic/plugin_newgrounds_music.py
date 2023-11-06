import requests

def download_newgrounds_music_by_id(track_id, output_path):
    base_url = "https://www.newgrounds.com/audio/download/"
    url = f"{base_url}{track_id}"

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"Downloaded track {track_id} to {output_path}")

if __name__ == "__main__":
    track_id = "1237698"
    output_path = "output.mp3"
    download_newgrounds_music_by_id(track_id, output_path)