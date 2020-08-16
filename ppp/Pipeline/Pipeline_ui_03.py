from tkinter import *
import webbrowser
import subprocess
from PIL import ImageTk,Image

import os
import shutil
import glob
from pathlib import PureWindowsPath
from pathlib import Path



root = Tk()
root.title("Pipeline_setup")
root.configure(background='#272727')

instal_loc = os.getcwd()
print(instal_loc)

project_paths_BC = "F:/Julian/Project_files/"
project_paths_AC = "/Maya/scenes/"



#program labels
maya_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\icons\maya\hsMaya.png"))
chrome_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\icons\chrome\icon.png"))
affinity_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\\icons\\affinity\\icon.png"))
blender_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\\icons\\blender\\icon.png"))
nuke_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\\icons\\nuke\\icon.png"))
megascans_img = ImageTk.PhotoImage(Image.open(instal_loc+"\context_creator\\icons\\megascans\\icon.png"))


#Program executables
Affinity_exe = 'F:\\program_files\\affinity\\Photo.exe'
maya_exe = 'C:\\Program Files\\Autodesk\\Maya2018\\bin\\maya.exe'
blender_exe = 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'
nuke_exe = 'F:\\program_files\\Nuke12.2\\Nuke12.2v1\\Nuke12.2.exe --nukex --nc'
spotify = ''



#Template locations

list_of_maya_files = glob.glob(instal_loc+"/templates/maya/*")
maya_template_runaway = PureWindowsPath(max(list_of_maya_files, key=os.path.getctime))
maya_template = str(maya_template_runaway).replace("\\","/")
print(list_of_maya_files)


list_of_nuke_files = glob.glob(instal_loc+"/templates/nuke/*")
nuke_template_runaway = PureWindowsPath(max(list_of_nuke_files, key=os.path.getctime))
nuke_template = str(nuke_template_runaway).replace("\\","/")

print(list_of_nuke_files)

def set_context():
    context_file = open(instal_loc+"\config\Context\context.txt", "w")

    context_file.write(click.get())
    context_file.close()
    print(click.get())


def locate_context():
    try:
        global click, drop
        a = os.listdir('F:\Julian\Project_files')
        click = StringVar()
        click.set(a[0])
        drop = OptionMenu(root, click, *a)
        drop.config(borderwidth=0,fg='#9C9C9C')
        drop.grid(row = 0, column = 0)
        
    except:
        print("Couldn't find contexts")


def launch_chrome():
    try:
        chrome = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
        webbrowser.get(chrome).open_new("https://www.messenger.com/")
    except:
        print("couldn't launch chrome")


def Launch_Megascans():
    try: 
        chrome = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
        webbrowser.get(chrome).open_new("https://quixel.com/megascans/home/")
    except:
        print("Couldn't launch megascans")

def launch_affinity():
    try:
        subprocess.Popen(Affinity_exe)
    except:
        print("couldn't launch affinity")  

def launch_maya():
    try:
        context = click.get()
        list_of_files = glob.glob(project_paths_BC+context+project_paths_AC+'*')
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file_cleanup = str(latest_file).replace("\\","/")
        subprocess.Popen([maya_exe, "-file", latest_file_cleanup])
        print(latest_file_cleanup)
    except:
        print("couldn't launch maya")  

def launch_blender():
    try:
        subprocess.Popen(blender_exe)
    except:
        print("couldn't launch blender") 

def launch_nuke():
    try:
        subprocess.Popen(nuke_exe)
    except:
        print("couldn't launch Nuke") 

def create_new_context():
    try:
        if str(context.get()) == (""):
            print("Context is empty. Unable to create context files")
        else:
            os.makedirs("F:\\Julian\\Project_files\\"+context.get())
            print("Creating..... F:\\Julian\\Project_files\\"+context.get())
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\Alembic")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\Alembic")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\images")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\images")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\renderman")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\renderman")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\scenes")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\scenes")
            maya_template_target_runaway = "F:/Julian/Project_files/"+context.get()+"/Maya/scenes/"+context.get()+"_maya_v01.ma"
            maya_template_target = str(maya_template_target_runaway).replace("\\","/")
            print(maya_template_target)
            shutil.copyfile(maya_template, maya_template_target)
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\sourceimages")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\sourceimages")


            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Nuke\\scene")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\Nuke\\scene")
            nuke_template_target = "F:/Julian/Project_files/"+context.get()+"/Nuke/scene/"+context.get()+"_nuke_v01.nknc"
            #nuke_template_target = str(nuke_template_target_runaway).replace("\\","/")
            print(nuke_template_target)
            shutil.copyfile(nuke_template, nuke_template_target)

            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\ouput\\renders")
            print("Creating..... F:\\Julian\\Project_files\\"+context.get()+"\\ouput\\renders")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\ouput\\finals")


    except:
        print("couldn't create context") 


def Archive():
    try:
        current_context = click.get()
        source = "F:/Julian/Project_files/"+current_context
        destination = "F:/Julian/Archives/"
        print("source =    "+source)
        print("destination =    "+destination)
        shutil.move(source, destination)
        print("moving........F:\\Julian\\Project_files\\"+current_context+"To..........F:\\Julian\\Archives\\")
    except:
        print("couldn't archive current job")



#Locate context
locate_context_button = Button(root, command=locate_context)
locate_context_button.config(bg='#595959', width=15, height=1, text="locate Contexts")
#Archive
Archive_button = Button(root, command=Archive)
Archive_button.config(bg='#595959', width=20, height=1, text="Archive Current project")
#set_current_context
set_context_button = Button(root, command=set_context)
set_context_button.config(bg='#595959', width=20, height=1, text="Set Context")

#general apps label
general_label = Label(root,text="General Applications", fg='#9C9C9C')
general_label.configure(background='#272727')
#chrome
chrome_button = Button(root, image=chrome_img, width=60, height=60, command=launch_chrome)
chrome_button.config(bg='#272727',borderwidth=0)


#general apps label
modelingaps_label = Label(root,text="Modeling Applications", fg='#9C9C9C')
modelingaps_label.configure(bg='#272727')
#maya
maya_button = Button(root, image=maya_img, command=launch_maya)
maya_button.config(bg='#272727',borderwidth=0)
#blender
blender_button = Button(root, image=blender_img, command=launch_blender)
blender_button.config(bg='#272727',borderwidth=0)
#Megscans
scans_button = Button(root, image=megascans_img, command=Launch_Megascans)
scans_button.config(bg='#272727',borderwidth=0)

#compositing apps label
compaps_label = Label(root,text="Compositing Applications", fg='#9C9C9C')
compaps_label.configure(bg='#272727',borderwidth=0)
#affinity
affinity_button = Button(root, image=affinity_img, command=launch_affinity)
affinity_button.config(bg='#272727',borderwidth=0)
#Nuke
Nuke_button = Button(root, image=nuke_img, command=launch_nuke)
Nuke_button.config(bg='#272727',borderwidth=0)


#Creating context entry
context = Entry(root, borderwidth=0, bg='#202020', fg='#9C9C9C')
context.configure(bg='#202020', fg='#9C9C9C')

create_context_button = Button(root, command=create_new_context)
create_context_button.config(bg='#595959', width=15, height=1, text="Create new context")



#set context

locate_context_button.grid(row=0, column=1)
Archive_button.grid(row=0, column=3)
set_context_button.grid(row=0, column=2)

#general apps
general_label.grid(row = 2, column = 0)
#chrome
chrome_button.grid(row = 3, column = 0)


#Modeling apps
modelingaps_label.grid(row = 4, column = 0)
#maya
maya_button.grid(row = 5, column = 0)
#blender
blender_button.grid(row = 5, column = 1)
#MegaScans
scans_button.grid(row = 5, column = 2)

#Photo apps
compaps_label.grid(row = 6, column = 0)
#affinity
affinity_button.grid(row = 7, column = 0)
#nuke
Nuke_button.grid(row = 7, column = 1)

#create context 
context.grid(row=8, column=0,pady=20, padx=5)
create_context_button.grid(row=8, column=1)



root.mainloop()
