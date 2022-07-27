from asyncio import streams
from pytube import YouTube

link = " https://youtu.be/OoIEZ8wI3Sc"

video = YouTube(link)
stream = video.streams.get_highest_resolution()
emailid = input("Enter your email id: ")
stream.download()