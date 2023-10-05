import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

pygame.mixer.init()

def Open_File():
    music_file=filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if os.path.exists(music_file):
        Play_Music(music_file)

def Play_Music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

def Stop_Music():
    pygame.mixer.music.stop()

def Pause_Music():
    pygame.mixer.music.pause()

def UnPause_Music():
    pygame.mixer.music.unpause()

def Exit():
    pygame.mixer.quit()

def set_volume(val):
    volume=float(val)/100
    pygame.mixer.music.set_volume(volume)

root=tk.Tk()
root.title("Python Music Player \n")

button_width=15
button_height=2

Open_Button=tk.Button(root,  text="Open", command=Open_File, width=button_width, height=button_height, bg="black", fg="white", relief="raised")
Play_button=tk.Button(root,  text="Play", command=Play_Music, width=button_width, height=button_height, bg="black", fg="white", relief="raised")
Stop_button=tk.Button(root,  text="Stop", command=Stop_Music, width=button_width, height=button_height, bg="black", fg="white", relief="raised")
Pause_button=tk.Button(root,  text="Pause", command=Pause_Music, width=button_width, height=button_height, bg="black", fg="white")
Unpause_button=tk.Button(root,  text="Unpause", command=UnPause_Music, width=button_width, height=button_height, bg="black", fg="white")
Exit_button=tk.Button(root,  text="Exit", command=Exit, width=button_width, height=button_height, bg="black", fg="white")


volume_label=tk.Label(root, text="Volume: ", bg="black", fg="white", width=button_width, height=button_height)
volume_slider=ttk.Scale(root,  from_=0, to=100, orient="horizontal", command=set_volume)
volume_slider.set(50)
volume_label.pack()
volume_slider.pack()


button_padding=10
Open_Button.pack(pady=button_padding)
Play_button.pack(pady=button_padding)
Stop_button.pack(pady=button_padding)
Pause_button.pack(pady=button_padding)
Unpause_button.pack(pady=button_padding)
Exit_button.pack(pady=button_padding)

root.mainloop()
