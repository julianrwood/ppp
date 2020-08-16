import os
import glob
import subprocess
list_of_files = glob.glob('F:/Julian/Project_files/testing/Maya/scenes/*')
latest_file = max(list_of_files, key=os.path.getctime)
latest_file_cleanup = str(latest_file).replace("\\","/")

maya_exe = "C:\\Program Files\\Autodesk\\Maya2018\\bin\\maya.exe"
subprocess.call([maya_exe, "-file", latest_file_cleanup])

#b = print(latest_file_cleanup)


#os.system('cmd /k b ')
print(latest_file_cleanup)



#file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "C:/Users/Julian/Desktop/ney/scenes/ney_v01.ma";addRecentFile("C:/Users/Julian/Desktop/ney/scenes/ney_v01.ma", "mayaAscii");

