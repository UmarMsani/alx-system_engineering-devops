# Puppet manifest for fixing Apache 500 error
# Description: Fix the Apache issue causing a 500 Internal Server Error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
