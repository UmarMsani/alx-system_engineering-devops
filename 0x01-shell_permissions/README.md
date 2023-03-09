su betty switches the current user to the user betty.
whoami prints the effective username of the current user.
groups prints all the groups the current user is part of.
chown betty hello changes the owner of the file hello to the user betty.
touch hello will create empty file called hello.
chmod u+x hello to adds execute permission to the owner of the file hello.
chmod u+x,g+x,o+r hello this code will adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
chmod ugo+x hello this code will adds execution permission to the owner, the group owner and the other users, to the file hello without comma.
chmod 007 hello this will sets the permission to the file hello Owner: no permission at all,Group: no permission at all,Other users: all the permissions.
chmod 753 hello this script that sets the mode of the file hello to this:-rwxr-x-wx.
chmod --reference-olleh hello this will change the mode of hello the same thing as olleh.
chmod -R ugo+x . this will adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
mkdir -m 751 my_dir this code creates a directory called my_dir with permissions 751 in the working directory
chgrp school hello this will changes the group owner to school for the file hello
chown -R vincent:staff ./* changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
chown vincent:staff _hello this will changes the owner and the group owner of _hello to vincent and staff respectively
