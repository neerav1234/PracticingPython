from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Download videos with Link")

Label(root, text = 'Youtube Video Downloader', font = 'algerian').pack()

link = StringVar()

Label(root, text = 'Paste Link Here', font = 'arial 16 bold').place(x=160, y=60)
link_enter = Entry(root, textvariable = link, bg = 'ghost white', font = 'arial 16 bold', width = 70).place(x=32, y=90)


def Download():
    yt = YouTube(str(link.get()))
    video = yt.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Download).place(x=180 ,y = 150)

root.mainloop()