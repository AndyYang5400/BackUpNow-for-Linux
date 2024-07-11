import os
import subprocess
from io import StringIO
import sys


# change to home directory of the user
os.chdir(os.path.expanduser('~'))


# run the command in home directory and convert the command into string and split the string
proc = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
sp = proc.split()
#print(sp)


# this loop automatically detects the name of the shared folder
# shared folder has group and owner of root
for i in range (len(sp)):
    if sp[i] == 'root' and sp[i-1] == 'root':
        name_of_hdd = sp[i+5]
#print(name_of_hdd)


# this code automatically detects the name of the user in the home directory
user = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8')
user = user.strip()
#print(user)


# copy all the files and folders recursively to the shared folder using rsync
# --links copies all symlinks
# --delete deletes all files in backup that don't exist in the source
# -- exclude flags exclude all hidden files and directories in the home directory and the shared folder itself
cmd = 'rsync -a --links --delete --exclude=".*" --exclude=".*/" --exclude="' + name_of_hdd + '"' + " /home/" + user + "/" + " /home/" + user + "/" + name_of_hdd
os.system(cmd)
#print(cmd)
