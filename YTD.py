from tkinter import *
from pytube import YouTube
import os
from moviepy.editor import *

root = Tk()
root.geometry('700x500')
root.resizable(0,0)
root.title("Youtube Downloader")


Label(root,text = 'Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root,text = 'Paste Link Here:', font = 'arial 15 bold').place(x=160, y =60)
link_enter = Entry(root, width = 70, textvariable = link).place(x=32, y =90)

def Downloader():
    url = str(link.get())
    
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    else:
        video = YouTube(url)
    highest_quality_video(video)
    #audio_only(url)


def highest_quality_video(url):
    print("Downloading Video")

    try:
        filename = url.title
        for r in ((" ", "_"), ("|", "")):
            filename = filename.replace(*r)
        filters = url.streams.filter(progressive=True, file_extension='mp4')
        

        
        filters.get_highest_resolution().download(
            output_path='/Volumes/Nikhil_SD/Music/YTD', filename=filename)
        # try:
        #     filters.get_by_resolution('1080p').download(
        #         output_path='/Volumes/Nikhil_SD/Music/YTD', filename=filename)
        #     print("1080p")
        # except:
        #     filters.get_highest_resolution().download(output_path='/Volumes/Nikhil_SD/Music/YTD', filename=filename)
        #     print("Highest Resolution Available")
        
        print('Download Complete! Saved to file: %s' % filename)
        Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

    except Exception as e:
        print(e)
        

def audio_only(url):
 #       https://www.youtube.com/watch?v=QUF9cJSts8c

    try:
        print("download initiated")
        print("title :",url.title)
        # name = url.title.replace(" ","_")+".mp4"
        # name.replace("|","")
        # print("File Name: ",name)
        name="temp"
        url.streams.get_audio_only().download(
            output_path='/Volumes/Nikhil_SD/Music/YTD', filename= name)
        name+= ".mp4"
        video = VideoFileClip(os.path.join(
            "/Volumes/Nikhil_SD/Music/YTD", name,))
        video.audio.write_audiofile(os.path.join(
            "/Volumes/Nikhil_SD/Music/YTD", name, ".mp3"))
        print('Audio Downloaded Successfully')
        
        Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

    except Exception as e:
        print(e)
    
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pale violet red', padx=2, command = Downloader).place(x=180, y=150)

root.mainloop()

#Download Highest Resolution Video

