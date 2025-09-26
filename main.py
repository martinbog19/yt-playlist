import os

from src.utils import read_playlist, read_archives, preprocess_filename
from src.youtube_download import download_audio



PLAYLIST     = 'playlist.txt'
SONGS_PATH   = 'songs.nosync'
ARCHIVE_PATH = 'downloaded.txt'

youtube_ids = read_playlist(PLAYLIST)

print('\n')
for i, youtube_id in enumerate(youtube_ids):

    video_url = 'https://www.youtube.com/watch?v=' + youtube_id

    title, file_path = download_audio(video_url, SONGS_PATH, ARCHIVE_PATH)

    if title and file_path:
        
        print(f'[{str(i+1).zfill(3)}/{str(len(youtube_ids)).zfill(3)}]  Successfully downloaded audio of "{title}"')

        safe_filename = preprocess_filename(file_path.split('/')[-1])
        safe_path = os.path.join(SONGS_PATH, safe_filename)
        os.rename(file_path, safe_path)
        print(f'Saved as {safe_path}')

    else:
        print(f'Skipping {video_url}...')