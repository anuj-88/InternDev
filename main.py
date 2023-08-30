import tkinter
import customtkinter
from pytube import YouTube
import time

def startDownload():
    try:
        ytLink=link.get()
        ytObject=YouTube(ytLink)
        video=ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube Link is Invalid")
    print("Download Complete")
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("720x480")

app.title("Youtube Downloader")

#Adding UI
title=customtkinter.CTkLabel(app,text="Insert a youtube link")
title.pack(padx=10,pady=10)

#Link Input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#Download Button
download=customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)

# run app
app.mainloop()