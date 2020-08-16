from tkinter import *
import webbrowser
import subprocess
from PIL import ImageTk,Image
import os


root = Tk()
root.title("Pipeline_setup")
root.configure(background='#272727')


#program labels
maya_img = ImageTk.PhotoImage(Image.open("F:\Julian\Pipeline\context_creator\icons\maya\hsMaya.png"))
chrome_img = ImageTk.PhotoImage(Image.open("F:\Julian\Pipeline\context_creator\icons\chrome\icon.png"))
affinity_img = ImageTk.PhotoImage(Image.open("F:\\Julian\\Pipeline\\context_creator\\icons\\affinity\\icon.png"))
blender_img = ImageTk.PhotoImage(Image.open("F:\\Julian\\Pipeline\\context_creator\\icons\\blender\\icon.png"))
nuke_img = ImageTk.PhotoImage(Image.open("F:\\Julian\\Pipeline\\context_creator\\icons\\nuke\\icon.png"))

#Program executables
Affinity_exe = 'F:\\program_files\\affinity\\Photo.exe'
maya_exe = 'C:\\Program Files\\Autodesk\\Maya2018\\bin\\maya.exe'
blender_exe = 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'
nuke_exe = 'F:\\program_files\\Nuke12.0v5\\Nuke12.0.exe --nukex --nc'
spotify = ''



def main():
    try:
        a = os.listdir('F:\Julian\Project_files')
        click = StringVar()
        click.set(a[0])
        drop = OptionMenu(root, click, *a)
        drop.config(borderwidth=0,fg='#9C9C9C')
        drop.grid(row = 0, column = 0)
        refresh_context_button.grid(row=0, column=1)
    except:
        print("Couldn't find contexts")


def launch_chrome():
    try:
        chrome = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
        webbrowser.get(chrome).open_new("https://www.messenger.com/")
    except:
        print("couldn't launch chrome")

def launch_affinity():
    try:
        subprocess.Popen(Affinity_exe)
    except:
        print("couldn't launch affinity")  

def launch_maya():
    try:
        subprocess.Popen(maya_exe)
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
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\Alembic")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\images")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\renderman")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\scenes")
            os.makedirs("F:\\Julian\\Project_files\\"+context.get()+"\\Maya\\sourceimages")
    except:
        print("couldn't create context") 


#set context

#a = os.listdir('F:\Julian\Project_files')
#click = StringVar()
#click.set(a[0])
#drop = OptionMenu(root, click, *a)

#refresh context
refresh_context_button = Button(root, command=main)
refresh_context_button.config(bg='#595959', width=15, height=1, text="Refresh Contexts")

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
context = Entry(root, borderwidth=0)
context.configure(background='#202020', fg='#9C9C9C')

create_context_button = Button(root, command=create_new_context)
create_context_button.config(bg='#595959', width=15, height=1, text="Create new context")



#set context
#drop.grid(row = 0, column = 0)

refresh_context_button.grid(row=0, column=1)

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
