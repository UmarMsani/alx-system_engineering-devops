su betty switches the current user to the user betty
whoami prints the effective username of the current user
groups prints all the groups the current user is part of
chown betty hello changes the owner of the file hello to the user betty
touch hello will create empty file called hello
chmod u+x hello to adds execute permission to the owner of the file hello
chmod u+x,g+x,o+r hello this code will adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
chmod ugo+x hello this code will adds execution permission to the owner, the group owner and the other users, to the file hello without comma
chmod 007 hello this will sets the permission to the file hello Owner: no permission at all,Group: no permission at all,Other users: all the permissions
