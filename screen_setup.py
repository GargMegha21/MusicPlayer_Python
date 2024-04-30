from datetime import time
from tkinter import *
from PIL import Image,ImageTk
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3

mixer.init()
class musicplayer:
    def __init__(self,Tk):
        self.root = Tk
        self.root.title('Music_Player')
        self.root.geometry('700x400')
        self.root.configure(background='white')

        # open file dialog
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

        #menu
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='open' , command=Openfile)
        self.submenu.add_command(label='exit' , command=self.root.destroy)

        def About():
            tkinter.messagebox.showinfo('About us' , 'Music Player created By Megha Garg')


        self.submenu3 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.submenu3)
        self.submenu3.add_command(label='About' , command=About)


        # self.submenu2 = Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label='Edit', menu=self.submenu2)
        # self.submenu2.add_command(label='cut')
        # self.submenu2.add_command(label='copy')
        # self.submenu2.add_command(label='paste')



        #Adding Label
        self.filelabel=Label(text='Lets Make it' , bg='black' , fg='white' , font=22)
        self.filelabel.place(x=50,y=20,height=50)

        def songinf():
            self.filelabel['text'] = 'Current Music :-' + os.path.basename(filename)

        # Adding Leftsideimage--
        # L=Left
        self.L_photo = ImageTk.PhotoImage(file='leftimg.png')
        L_photo = Label(self.root, image=self.L_photo).place(x=150, y=100,  height=250)

        # Adding image
        self.photo=ImageTk.PhotoImage(file= 'music.png')
        photo = Label(self.root,image=self.photo,bg='cyan').place(x=50,y=100)

        # functions
        def playmusic():
            global paused
            try:
                paused
            except NameError:
                try:
                    # mixer.music.load('Naina.mp3')
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music Playing..'
                    songinf()
                except:
                    self.label1['text'] = 'Error: File not found'
            else:
                mixer.music.unpause()
                self.label1['text'] = 'Music Unpaused..'

        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music Stopped..'

        def pausemusic():
            global  paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music Paused..'

        # label
        self.label1=Label(self.root,text='Lets play it')
        self.label1.pack(side=BOTTOM,fill=X)

        def length_bar():
            if mixer.music.get_busy():
                current_time = mixer.music.get_pos() / 1000
                convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))
                song_mut = MP3(filename)
                song_mut_length = song_mut.info.length
                convert_song_mut_length = time.strftime('%M:%S', time.gmtime(song_mut_length))
                self.lengthbar.config(
                    text=f'Current Time: {convert_current_time} / Total Length: {convert_song_mut_length}')
            else:
                self.lengthbar.config(text='Current Time: 00:00 / Total Length: 00:00')

            self.lengthbar.after(1000, length_bar)


        #Creating Butons

        self.lengthbar = Label(self.root, text='Total_Length:-00:00', bg='black', fg='white', font=20 )
        self.lengthbar.place(x=50,y=515)
        #playbutton
        self.photo_B1=ImageTk.PhotoImage(file='play.png')
        Button(self.root, image=self.photo_B1, bd=0, bg='white', command=playmusic).place(x=60, y=550)

        # pausebutton
        self.photo_B2 = ImageTk.PhotoImage(file='play.png')
        photo_B2 = Button(self.root, image = self.photo_B2, bd=0, bg='white' , command=pausemusic).place(x=150, y=550)

        # stopbutton
        self.photo_B3 = ImageTk.PhotoImage(file='play.png')
        photo_B3 = Button(self.root, image=self.photo_B3, bd=0, bg='white',command=stopmusic).place(x=250, y=550)

#         volume bar




root=Tk()
obj=musicplayer(root)
root.mainloop()