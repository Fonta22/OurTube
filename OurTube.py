import os
from pytube import YouTube
os.system('clear')
print("LOADING...")
print("")
os.system('pip install pytube')
os.system('clear')

print("__________________________________")
print("| ☭ Coммuиisт уоuтuве Dошиlоаdея ☭|")
print("|                                 |")
print("\_ _ _ _ _ _By PoLocHiK_ _ _ _ _ _/")
print(" ")
print("Introdueix el link de Youtube")
url = input()
os.system('clear')

print("Working...")
video= YouTube(url)
stream = video.streams.get_highest_resolution()
os.system('clear')

print("Ara la ruta de descarrega")
stream.download(output_path = input())
os.system('clear')
print("Descarregat!")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

#/home/usuari/Vídeos/youTuBiiDownload
