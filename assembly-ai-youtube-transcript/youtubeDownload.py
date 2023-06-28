import uuid
import yt_dlp as youtubeDownloaderModule

videoExtension = ".mp4"

def makeVideoName(name : str) -> str:
    try:
        return "{}{}".format(name, videoExtension)
    except Exception as e:
        return "test.mp4"

def downloadYoutubeVideo(youtubeLink : str) -> str:
    try:
        name = str(uuid.uuid4())
        madeVideoName = makeVideoName(name)
        options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': madeVideoName, 
            }
        with youtubeDownloaderModule.YoutubeDL(options) as youtubeDownloader:
            youtubeDownloader.download([youtubeLink])
        return madeVideoName
    except Exception as e:
        return None
