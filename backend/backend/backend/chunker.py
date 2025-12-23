 import subprocess
import os

def split_into_chunks(video_path, chunk_minutes=5):
    os.makedirs("chunks", exist_ok=True)

    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_path,
        "-c", "copy",
        "-map", "0",
        "-segment_time", str(chunk_minutes * 60),
        "-f", "segment",
        "chunks/chunk_%03d.mp4"
    ], check=True)

    return sorted([
        f"chunks/{f}" for f in os.listdir("chunks")
        if f.endswith(".mp4")
    ])
