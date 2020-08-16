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

#project_paths_BC = "F:/Julian/Project_files/"
project_paths_AC = "/Maya/scenes/"
project_paths_nuke = "/Nuke/scene/"


#program labels
maya_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\icons\maya\hsMaya.png"))
chrome_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\icons\chrome\icon.png"))
affinity_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\\icons\\affinity\\icon.png"))
blender_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\\icons\\blender\\icon.png"))
nuke_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\\icons\\nuke\\icon.png"))
megascans_img = ImageTk.PhotoImage(Image.open(instal_loc+"\Pipeline\context_creator\\icons\\megascans\\icon.png"))


#Program executables
chrome = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
Affinity_exe = 'F:\\program_files\\affinity\\Photo.exe'
maya_exe = 'C:\\Program Files\\Autodesk\\Maya2018\\bin\\maya.exe'
blender_exe = 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'
nuke_exe = 'F:\\program_files\\Nuke12.2\\Nuke12.2v1\\Nuke12.2.exe --nukex --nc'
spotify = ''



#Template locations

list_of_maya_files = glob.glob(instal_loc+"/Pipeline/templates/maya/*")
maya_template_runaway = PureWindowsPath(max(list_of_maya_files, key=os.path.getctime))
maya_template = str(maya_template_runaway).replace("\\","/")



list_of_nuke_files = glob.glob(instal_loc+"/Pipeline/templates/nuke/*")
nuke_template_runaway = PureWindowsPath(max(list_of_nuke_files, key=os.path.getctime))
nuke_template = str(nuke_template_runaway).replace("\\","/")


global click, project_drop, shot_drop
a = os.listdir(instal_loc+'\Project_files')
click = StringVar()
click.set(a[0])

project_drop = OptionMenu(root, click, *a)
project_drop.config(borderwidth=0,fg='#9C9C9C')
project_drop.grid(row = 0, column = 0)


shotmenu = StringVar()
#shotmenu.set("Find some shots")
shot_menu = OptionMenu(root, shotmenu, "")
shot_menu.config(borderwidth=0,fg='#9C9C9C')
shot_menu.grid(row = 0, column = 2)


def main():
    try:
        global click, project_drop
        a = os.listdir(instal_loc+'\Project_files')
        click = StringVar()
        click.set(a[0])
        project_drop = OptionMenu(root, click, *a)
        project_drop.config(borderwidth=0,fg='#9C9C9C')
        project_drop.grid(row = 0, column = 0)
    except:
        print("Couldn't find contexts")


def shots():
        global shotmenu, shot_drop
        b = os.listdir(instal_loc+"/Project_files/"+click.get()+"/")
        print(b)
        shotmenu = StringVar()
        shotmenu.set(b[0])
        shot_menu = OptionMenu(root, shotmenu, *b)
        shot_menu.config(borderwidth=0,fg='#9C9C9C')
        shot_menu.grid(row = 0, column = 2)



def set_context():
    context_file = open(instal_loc+"\Pipeline\config\Context\context.txt", "w")

    context_file.write(click.get()+","+shotmenu.get())
    context_file.close()
    print(click.get()+","+shotmenu.get())


def launch_chrome():
    try:
        webbrowser.get(chrome).open_new("https://www.messenger.com/")
    except:
        print("couldn't launch chrome")


def Launch_Megascans():
    try: 
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
        set_context()
        context = click.get()
        shot = shotmenu.get()
        list_of_files = glob.glob(instal_loc+"/Project_files/"+context+"/"+shot+project_paths_AC+'*')
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        latest_file_cleanup = str(latest_file.replace("\\","/"))
        print(latest_file_cleanup)
        subprocess.Popen([maya_exe, "-file", latest_file_cleanup])
        print("opening maya...." +latest_file_cleanup)
    except:
        print("couldn't launch maya")  

def launch_blender():
    try:
        set_context()
        subprocess.Popen(blender_exe)
    except:
        print("couldn't launch blender") 

def launch_nuke():
    try:
        set_context()
        set_context()
        context = click.get()
        shot = shotmenu.get()
        print(context)
        print(shot)
        print("1")
        list_of_nuke_files = glob.glob(instal_loc+"/Project_files/"+context+"/"+shot+project_paths_nuke+'*')
        print("1")
        latest_nuke_file = max(list_of_nuke_files, key=os.path.getctime)
        print("2")
        latest_nuke_file_cleanup = str(latest_nuke_file).replace("\\","/")
        print(latest_nuke_file_cleanup)
        

        #nuke_exe,

        #currently won't open nuke
        #subprocess.Popen(['python', '/path/to/script.py', '--some-argument'])
        subprocess.Popen(['F:/program_files/Nuke12.2/Nuke12.2v1/Nuke12.2.exe', '--nc', '--nukex', latest_nuke_file_cleanup+''],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        #subprocess.Popen([latest_nuke_file_cleanup])
        #print(latest_nuke_file_cleanup)
        
        
        #subprocess.Popen(nuke_exe)
    except:
        print("couldn't launch Nuke") 



def create_new_context():
    try:
        if str(context.get()) == (""):
            print("Context is empty. Unable to create context files")
        else:
            print("0")
            desired_context = context.get()
            desired_shot_count = int(shot_count.get())
            print(desired_context)
            print(desired_shot_count)        
            desired_context1 = desired_context.replace(" ","_")
            sequence_abv = desired_context1[0] + desired_context1[1] + desired_context1[2]
            print(sequence_abv)
            

            a = 00
            for i in range(0,desired_shot_count):
                 
                b = a + 10
                a = b
                seq_name = instal_loc+"/Project_files/"+desired_context1+"/"+ sequence_abv+"_"+str(a)
                project_name = instal_loc+"/Project_files/"+desired_context1+"/"
                print(seq_name)
                os.makedirs(seq_name+"\\Maya\\Alembic")
                print("Made some alembic folders")
                os.makedirs(seq_name + "\\Maya\\images")
                os.makedirs(seq_name + "\\Maya\\renderman")
                os.makedirs(seq_name + "\\Maya\\scenes")
                maya_template_target_runaway = seq_name +"/Maya/scenes/"+desired_context1+"_maya_v01.ma"
                print(maya_template_runaway)
                
                maya_template_target = str(maya_template_target_runaway).replace("\\","/")
                print(maya_template)
                print(maya_template_target)
                shutil.copyfile(maya_template, maya_template_target)
                os.makedirs(seq_name + "\\Maya\\sourceimages")
                os.makedirs(seq_name + "\\Nuke\\scene")
             
                nuke_template_target_runaway = seq_name +"/Nuke/scene/"+desired_context1+"_nuke_v01.nknc"
                nuke_template_target = str(nuke_template_target_runaway).replace("\\","/")
                print(nuke_template_target)
                print(nuke_template)
                shutil.copyfile(nuke_template, nuke_template_target)
                os.makedirs(seq_name + "\\Plate")


                os.makedirs(seq_name + "\\output\\renders")
                os.makedirs(seq_name + "\\output\\finals")
                main()

        os.makedirs(project_name + "\\cut\\Premiere")
        os.makedirs(project_name + "\\"+sequence_abv+"_seq\\Nuke\\scene")
        print("1")
        seq_nuke_copy = project_name+"/"+sequence_abv+"_seq/Nuke/scene/"+desired_context1+"_nuke_v01.nknc"
        print(seq_nuke_copy)
        shutil.copyfile(nuke_template, seq_nuke_copy)
    except:
        print("couldn't create context") 


def Archive():
    try:
        current_context = click.get()
        source = instal_loc+"/Project_files/"+current_context
        destination = instal_loc+"/Archives/"
        print("source =    "+source)
        print("destination =    "+destination)
        shutil.move(source, destination)
        print("moving........"+instal_loc+current_context+"To.........."+instal_loc+"\\Archives\\")
    except:
        print("couldn't archive current job")



#Locate context
locate_context_button = Button(root, command=main)
locate_context_button.config(bg='#595959', width=15, height=1, text="locate Projects")

#locate shot
locate_shot_button = Button(root, command=shots)
locate_shot_button.config(bg='#595959', width=15, height=1, text="locate Shots")



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
new_project_name_label = Label(root,text="New Project Name", fg='#9C9C9C')
new_project_name_label.configure(bg='#272727',borderwidth=0)
new_project_sequence_count_label = Label(root,text="Shot Count", fg='#9C9C9C')
new_project_sequence_count_label.configure(bg='#272727',borderwidth=0)


context = Entry(root, borderwidth=0, bg='#202020', fg='#9C9C9C')
shot_count = Entry(root, borderwidth=0, bg='#202020', fg='#9C9C9C')
context.configure(bg='#202020', fg='#9C9C9C')
shot_count.configure(bg='#202020', fg='#9C9C9C')

create_context_button = Button(root, command=create_new_context)
create_context_button.config(bg='#595959', width=15, height=1, text="Create new context")



#set context

locate_context_button.grid(row=0, column=1)
locate_shot_button.grid(row=0, column=3)
set_context_button.grid(row=0, column=4)
Archive_button.grid(row=0, column=5)

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
new_project_name_label.grid(row = 8, column = 0)
new_project_sequence_count_label.grid(row = 8, column = 1)


context.grid(row=9, column=0,pady=20, padx=5)
shot_count.grid(row=9, column=1,pady=20)

create_context_button.grid(row=9, column=2)



root.mainloop()
