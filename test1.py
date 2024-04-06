import os
import sys
import tkinter as tk
import winsound

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def play_sound():
    winsound.PlaySound(resource_path('moan.wav'), winsound.SND_FILENAME)

window = tk.Tk() 
window.geometry("420x420")
window.title("Oh yes daddy!!!")

icon = tk.PhotoImage(file=resource_path('logo.png'))
window.iconphoto(True, icon)
window.config(background="#693e50")

button = tk.Button(window, text="Click me!", command=play_sound)
button.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()