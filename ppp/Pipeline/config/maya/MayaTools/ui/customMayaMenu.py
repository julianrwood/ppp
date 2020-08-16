import maya.cmds as cmds
import maya.mel as mel


def customMayaMenu():
    gMainWindow = mel.eval('$temp1 = $gMainWindow')
    customMenu = cmds.menu(parent = gMainWindow, label = "Pipeline")
    shotSetup = cmds.menuItem(parent = customMenu, label = "Set Up Shot", subMenu = True)
    cmds.menuItem(parent = shotSetup, label = "Set Frame Range")
    print("Created All menus")

    

def createGlobalVariableAttributes():

    context_file = open("F:\Julian\Pipeline\config\Context\context.txt", "r")
    context = context_file.read()
    current_context = context.split(",")[0]
    project_path = "F:/Julian/Project_files/"

    if cmds.objExists("Global_shot_options"):
        result = cmds.setAttr('Global_shot_options.Current_Context', current_context, type="string")
        result = cmds.setAttr('Global_shot_options.Project_Path', project_path, type="string")
        print("Set variables")
    else:
        result = cmds.circle(name="Global shot options")
        result = cmds.setAttr('Global_shot_options.Current_Context', current_context, type="string")
        result = cmds.setAttr('Global_shot_options.Project_Path', project_path, type="string")
        Print("Created shot globals")


customMayaMenu()

print("Creating Custom menus")
createGlobalVariableAttributes()
print("Creating Global variables")