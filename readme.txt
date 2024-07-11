(\_/)          (\_/)          (\_/) 
(-.-)          (-.-)          (-.-)
(___)          (___)          (___)

Thank you for using our open-source backup program, BackUpNow, or BUN.  Right out of the box, this program will automatically detect the user (you) and the shared folder that your personal files will be backed up to, and it then copies all your files and directories to that folder. Not only that, it also keeps all your files and directories in sync with the backup. If the default configuration doesn't work out the best for you, feel free to modify the source code to suit your need. I hope you enjoy using BUN and appreciate all the conveniences thar BUN brings. 



 
**** How to use ****

Setting up the program:

1. Download the program from the repository
2. Move the Python program (file ends with.py) to the your home directory
3. Install rsync (if your computer doesn't come with it). Open terminal and type "sudo apt install rsync" for Debian and Ubuntu based OSs or "sudo yum install rsync" for Redhat, CentOS, Fedora, Rocky, and AlmaLinux based OSs.


  
To run the program maunally: 

1. open terminal and type "python3 BUN.py". Make sure that the terminal is in your home directory.



To run the program automatically with Linux Cron

1. Open terminal and type "crontab -e"
2. At the bottom of the terminal editor, type "0 * * * * python3 BUN.py". This will automatically run the program every hour at 00 minute while the system is up and running. If you would like to run the program at a different time or frequency, you can visit https://crontab.guru/ to learn more about Cron. 
3. Hit ctrl + x to quit crontab terminal editor, and then hit Y to save the modification.
4. To stop Cron from automatically running the program, use command "crontab -r" to remove. 
