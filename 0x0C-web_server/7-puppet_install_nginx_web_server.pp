# File: nginx_setup.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name _;

      location / {
        root /usr/share/nginx/html;
        index index.html;
        # Return Hello World! for GET requests to the root /
        add_header Content-Type text/html;
        return 200 'Hello World!';
      }

      location /redirect_me {
        # Perform a 301 redirect
        return 301 https://www.example.com;
      }
    }
  ",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enable on boot
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
