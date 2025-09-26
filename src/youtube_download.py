import yt_dlp
from mutagen.easyid3 import EasyID3



def progress_hook(progress: dict) -> None:

    if progress['status'] == 'downloading':
        percent = progress.get('_percent_str', '').strip()
        speed = progress.get('_speed_str', '').strip()
        eta = progress.get('_eta_str', '').strip()
        progress_msg = f"\r{percent} | {speed} | ETA: {eta}"
        print(progress_msg, end='', flush=True)


def download_audio(
        youtube_url: str,
        output_path: str,
        archive_path: str,
    ) -> tuple[str, str]:
    
    ydl_opts = {
        'quiet': True,  # Suppress everything except errors
        'progress_hooks': [progress_hook],
        'download_archive': archive_path,
        'format': 'bestaudio/best',
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(youtube_url, download=True)

        if info is None:
            return None, None

        title = info.get('title', 'Unknown Title')
        artist = info.get('uploader', 'Unknown Artist')
        album = info.get('album', 'Unknown Album')
        file_path = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3").replace(".mp4", ".mp3")

        audio = EasyID3(file_path)
        audio['title'] = title
        audio['artist'] = artist
        audio['album'] = album
        audio.save()
    
    return title, file_path

