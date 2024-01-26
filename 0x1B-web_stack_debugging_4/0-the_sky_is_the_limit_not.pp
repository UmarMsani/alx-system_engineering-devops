# Increases amount of traffic an Nginx server can handle

# Increases the ULIMIT of the default file
exec { 'fix':
    provider => shell,
    command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

# Restart Nginx service
exec { 'restart':
    provider => shell,
    command  => 'sudo service nginx restart'
}
