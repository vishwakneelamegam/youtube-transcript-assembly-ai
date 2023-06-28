import youtubeDownload
import transcribeVideo

#test area

url = "https://www.youtube.com/watch?v=oYZ--rdHL6I"

downloadedFileName = youtubeDownload.downloadYoutubeVideo(url)
if downloadedFileName == None:
    print("Exception occurred while downloading the video")
else:
    print("Downloaded File : {}".format(str(downloadedFileName)))
    uploadedUrl = transcribeVideo.uploadVideo(downloadedFileName)
    if uploadedUrl == None:
        print("Didn't received uploaded url")
    else:
        print("Uploaded Url : {}".format(uploadedUrl))
        payload = transcribeVideo.makePayload(uploadedUrl)
        id = transcribeVideo.startToTranscriptVideo(payload)
        if id == None:
            print("Didn't receive id")
        else:
            print("id : {}".format(id))
            transcribedText =  transcribeVideo.pollTranscriptionVideo(id)
            if transcribedText == None:
                print("Error while polling")
            else:
                print("Transcribed Text : {}".format(transcribedText))