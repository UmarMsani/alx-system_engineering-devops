# Increases amount of traffic an Nginx server can handle

# Increases the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx service
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/'
}
