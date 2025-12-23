import subprocess

def download_video(url, output="input.mp4"):
    subprocess.run(
        ["yt-dlp", "-f", "mp4", "-o", output, url],
        check=True
    )
