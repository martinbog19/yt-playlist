import os
import shutil
import sys


from src.utils import read_playlist, preprocess_filename
from src.youtube_download import download_audio
from src.apple_music import create_playlist, move_to_playlist


assert len(sys.argv) > 1, 'Please specify playlist name!'
assert len(sys.argv) < 3, 'Please provide only one argument...'

PLAYLIST_NAME = sys.argv[1]
video_urls = read_playlist(PLAYLIST_NAME)

print('\n')
try:
    temp_path = 'temp_folder.nosync'
    os.makedirs(temp_path)

    for i, video_url in enumerate(video_urls):
        title, file_path = download_audio(video_url, temp_path)
        print(f'[{str(i+1).zfill(2)}/{len(video_urls)}]  Successfully downloaded audio of "{title}"')
        
    print('\n')

    mp3_files = [
        file for file in os.listdir(temp_path)
        if file.endswith('.mp3')
    ]

    create_playlist(PLAYLIST_NAME)
    for i, mp3_file in enumerate(mp3_files):

        file_path = os.path.join(temp_path, mp3_file)
        safe_filename = preprocess_filename(mp3_file)
        safe_path = os.path.join(temp_path, safe_filename)
        os.rename(file_path, safe_path)

        abs_file_path = os.path.abspath(safe_path)

        move_to_playlist(abs_file_path, PLAYLIST_NAME)
        print(f'[{str(i+1).zfill(2)}/{len(video_urls)}]  {PLAYLIST_NAME} <-- {safe_filename}')

    print('\n')

except Exception as e:
    print(f'{video_url} Failed with error {e}')

finally:
    shutil.rmtree(temp_path)