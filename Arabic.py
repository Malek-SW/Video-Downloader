
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
import re



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
            os.startfile(full)
        except FileNotFoundError:
            messagebox.showerror("خطأ", f"لم يتم العثور على الملف: {full}")



    def close():
        new.destroy()
    qe = che.get()
    new = ctk.CTkToplevel(root)
    ctk.set_appearance_mode('dark')
    new.lift()
    new.title("برنامج مالك لتحميل الفيديوهات")
    new.geometry('300x200')
    new.lift()
    new.resizable(False,False)
    icon = Image.open("success-icon.ico")
    ph = ImageTk.PhotoImage(icon)
    
    img = ctk.CTkLabel(new, image=ph, text="")
    img.place(y=28, x=30)

    tet = ctk.CTkLabel(new, text=('تم تحميل الفيديو بنجاح'), font=('Arial', 15)) 
    tet.place(y=32, x=120)


    if qe == 'فيديو':

        btn1 = ctk.CTkButton(new, text='الفيديو فتح', command=video)
        btn1.place(y=90, x=155)
        btn2 = ctk.CTkButton(new, text='المجلد فتح', command=open_folder)
        btn2.place(y=90, x=10)

        btn3 = ctk.CTkButton(new, text='اغلاق', command=new.destroy)
        btn3.place(y=130, x=90)
    elif qe == 'قناه':

        btn2 = ctk.CTkButton(new, text='المجلد فتح', command=open_folder)
        btn2.place(y=90, x=90)

        btn3 = ctk.CTkButton(new, text='اغلاق', command=new.destroy)
        btn3.place(y=130, x=90)
    else:

        btn2 = ctk.CTkButton(new, text='المجلد فتح', command=open_folder)
        btn2.place(y=90, x=90)

        btn3 = ctk.CTkButton(new, text='اغلاق', command=new.destroy)
        btn3.place(y=130, x=90)

def info():
    news= ctk.CTkToplevel(root)
    news.geometry("400x200")
    news.lift()
    news.title("برنامج مالك لتحميل الفيديوهات")
    news.resizable(False, False)
    n = ctk.CTkLabel(news, text=""" 
                            هذا البرنامج هو المشروع الثالث للطالب مالك عبد الفتاح                              
                             في مجال البرمجة. يقوم البرنامج بتنزيل الفيديوهات من                            
                           مواقع متعددة، بما في ذلك تنزيل القنوات وقوائم التشغيل.                        
                           بشرط استخدامه فى المحتوى الهادف مع التأكيد على التبرء                          
                           من اى مخالفات شرعية. نأمل أن تجد البرنامج مفيدًا وممتعًا                          
                                    في استخدامك اليومي . شكراً لاستخدامك البرنامج.                              

 
              """ , font=('Arial', 15))
    n.pack(padx=60)
    clo = ctk.CTkButton(news, text='اغلاق',command=news.destroy)
    clo.place(x=130, y=150)
  

    
def hook(d):
    if d['status'] == 'downloading':

        progress_var.set(d['downloaded_bytes'] / d['total_bytes'] * 100)
        root.update_idletasks() 
def button_callback():
    
    url = down.get()
    wer = chose.get()
    qa = chse.get()

    if not path:
            messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , 'لم يتم تحديد مكان التحميل')
    elif not url:
            messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , 'لم يتم تحديد رابط التحميل')
    elif not wer:
            messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , 'لم يتم تحديد الجوده')
    elif not qa:
            messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , 'لم يتم تحديد نوع التحميل (فيديو/صوت)')
    else:            
        if qa == 'فيديو':
            sw = f"bestvideo[height<={wer}]+bestaudio/best"
        elif qa == 'صوت':
            sw = 'bestaudio'
        
        ydl_opts = {
              'format': sw,
              'outtmpl': f'{path}/%(title)s.%(ext)s',   
              'progress_hooks': [hook]  
          }
          
        global full
        full = ""
      
        try:
         
         
                 with yt_dlp.YoutubeDL(ydl_opts) as downloader:
         
                     main = downloader.extract_info(url, download=False)
                      
                     title = main.get('title', 'video')
                     ext = main.get('ext', 'mp4')
                     
                     cleaned_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
                 #    if not os.path.exists(f'{path}/{cleaned_title}.{ext}'):
                   #     messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , f'الفيديو {title} موجود بالفعل فى المكان ليس{path}')    
                     full = f'{path}/{title}.{ext}'
                     global progress_bar
                     global progress_var 
         
                     progress_var = DoubleVar()
                     progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
                     progress_bar.place(x=117, y=570, width=400)
                     inf = ctk.CTkLabel(root, text=f"يتم تحميل : {title}" , font=('Arial' ,14))
                     inf.place(x=120,y=500)
                     ydl_opts = {
                       'format': sw,
                       'outtmpl': f'{path}/%{cleaned_title}.%ext',
                       'progress_hooks': [hook]  
                       }
                     downloader.download([url])
                    # if not os.path.exists(f'{path}/{cleaned_title}.{ext}'):
                     #   messagebox.showerror('برنامج مالك لتحميل الفيديوهات' , f'الفيديو {title} موجود بالفعل فى المكان ليس{path}')                         
                     progress_bar.destroy()
                     inf.configure(text=f"! تم التحميل بنجاح ", font=('Arial' ,14) , text_color='green')   
                     inf.place(x=200,y=450)
                     threading.Thread(target=successfuly).start()
                     
        except Exception as e:
                 inf.place_forget() 
                 sw = ctk.CTkLabel(root, text=f"! خطأ في التحميل" , font=('Arial' ,14) , text_color='red')
                 sw.place(x=223, y=480)
                 messagebox.showerror('برنامج مالك لتحميل الفيديوهات', f'خطأ في التحميل {e}')
def thread():
     aw = threading.Thread(target=button_callback)
     aw.start()

down = ctk.CTkEntry(root, height=27, width=200)
down.place(x=150, y=100)


se= ctk.CTkLabel(root, text="الصق الرابط", font=('Arial', 15)) 
se.place(x=360, y=100)

chose = ctk.CTkComboBox(root, values=['360', '480', '720', '1080'])
chose.place(x=180, y=150)

button = ctk.CTkButton(root, text="الان حمل", command=thread)
button.place(x=180, y=390)

buttn = ctk.CTkButton(root, text="المكان اختر", command=browse)
buttn.place(x=180, y=200)

chse = ctk.CTkComboBox(root, values=["فيديو", "صوت"])
chse.place(x=180, y=290)

sewq= ctk.CTkLabel(root, text="اختر نوعية الفيديو", font=('Arial', 15)) 
sewq.place(x=340, y=290)


che = ctk.CTkComboBox(root, values=['فيديو', 'قناه', 'تشغيل قائمة'])
che.place(x=180, y=340)


sewq1= ctk.CTkLabel(root, text="اختر حجم التحميل", font=('Arial', 15)) 
sewq1.place(x=340, y=340)

sewq2= ctk.CTkLabel(root, text="اختر الجوده", font=('Arial', 15)) 
sewq2.place(x=340, y=150)

btn_info = ctk.CTkButton(root,image=icon_phot,text="", width=7 , height=7 , command=info)
btn_info.place(x=430 , y=540)
d = ctk.CTkLabel(root, image=icon_photo, text="" )
d.place(x=230, y=40)

dow = ctk.CTkEntry(root, height=27, width=200)
dow.place(x=150, y=250)
root.title("برنامج مالك لتحميل الفيديوهات")


root.mainloop() 