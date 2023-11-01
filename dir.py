import os
import shutil
# os.mkdir("F:/Python/DemoDir")   #Create new directory in specified path
# os.mkdir("/DemoDir1")   #Create new directory in current dir
print("String format:",os.getcwd())      #Retruns current working dir
print("Binary format:",os.getcwdb())      #Retruns current working dir in binary format

# os.chdir('F://Python/DemoDir')
# print(os.getcwd())

# print(os.listdir())     # list all sub-directories

# os.mkdir("./Test")

# os.rename('Test','New Dir') #Renaming dir
# os.renames('./Test/hello.c','./DemoDir/Prog.c') #Renaming file and moving

# os.remove("./DemoDir/Test.py")  #removing file

# shutil.rmtree('./New Dir')    #Removing dir with its contents
# shutil.rmtree('./Test')    #Removing dir with its contents

# delete the empty directory "mydir"
# os.rmdir("./Test") 

#size of dir
print(os.path.getsize("dir.py"))
print(os.path.getsize("./DemoDir"))

if os.path.exists("dir.py"):
    print("Exists")
else:
    print("Not exists")

# Checking if it's a directory
if os.path.isdir("./DemoDir"):
    print("Is a directory")
else:
    print("it is not a directory")

# Checking if it's a file
if os.path.isfile("dir.py"):
    print("Is a file")
else:
    print("Is not a file")