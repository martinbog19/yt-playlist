import subprocess



def run_subprocess(apple_script: str):

    subprocess.run(
        ["osascript", "-e", apple_script],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def create_playlist(playlist_name: str):

    apple_script = f'''
    tell application "Music"
        -- Check if playlist exists, if not create it
        if not (exists playlist "{playlist_name}") then
            make new playlist with properties {{name:"{playlist_name}"}}
        end if
    end tell
    '''
    
    run_subprocess(apple_script)


def move_to_playlist(file_path: str, playlist_name: str):
     
    file_path_applescript = file_path.replace("'", "'\\''")

    apple_script = f'''
    tell application "Music"
        -- Add the file to the playlist
        add POSIX file "{file_path_applescript}" to playlist "{playlist_name}"
    end tell
    '''

    run_subprocess(apple_script)