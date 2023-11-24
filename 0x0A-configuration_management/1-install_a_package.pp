# Purpose: Install Flask version 2.1.0 using pip3
#
# Puppet manifest for installing Flask version 2.1.0 using pip3
# Ensure pip3 is installed before installing Flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
