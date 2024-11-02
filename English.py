
import customtkinter as ctk
import yt_dlp
from tkinter import messagebox
from tkinter import StringVar, ttk
from PIL import Image, ImageTk
from tkinter import *
import os
import pygame
import customtkinter as ctk
import yt_dlp
import re
from tkinter import messagebox
from tkinter import StringVar
from PIL import Image, ImageTk
from tkinter import *
from PIL import *
import time
import threading
from tkinter import filedialog
from tkinter import dialog
from PIL import Image, ImageTk
import os
import threading
import time
import playsound
import pygame


titles = 'Downloader Video'

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

root = ctk.CTk()
root.geometry("500x600")
swer = StringVar()

ctk.set_appearance_mode('dark')

icon_image = Image.open("icon.ico") 
icon_photo = ImageTk.PhotoImage(icon_image)


icon_imag = Image.open("info.ico") 
icon_phot = ImageTk.PhotoImage(icon_imag)

root.iconphoto(False, icon_photo)
root.resizable(False, False)
def browse():
    global path
    path = filedialog.askdirectory().strip()
    dow.delete(0, 'end')
    dow.insert(0, str(path))
    
def successfuly():
    pygame.mixer.music.load("sfx_-_success.ogg")
    pygame.mixer.music.play()

    def open_folder():
       new.destroy()

       os.startfile(path)
    def video():
        new.destroy()
        print("Trying to open:", full)  # Debugging line
        try:
            os.startfile(full.strip())
        except FileNotFoundError:
            messagebox.showerror("Error", f"The File Is Not Found: {full}")



    def close():
        new.destroy()
    qe = che.get()
    new = ctk.CTkToplevel(root)
    ctk.set_appearance_mode('dark')
    new.lift()
    new.title("Video Downloader")
    new.geometry('300x200')
    new.lift()
    new.resizable(False,False)
    icon = Image.open("success-icon.ico")
    ph = ImageTk.PhotoImage(icon)
    
    img = ctk.CTkLabel(new, image=ph, text="")
    img.place(y=28, x=30)

    tet = ctk.CTkLabel(new, text=('The Video Is Downloaded !'), font=('Arial', 15)) 
    tet.place(y=32, x=100)


    if qe == 'video':

        btn1 = ctk.CTkButton(new, text='Open Video', command=video)
        btn1.place(y=90, x=155)
        btn2 = ctk.CTkButton(new, text='Open Folder', command=open_folder)
        btn2.place(y=90, x=10)

        btn3 = ctk.CTkButton(new, text='Close', command=new.destroy)
        btn3.place(y=130, x=90)
    elif qe == 'channel':

        btn2 = ctk.CTkButton(new, text='Open Folder', command=open_folder)
        btn2.place(y=90, x=90)

        btn3 = ctk.CTkButton(new, text='Close', command=new.destroy)
        btn3.place(y=130, x=90)
    else:

        btn2 = ctk.CTkButton(new, text='Open Folder', command=open_folder)
        btn2.place(y=90, x=90)

        btn3 = ctk.CTkButton(new, text='Close', command=new.destroy)
        btn3.place(y=130, x=90)

def info():
    news= ctk.CTkToplevel(root)
    news.geometry("400x300")
    news.lift()
    news.title("Downloader Video")
    news.resizable(False, False)
    n = ctk.CTkLabel(news, text=""" 
This program is the third project by the
student Malek Abdel Fattah in the field of
programming. The program allows downloading
videos from various platforms, including
channels and playlists, with the condition
that it be used for beneficial and lawful
content. We disclaim any responsibility
for improper use. We hope you find the 
program useful and enjoyable in your daily
use. Thank you for choosing our program.                         

 
              """ , font=('Arial', 15))
    n.pack(padx=60)
    clo = ctk.CTkButton(news, text='Close',command=news.destroy)
    clo.place(x=130, y=250)
  

    
def hook(d):
    if d['status'] == 'downloading':

        progress_var.set(d['downloaded_bytes'] / d['total_bytes'] * 100)
        root.update_idletasks()         

def button_callback():
    inf = ctk.CTkLabel(root, text=f"" , font=('Arial' ,14))
    inf.place(x=200, y=450)    
    url = down.get()
    wer = chose.get()
    qa = chse.get()

    if not path:
        messagebox.showerror(titles, 'The path is not selected')
    elif not url:
        messagebox.showerror(titles, 'the URL is not entered')
    elif not wer:
        messagebox.showerror(titles, 'The quality is not selected')
    elif not qa:
        messagebox.showerror(titles, 'The type is not selected (audio or video)')
    else:            
        if qa == 'video':
            sw = f"bestvideo[height<={wer}]+bestaudio/best"
        elif qa == 'audio':
            sw = 'bestaudio'
        
        ydl_opts = {
            'format': sw,
            'outtmpl': f'{path}/%(title)s.%(ext)s',    
            'progress_hooks': [hook]  
        }
          

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as downloader:
                main = downloader.extract_info(url, download=False)
                title = main.get('title', 'video')
                ext = main.get('ext', 'mp4')
                global full
                full = f'{path}/{title}.{ext}'
    


                global progress_bar
                global progress_var 

                progress_var = DoubleVar()
                progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
                progress_bar.place(x=117, y=570, width=400)
                inf.configure(text=f"Downloading : {title}" , font=('Arial' ,14))
                inf.place(x=120, y=500)         
                downloader.download([url])
                progress_bar.destroy()
                inf.configure(text=f"The Video Is Downloaded Successfully", font=('Arial' ,14) , text_color='green')   
                inf.place(x=150, y=450)
                threading.Thread(target=successfuly).start()
                     
        except Exception as e:
            inf.place_forget()  # أخفاء inf عند حدوث خطأ
            er = ctk.CTkLabel(root, text=f"Error: {e}", font=('Arial' ,14), text_color='red')
            er.place(x=223, y=480)                 
            messagebox.showerror(titles, 'Error During Downloading!')      


def thread():
     aw = threading.Thread(target=button_callback)
     aw.start()

down = ctk.CTkEntry(root, height=27, width=200)
down.place(x=150, y=100)


se= ctk.CTkLabel(root, text="Paste the URL", font=('Arial', 15)) 
se.place(x=360, y=100)

chose = ctk.CTkComboBox(root, values=['360', '480', '720', '1080'])
chose.place(x=180, y=150)

button = ctk.CTkButton(root, text="Download", command=thread)
button.place(x=180, y=390)

buttn = ctk.CTkButton(root, text="Browse", command=browse)
buttn.place(x=180, y=200)

chse = ctk.CTkComboBox(root, values=['video' , 'audio'])
chse.place(x=180, y=290)

sewq= ctk.CTkLabel(root, text="Select The Type", font=('Arial', 15)) 
sewq.place(x=340, y=290)


che = ctk.CTkComboBox(root, values=['video' , 'channel', 'playlist'])
che.place(x=180, y=340)


sewq1= ctk.CTkLabel(root, text="Choose The Download", font=('Arial', 15)) 
sewq1.place(x=340, y=340)

sewq2= ctk.CTkLabel(root, text="Choose The Quality", font=('Arial', 15)) 
sewq2.place(x=340, y=150)

btn_info = ctk.CTkButton(root,image=icon_phot,text="", width=7 , height=7 , command=info)
btn_info.place(x=430 , y=540)
d = ctk.CTkLabel(root, image=icon_photo, text="" )
d.place(x=230, y=40)

dow = ctk.CTkEntry(root, height=27, width=200)
dow.place(x=150, y=250)
root.title(titles)


root.mainloop() 