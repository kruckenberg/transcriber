import sys
from operator import itemgetter
import download_audio as da
import speech_to_text as stt

def main(yt_url):
    filepath, title = itemgetter('filepath', 'title')(da.download_audio_only(yt_url))
    stt.speech_to_text(filepath=filepath, title=title)

if __name__ == '__main__':
    yt_url = sys.argv[1]
    print(f"Downloading video at {yt_url}")
    main(yt_url)
