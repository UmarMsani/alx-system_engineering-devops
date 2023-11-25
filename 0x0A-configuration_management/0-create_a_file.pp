# Purpose: Create a file in /tmp with specific permissions, owner, and content
#
# Puppet manifest for creating a file in /tmp with specific permissions, owner, and content

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
