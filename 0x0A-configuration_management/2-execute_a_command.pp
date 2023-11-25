# Purpose: Terminate a process named 'killmenow'
#
# Puppet manifest for using exec resource to kill a process

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin:/usr/local/bin', # Specify the necessary paths if required
}
