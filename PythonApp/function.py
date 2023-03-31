from pytube import YouTube

def Downloader(link, save_path, dltype):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(res="720p", file_extension = "mp4").first()
        save_path_real = save_path[0]
        lastslash = save_path_real.rfind("/")
        if(dltype == "single"):
            stream.download(save_path_real[0:lastslash],filename=save_path_real[lastslash+1:]+".mp4")
        else:
            stream.download(save_path_real[0:lastslash])
    except Exception as e:
        print(e)

    #print(save_path)
    #yt.set_filename('GeeksforGeeks Video')
    #d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    #try: 
        # downloading the video 
        #d_video.download(SAVE_PATH) 
    #except: 
        #print("Some Error!")