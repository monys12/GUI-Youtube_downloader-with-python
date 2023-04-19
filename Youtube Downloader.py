import tkinter
import customtkinter
import pytube
from pytube import YouTube
import threading
def startdownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_pro)
        vid = ytobject.streams.get_highest_resolution()
        vid.download()

        title.configure(text=ytobject.title, text_color="white")
        fin.configure(text="")
        fin.configure(text="Downloaded! ", text_color="green")
    except:
        fin.configure(text="Invalid Url ", text_color="red")
def on_pro(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perc = bytes_download / total_size * 100
    per = str(int(perc))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    progressBar.set(float(perc) / 100 )
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x479")
app.title("Youtube Downloder GUI ")
title = customtkinter.CTkLabel(app, text="Put the url here", font=('Goudy Bookletter 1911', 19))
title.pack(padx=10, pady=15)
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()
fin = customtkinter.CTkLabel(app, text="")
fin.pack()
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()
def therd():
    th = threading.Thread(target=startdownload).start()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=therd)
download.pack()

app.mainloop()