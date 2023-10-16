import os#for list dirs
import pathlib#for extintions
import shutil#copy files
import tkinter as tk#gui
from tkinter.ttk import *
from tkinter import *

#everything is ready---
def mainrun(device_directory,phone_backup_dir):
    print("test")
    failed = []
    phone_backup_dir += "/phone_backup"
    try:
        shutil.rmtree(phone_backup_dir)
    except:
        os.mkdir(phone_backup_dir)

    def search(p):
        
        try:
            layer = os.listdir(p)#list
            layer_dirs = []
            #sort dirs and files
            for i in range(len(layer)):
                file_extension = pathlib.Path(layer[i]).suffix
                file_extension = file_extension.lower()
                try:
                    os.mkdir(phone_backup_dir+"/"+file_extension)
                except:
                    pass
                file_in_path = p+"/"+layer[i]
                if os.path.isfile(file_in_path):
                    lab.configure(text="Copying: "+file_in_path)
                    win.update()
                    shutil.copy(file_in_path,phone_backup_dir+"/"+file_extension)
                else:
                    layer_dirs.append(layer[i])
            for i in range(len(layer_dirs)):
                if p.count("/")<20:#depth limit
                    search(p+"/"+layer_dirs[i])
        except:
            failed.append(p)
            print("FAILED      ",p,"\n")


    search(device_directory)#"/run/user/1000/gvfs/mtp:host=Google_Pixel_7_2B301FDH2000S0/"

    #delete empty folders
    layer = os.listdir(phone_backup_dir)
    for i in range(len(layer)):
        try:
            os.rmdir(phone_backup_dir+"/"+layer[i])
            i -= 1
            lab.configure(text="Empty: "+phone_backup_dir+"/"+layer[i])
            win.update()
        except:
            print("NOT EMPTY", layer[i])

#get vars---
def step1():#sets device_directory
    window = tk.Tk(className = "1 of 2")
    label = tk.Label(text="Device Directory")
    frame = tk.Frame(height=100,width=1000)
    entry = tk.Entry(fg="black", bg="white", width=50)
    text = tk.Label(
        text="""Input the top of the directory tree of device (as it will look like in your file explorer)

        Example: /run/user/1000/gvfs/mtp:host=Google_Pixel_7_7A777AAA7777A7/

        starting at mtp: will NOT work.
        """
        )
    def callback():
        global device_directory 
        device_directory= entry.get()
        window.destroy()

    button = tk.Button(
        text="Ready!",
        width=10,
        height=5,
        activebackground="green",
        activeforeground = "white",
        command= callback
    )
    frame.pack()
    label.pack()
    entry.pack()
    text.pack()
    button.pack()
    window.mainloop()
def step2():#sets phone_backup_dir
    window = tk.Tk(className = "2 of 2")
    label = tk.Label(text="directory of copy folder end location ")
    frame = tk.Frame(height=100,width=1000)
    entry = tk.Entry(fg="black", bg="white", width=50)
    text = tk.Label(
        text="""Input the location where you would like the main folder to be created

        Example: /home/user/Desktop

        """
        )
    def callback():
        global phone_backup_dir 
        phone_backup_dir= entry.get()
        window.destroy()

    button = tk.Button(
        text="Ready!",
        width=10,
        height=5,
        activebackground="green",
        activeforeground = "white",
        command= callback
    )
    frame.pack()
    label.pack()
    entry.pack()
    text.pack()
    button.pack()
    window.mainloop()

#final window---
def step3():

    global win,lab
    win = tk.Tk(className = "working")
    #l1 = tk.Label(text="\n\n\n")
    l2 = tk.Label(text="\n\n\nKill by killing terminal")
    lab = tk.Label(text="press any key to start")#textvariable=status)
    
    def task_2(event):
        print("triggered")
        win.unbind('<Key>',run)
        lab.configure(text="running")
        win.update()
        mainrun(device_directory,phone_backup_dir)

    def callback():
        exit(1)

    button = tk.Button(
        text="cancel!",
        width=10,
        height=5,
        activebackground="red",
        activeforeground = "white",
        command= callback
    )
    frame = tk.Frame(height=100,width=1000)
    run = win.bind('<Key>',task_2)

        
    frame.pack()
    lab.pack()
    l2.pack()    
    mainloop()

step1()
step2()
step3()
