Linux shell basic commands
pwd prints the absolute path name of the current working directory
ls Display the contents list of your current directory
cd /root  changes the working directory to the user’s home directory
ls -l Display current directory contents in a long format
ls -la Display current directory contents, including hidden files starting with . Use the long format
ls -na Display current directory contents in Long format, with user and group IDs displayed numerically, And hidden files
mkdir /tmp/my_first_directory Create a script that creates a directory named my_first_directory in the /tmp/ directory
mv /tmp/betty /tmp/my_first_directory/ Move the file betty from tmp to tmp my_first_directory
rm /tmp/my_first_directory/betty to delect The file betty is in tmp my_first_directory
rm -r /tmp/mt_first_directory To Delete the directory my_first_directory that is in the tmp directory
cd - to changes the working directory to the previous one
ls -la . .. /boot to lists all files even ones with names beginning with a period character which are hidden in the current directory and the parent of the working directory and the boot directory in log
file /tmp/ianafile prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script
ln -s /bin/ls ./ls to create symbolic link
ln -s /bin/ls _ls_ to create symbolic link in the current directory
