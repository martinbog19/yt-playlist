import os
import re
import unicodedata



def read_playlist(playlist_path) -> list[str]:

    assert playlist_path.endswith('.txt'), 'Playlist path must be a .txt file!'

    with open(playlist_path, 'r') as f:
        youtube_ids = [
            line.split('#')[0].rstrip().rstrip('\n')
            for line in f.readlines()
        ]

    return youtube_ids


def read_archives(archive_path) -> list[str]:

    with open(archive_path, 'r') as f:
        youtube_ids = [
            line.lstrip('youtube ').rstrip('\n')
            for line in f.readlines()
        ]

    return youtube_ids




def preprocess_filename(raw_name: str) -> str:

    filename = raw_name.rstrip('.mp3')
    filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('utf-8') # Accents
    filename = re.sub(r'[^a-zA-Z0-9\s]', '_', filename) # Non-alphanumeric characters
    filename = re.sub(r'\s+', '_', filename) # Spaces
    filename = filename.strip('_')

    return filename.lower() + '.mp3'