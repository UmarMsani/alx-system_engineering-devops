# instal Flask version 2.1.0 using pip3
# Ensure pip3 is installed before attempting Flask installation

exec { 'install_flask_2.1.0':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Package['python3-pip'],
}

file { '/usr/local/bin/flask_check':
  ensure  => present,
  require => Exec['install_flask_2.1.0'],
}

exec { 'check_flask_version':
  command     => '/usr/bin/pip3 show Flask | grep "Version: 2.1.0" > /usr/local/bin/flask_check',
  refreshonly => true,
  subscribe   => File['/usr/local/bin/flask_check'],
  notify      => Exec['verify_flask_version'],
}

exec { 'verify_flask_version':
  command     => '/usr/local/bin/flask --version',
  refreshonly => true,
}
