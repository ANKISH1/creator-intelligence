from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_transcript(url:str):
    def fetch_video_id(string):
        parsed = urlparse(string)
        query = parse_qs(parsed.query)
        return query.get("v", [None])[0]              

    video_id = fetch_video_id(url)

    transcript_api = YouTubeTranscriptApi()

    transcript = transcript_api.fetch(video_id, languages=['en', 'hi'])

    final_transcript = " ".join([s.text for s in transcript.snippets])
    return final_transcript