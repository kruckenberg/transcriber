import yt_dlp

class MetaDataCollectorPostProcessor(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(MetaDataCollectorPostProcessor, self).__init__(None)
        self.filepath = None 
        self.title = None 

    def run(self, information):
        self.filepath = information['filepath']
        self.title = information['title']
        return [], information

def download_audio_only(yt_url):
    opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'paths': {
            'home': './audio',
        },
    }

    metadata_collector = MetaDataCollectorPostProcessor()

    with yt_dlp.YoutubeDL(opts) as ytdl:
        ytdl.add_post_processor(metadata_collector)
        ytdl.download(yt_url)


    return { 
        'filepath': metadata_collector.filepath, 
        'title': metadata_collector.title 
    } 
