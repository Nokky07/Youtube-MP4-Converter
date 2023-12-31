#Created By Nokky07
#File Created On 21th December 2022
#Mp4 Supported Only
#Educational purposes only. Use this at your own risk!

from pytube import YouTube
import art
import os
import time

Blue = "\033[0;34m"
Red = "\033[0;31m"
Green = "\033[0;32m"


def main():

  def clear():
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")

  print(Red + art.heading)
  menu = int(
    input(
      Green +
      "\n\nWelcome To The Youtube Converter Please Choose An Option:\n\n (1) - Mp4\n (2) - Credits\n (3) - Exit\n\n  >"
    ))

  if menu == (1):
    print(Red + art.heading1)
    def Download(url):
      youtubeObject = YouTube(url)
      youtubeObject = youtubeObject.streams.get_highest_resolution()
      try:
        youtubeObject.download()
      except:
        print(Red + "\n\nAn error has occurred :(")
      print(Green + "\n\nDownload is completed successfully :)")
  
    url = input(Blue + "\n\nEnter the YouTube video URL: ")
    Download(url)
    time.sleep(1)
    clear()
    print(Green + art.walter)
    print(Blue + "\n\nYour file should be downloaded")
    print(Blue + "\n\nThank You For Using My Mp4 Converter By Nokky07")
    time.sleep(5)
    clear()
    Download(url)
    main()
    time.sleep(2)
    main()
  elif menu == (2):
    print(Blue + art.credits)
    print(Red +art.smoke)
  elif menu == (3):
    exit()
main()