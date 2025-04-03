import os
import re
import unicodedata



def read_playlist(playlist_name: str, playlist_folder: str='playlists') -> list[str]:

    file = playlist_name if playlist_name.endswith('.txt') else playlist_name + '.txt'
    filepath = os.path.join(playlist_folder, file).lower()

    with open(filepath, 'r') as f:
        video_urls = [
            line.split('#')[0].rstrip().rstrip('\n')
            for line in f.readlines()
        ]

    return video_urls


def preprocess_filename(raw_name: str) -> str:

    filename = raw_name.rstrip('.mp3')
    filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('utf-8') # Accents
    filename = re.sub(r'[^a-zA-Z0-9\s]', '_', filename) # Non-alphanumeric characters
    filename = re.sub(r'\s+', '_', filename) # Spaces
    filename = filename.strip('_')

    return filename.lower() + '.mp3'