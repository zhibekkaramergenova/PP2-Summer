import os
os.chdir(r'C:\Users')
os.chdir('..')ss
while 1:
    if os.path.isfile(os.getcwd()):
        print('a)delete file\nb)rename file\nc)add content to this file\nd)rewrite content of this file\ne)return to the parent directory')
        command=input()
        if command=='a':
            os.remove(os.getcwd())
        if command=='b':
            print('Print a new name for this file:')
            newname=input()
            os.rename(os.name,newname)
        if command=='c':
            with open(os.getcwd(),'a') as f:
                print('What would you like to add?')
                add=input()
                f.write(add)
        if command=='d':
            os.сhdir('..')
    if os.path.isdir(os.getcwd()):
        print('a)rename directory\nb)print number of files\nc)print number of directories\nd)list content of the directory\ne)add file to this directory\nf)add new directory to this directory')
        command=input()
        if command=='a':
            print('Print a new name for this directory:')
            newname=input()
            os.rename(os.name,newname)            
        if command=='b':
            print(len([files for files in os.listdir(os.getcwd()) if os.path.isfile(files)]))
        if command=='c':
            print(len([directory for directory in os.listdir(os.getcwd()) if os.path.isdir(directory)]))
        if command=='d':
            print(os.listdir(os.getcwd()))
        if command=='e':
            print('The name of new file:')
            filename=input()
            os.mknod(os.getcwd(),)
        if command=='f':
            print('Print the name of new directory:')
            newdir=input()
            os.mkdir(newdir)
        if command=='test':
            print(os.getcwd())
