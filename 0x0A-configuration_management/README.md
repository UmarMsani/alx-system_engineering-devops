# 0x0A. Configuration management

# Resources
Read or watch:
1. [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
2. [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
3. [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
4. [Puppet lint](http://puppet-lint.com/)
5. [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

# Requirements
General
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension .pp

# Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

# Install puppet
* $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
* $ apt-get install -y ruby-augeas
* $ apt-get install -y ruby-shadow
* $ apt-get install -y puppet
* You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

# Puppet 5 Docs

* Install puppet-lint
* $ gem install puppet-lint

# Tasks

0. Create a file
mandatory
Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet

1. Install a package
mandatory
Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0

2. Execute a command
mandatory
Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
Example:

Terminal #0 - starting my process
