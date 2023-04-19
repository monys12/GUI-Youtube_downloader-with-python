import pytube
from pytube import YouTube
import os
import wget

url = pytube.YouTube(input("Youtube Link :"))
print(url.thumbnail_url)


