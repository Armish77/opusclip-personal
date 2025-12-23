from fastapi import FastAPI
from pydantic import BaseModel

from downloader import download_video
from chunker import split_into_chunks
from ai_pipeline import collect_scores
from video_utils import crop_vertical
from captions import add_captions
from cloud_storage import upload

app = FastAPI()

class Req(BaseModel):
    video_url: str

@app.post("/process")
def process(req: Req):
    download_video(req.video_url)
    chunks = split_into_chunks("input.mp4")

    ranked = collect_scores(chunks)
    top = ranked[:3]

    links = []

    for i, seg in enumerate(top):
        raw = f"clip_{i}.mp4"
        final = f"clip_{i}_final.mp4"

        crop_vertical("input.mp4", raw, seg["start"], 15)
        add_captions(raw, final)

        links.append(upload(final))

    return {"clips": links}
