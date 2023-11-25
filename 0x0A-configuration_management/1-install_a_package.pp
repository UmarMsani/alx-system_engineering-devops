# instal Flask version 2.1.0 using pip3
# Ensure pip3 is installed before attempting Flask installation

exec { 'install_flask_2.1.0':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Package['python3-pip']
}
