import os.path
from os import path
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter import *
import random
import time
import pyttsx3
from pyttsx3.drivers import sapi5
import webbrowser
import keyboard



#global================================================================================================
mysight = "https://sandeep-shaw10.github.io/sightexplore/"

#Introduction Window====================================================================================
class AppIntro(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('620x630+450+25')
        self.overrideredirect(True)
        self.configure(background='#ffffff')
        self.resizable(width=0, height=0)
        self.mycanvas = Canvas(self, bg="#ffffff", height=611, width=620)
        self.splashimg = PhotoImage(file="images//splashimg.png")
        self.mycanvas.create_image(0,0,image=self.splashimg, anchor=NW)
        self.mycanvas.pack()
        from tkinter import ttk
        from tkinter.ttk import Progressbar
        self.progress = ttk.Progressbar(self, orient=HORIZONTAL, length=620, mode="determinate")
        self.progress.pack()
        self.loaderBar()

    def loaderBar(self):
        for i in range(100):
            self.progress.configure(value = i)
            self.update()
            time.sleep(0.01*random.randint(1,5))
        self.destroy()         #loading


#App====================================================================================================
class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("    TEXT TO SPEECH 2020")
        self.iconbitmap('images//attsimgicon.ico')
        self.geometry('1260x760+100+0')
        self.make_topmost()                                 #tk_messages
        self.protocol("WM_DELETE_WINDOW", self.on_exit)     #tk_exit_message
        self.headinglayout()
        self.mainlayout()
        self.footerlayout()

    def say(self):
        #================================
        def onWord(name, location, length):
            print ('word', name, location, length, keyboard.is_pressed)
            if keyboard.is_pressed("esc"):
                print("PRESSED ")
                #self.engine.stop()
                #keyboard.is_pressed("esc") == False
                self.engine.endLoop()

        def onFinishUtterance(name, completed):
            #self.engine.endLoop()
            print("end")

        #================================
        self.textInput = self.text1.get("1.0","end-1c")
        self.lbl1.config(text="RUNNING", bg="#5cb85c")
        self.lbl1.update_idletasks()
        if self.textInput != "":
            self.engine = pyttsx3.init()
            print(self.engine)
            print("STEP 1 TEST")
            #============================
            
            print("STEP 2 TEST")
            #============================
            if self.rateEntry.get().isnumeric() and int(self.rateEntry.get()) > 0:
                print("STEP 3 TEST")
                self.engine.setProperty('rate', int(self.rateEntry.get()))
                self.engine.setProperty('volume',self.volumeEntry.get()/100)
                voices = self.engine.getProperty('voices')
                if self.voiceOption.get() == "MALE":
                    self.engine.setProperty('voice', voices[0].id)
                else:
                    self.engine.setProperty('voice', voices[1].id)
                self.engine.connect('started-word', onWord)
                self.engine.connect('finished-utterance', onFinishUtterance)
                print("STEP 4 TEST")
                self.engine.say(self.textInput)
                print("STEP 5 TEST")
                self.engine.runAndWait()
                #self.engine.startLoop()
                print("STEP 6 TEST")
                #self.text1.delete("1.0",'end-1c')
            else:
                print("INVALID RATE SELECTION")
                showerror("TTS ERROR", "INVALID RATE SELECTION")
        else:
            showwarning("TTS WARNING", "NO TEXT ENTERED")
        self.lbl1.config(text="STOP", bg="#d9534f")
        self.lbl1.update_idletasks()

    def save(self):
        self.textInput = self.text1.get("1.0","end-1c")
        #=============================================
        #def save_to_file(self, text, filename, name=None):
        '''
        Adds an utterance to speak to the event queue.
        @param text: Text to sepak
        @type text: unicode
        @param filename: the name of file to save.
        @param name: Name to associate with this utterance. Included in
            notifications about this utterance.
        @type name: str
        '''
        # self.proxy.save_to_file(text, filename, name)
        #=============================================

        if self.textInput != "" and self.saveEntry.get() != "":
            directory = os.getcwd()
            print("1 DIRECTORY : ",directory)
            dirName = "TTS_audio"           #Folder name VVIMP
            fileName = directory+"\\"+dirName
            print("2 To Search : ",fileName)
            savedFile = self.saveEntry.get()+".mp3"
            print("3 FILE NAME : ", savedFile)
            #print(fileName)
            if path.isdir(dirName):
                print("3 ",path.isdir(dirName))
                os.chdir(fileName)
                print("4 ",os.chdir(fileName))
                print("5 ",path.isfile(savedFile))
                if path.isfile(savedFile):
                    showerror("TTS 2020 Says", "FILE ALREADY EXIST")
                    os.chdir(directory)
                else:
                    self.engine = pyttsx3.init()
                    self.engine.save_to_file(self.textInput, savedFile)
                    self.engine.runAndWait()
                    msg = "YOUR FILE : "+savedFile+"\nIS SAVED AT LOCATION :\n"+fileName
                    showinfo("TTS FILE SAVED",msg)
                    os.chdir(directory)
            else:
                showerror("TTS ERROR","YOU HAVE CHANGED THE LOCATION!!!\nPLEASE MAKE A FOLDER 'TTS_audio' ")
                os.chdir(directory)
        else:
            showwarning("TTS WARNING", "CANNOT SAVE EMPTY FILE")

    def clear(self):
        self.text1.delete("1.0",'end-1c')

    def on_exit(self):                                      #Ask permission message before leaving
        if messagebox.askyesno("EXIT APPLICATION", "Do you want to quit TEXT TO SPEECH APP 2020?"):
            self.destroy()

    def make_topmost(self):                                 #Make the window appear in the front
        self.lift()
        self.attributes("-topmost", 1)
        self.attributes("-topmost", 0)

    def aboutus(self):
        webbrowser.open(mysight)
        
    def headinglayout(self):
        self.nameLabel = Label(self, text="TEXT TO SPEECH APP 2020", 
                               bg="#ff4d4d", 
                               fg="white", 
                               relief=RIDGE, 
                               font=("Helvetica",28,"bold"), 
                               height=1, bd=5, pady=10
                            )
        self.nameLabel.pack(fill = X)
        self.configure(bg="#292b2c")

    def mainlayout(self):
        from tkinter import ttk
        from tkinter.ttk import Scrollbar
        self.mainFrame = LabelFrame(self, padx=5, pady=5, height=800, bg="#f0ad4e")
        self.mainFrame.pack(padx=10, pady=(10,0), fill = X)

        self.dataFrame = LabelFrame(self.mainFrame, padx=5, pady=5, height=800, bg="#292b2c")
        self.dataFrame.pack(padx=10, pady=10, anchor=W, side=LEFT)
        self.scroll_y = ttk.Scrollbar(self.dataFrame)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.label1 = Label(self.dataFrame, text="ENTER THE TEXT ", bd=12, relief=FLAT, fg="#f7f7f7", bg="#d9534f", font=("times new roman",20,"bold"), pady=2, width=40).pack()
        self.text1 = Text(self.dataFrame, bd=12, relief=FLAT, fg="#292b2c", bg="#ffe6e6", font=("times new roman",12,"bold"), pady=2, width=80, yscrollcommand=self.scroll_y.set)
        self.text1.pack()
        self.scroll_y.config(command=self.text1.yview)
        #=========================================
        self.sideButton = LabelFrame(self.mainFrame, padx=5, pady=5, height=800, bg="#292b2c")
        self.sideButton.pack(padx=10, pady=10, anchor=N, side=LEFT, fill = X)

        self.btnFrame = LabelFrame(self.sideButton, padx=5, pady=5, height=800, bg="#d9534f")
        self.btnFrame.pack(padx=10, pady=10, anchor=W, side=TOP)



        #==============================
        def soundicon(e):
            self.splashimg = PhotoImage(file="images//soundpng.png")
            self.mycanvas.create_image(115,140,image=self.splashimg, anchor = CENTER)
            self.mycanvas.place(x = 595,y = 175, anchor = CENTER)

        def txticon(e):
            self.splashimg = PhotoImage(file="images//txtpng.png")
            self.mycanvas.create_image(115,140,image=self.splashimg, anchor = CENTER)
            self.mycanvas.place(x = 595,y = 175, anchor = CENTER)
            
        self.mycanvas = Canvas(self.sideButton, bg="#ffffff", height=300, width=225)
        self.splashimg = PhotoImage(file="images//txtpng.png")
        self.mycanvas.create_image(115,140,image=self.splashimg, anchor = CENTER)
        self.mycanvas.place(x = 595,y = 175, anchor = CENTER)
        #b2 = Label(, image = iconimg, font=("Helvitica",16,"bold"), pady=2, width=15, bg="#000", height=13) 
        #b2.place(x = 600,y = 175, anchor = CENTER)
        self.mycanvas.bind("<Enter>",soundicon)
        self.mycanvas.bind("<Leave>",txticon)

        #==============================
        self.bottomInfo = LabelFrame(self, padx=1, pady=1, height=800, bg="#f0ad4e")
        self.bottomInfo.pack(padx=10, pady=(10,0), anchor=W, side=TOP, fill = X)

        self.lbl1 = Label(self.bottomInfo, text="STOP", bd=12, relief=FLAT, fg="#f7f7f7", bg="#d9534f", font=("Helvitica",10,"bold"), width=10)
        self.lbl1.grid(row=0, column=0, padx=(8,80))

        self.lbl2 = Label(self.bottomInfo, text="<<STT>>", bd=12, relief=FLAT, fg="#f7f7f7", bg="#FF3333", font=("Helvitica",10,"bold"), width=10)
        self.lbl2.grid(row=0, column=1, padx=88)     

        self.lbl3 = Label(self.bottomInfo, text="<<AUTOMATION>>", bd=12, relief=FLAT, fg="#f7f7f7", bg="#FF3333", font=("Helvitica",10,"bold"), width=10)
        self.lbl3.grid(row=0, column=2, padx=88)

        self.lbl4 = Label(self.bottomInfo, text="<<TYPE>>", bd=12, relief=FLAT, fg="#f7f7f7", bg="#FF3333", font=("Helvitica",10,"bold"), width=10)
        self.lbl4.grid(row=0, column=3, padx=88)  

        self.lbl5 = Label(self.bottomInfo, text="<<COMPRESS>>", bd=12, relief=FLAT, fg="#f7f7f7", bg="#FF3333", font=("Helvitica",10,"bold"), width=10)
        self.lbl5.grid(row=0, column=4, padx=88)

        self.lbl6 = Button(self.bottomInfo, text="ABOUT", bd=12, relief=FLAT, fg="#f7f7f7", bg="#d9534f", font=("Helvitica",10,"bold"), width=10, command = self.aboutus)
        self.lbl6.grid(row=0, column=5, padx=(70,0))          


        self.button1 = Button(self.btnFrame, text="SAY", bd=12, relief=FLAT, bg="#292b2c", fg="#f0ad4e", font=("Helvitica",16,"bold"), pady=2, width=10, command=self.say)
        self.button1.grid(column = 0, padx=5, row = 0 ,pady=10)
        self.button1 = Button(self.btnFrame, text="CLEAR", bd=12, relief=FLAT, bg="#292b2c", fg="#f0ad4e", font=("Helvitica",16,"bold"), pady=2, width=10, command=self.clear)
        self.button1.grid(column =1, padx=5, row = 0,pady=10)
        self.rateLabel = Label(self.btnFrame, text="RATE : ", bd=12, relief=FLAT, bg="#292b2c", fg="#f0ad4e", font=("Helvitica",16,"bold"), pady=2, width=10)
        self.rateLabel.grid(row=1, column=0, padx=5,pady=10)
        self.rateEntry = Entry(self.btnFrame, bd=12, relief=FLAT, bg="#f7f7f7", font=("Helvitica",16,"bold"),width=20)
        self.rateEntry.grid(row=1, column=1, padx=5,pady=10) 
        self.rateEntry.insert(0, 200)     
        self.volumeLabel = Label(self.btnFrame, text="VOLUME : ", bd=12, relief=FLAT, bg="#292b2c", fg="#f0ad4e", font=("Helvitica",16,"bold"), pady=2, width=10)
        self.volumeLabel.grid(row=2, column=0, padx=5,pady=10)
        self.scale_var = DoubleVar()
        self.scale_var.set(50)
        self.volumeEntry = Scale(self.btnFrame, from_= 0, to = 100, orient = HORIZONTAL, length = 250, variable=self.scale_var)
        self.volumeEntry.grid(row=2, column=1, padx=5,pady=20)   
        self.voiceLabel = Label(self.btnFrame, text="VOICE : ", bd=12, relief=FLAT, bg="#292b2c", fg="#f0ad4e", font=("Helvitica",16,"bold"), pady=2, width=10)
        self.voiceLabel.grid(row=3, column=0, padx=5,pady=10)
        self.voiceOption = StringVar()           #"""Voice Option"""
        self.voiceOption.set("FEMALE")           #"""Voice Option"""
        self.voiceDrop = OptionMenu(self.btnFrame, self.voiceOption, "MALE", "FEMALE")
        self.voiceDrop.configure(width = 16, height=2, font=("Helvitica",16,"bold"))
        self.voiceDrop.grid(row=3, column=1, padx=5,pady=10)
        #===================================================================
        self.saveFrame = LabelFrame(self.sideButton, text="SAVE THE AUDIO FILE", padx=5, pady=5, height=800, bg="#d9534f")
        self.saveFrame.pack(padx=10, pady=10, anchor=S, side=BOTTOM, fill = X) 
        self.saveLabel = Label(self.saveFrame, text="ENTER THE NAME OF FILE : ", bd=12, relief=FLAT, fg="#f0ad4e", bg="#292b2c", font=("Helvitica",16,"bold"), pady=2, width=25)
        self.saveLabel.grid(row=0, column=0, padx=5,pady=10)               
        self.saveEntry = Entry(self.saveFrame, bd=12, relief=FLAT, fg="#292b2c", font=("Helvitica",16,"bold"),width=25)
        self.saveEntry.grid(row=0, column=1, padx=5,pady=10)
        self.saveButton = Button(self.saveFrame, text="SAVE", bd=12, relief=FLAT,  fg="#f0ad4e", bg="#292b2c", font=("Helvitica",16,"bold"), pady=2, width=10, command=self.save)
        self.saveButton.grid(column = 0, columnspan = 2, padx=5, row = 1 ,pady=10)


    def footerlayout(self):
        self.dataFrame = LabelFrame(self, bd=0, padx=0, pady=0)
        self.dataFrame.pack(side = BOTTOM, fill = X)
        self.footer = Label(self.dataFrame,text="Made by Sandeep Shaw\t|\tv 120.112.020\t|\t\u00A9 All right Reserved 2020",
                            relief=GROOVE,
                            bg="#ff4d4d",
                            fg="#ffffff",
                            border=0,
                            font=("times new roman",10,"bold"),
                            pady = 5
                            )
        self.footer.pack( padx = 0, pady = 0, fill = X)


#Main===================================================================================================

if __name__ == '__main__':
    AppIntro().mainloop()
    App().mainloop()

