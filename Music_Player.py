from tkinter import *
import pygame
import os


# Building Constructor for Title and geometry for window and initiate pygame and pygame mixer
class MusicPlayer:
    def __init__(self,root):
        self.root=root
    #Title of the Window
        self.root.title("MusicPlayer")
    #Window Geometry
        self.root.geometry("1000x200+200+200")
    #Initiating Pygame
        pygame.init()
    # Initiating pygame Mixer
        pygame.mixer.init()
    # Declaring track variable
        self.track =StringVar()
    # Declaring Status Variable
        self.status =StringVar()



    #Creating  the track frame for song label and status label

        trackframe=LabelFrame(self.root,text="Song Track", font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)

    # Inserting SOng track Label

        songtrack=Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="white",fg="gold").grid(row=0,column=1,padx=10,pady=5)
    # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="blue",fg="gold").grid(row=0,column=1,padx=10,pady=5)


# Creating Button Frame'''
        buttonframe=LabelFrame(self.root,text="Controls",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)

    #Inserting Play Button
    
        playbtn =Button(buttonframe ,text="PLAY",command=self.playsong,width=10,height=1,font=("Comic Sans MS",16,"bold"),fg="navyblue",bg="green").grid(row=0,column=0,padx=10,pady=5)
    #Inserting Pause Button
        playbtn =Button(buttonframe ,text="PAUSE",command=self.pausesong,width=10,height=1,font=("Comic Sans MS",16,"bold"),fg="navyblue",bg="red").grid(row=0,column=1,padx=10,pady=5)
    #Inserting Unpause Button
        playbtn =Button(buttonframe ,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("Comic Sans MS",16,"bold"),fg="navyblue",bg="yellow").grid(row=0,column=2,padx=10,pady=5)
    #Inserting Stopsong Button
        playbtn =Button(buttonframe ,text="STOPSONG",command=self.stopsong,width=10,height=1,font=("Comic Sans MS",12,"bold"),fg="navyblue",bg="orange").grid(row=0,column=3,padx=10,pady=5)

# '''Creating Playlist Frame'''
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("bitstreamverasans",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=600,height=400)

    #Inserting Scroll Bar

        scrol_y=Scrollbar(songsframe,orient=VERTICAL)

    #Inserting  Platlist Listbox

        self.playlist =Listbox(songsframe ,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("comicsansms",12,"bold"),bg="silver",fg="red",bd=5,relief=GROOVE)
    
#! Applying scroll to  listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)


#@ changng Directory

        os.chdir("E:\Cool\songs")
        songtracks =os.listdir()
#Inserting song into playlist

        for track in songtracks:
    
            self.playlist.insert(END,track)


#   @@@@@@@@@@@@@@@@@@@@     PLAYSONG()            @@@@@@@@@@@@@@@@@@@@@@@
    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
    # displaying status
        self.status.set("Playing")
    #Load selected SOng
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
    #playing selected song
        pygame.mixer.music.play()
        



    def stopsong(self):
    # displaying status
        self.status.set("STOP")
    #Paused SOng
        pygame.mixer.music.stop()



    def pausesong(self):
    # displaying status
        self.status.set("paused")
    #Paused SOng
        pygame.mixer.music.pause()

    def unpausesong(self):
    # It will Display the  Status
        self.status.set("-Playing")
    # Playing back Song
        pygame.mixer.music.unpause()

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()




















    
