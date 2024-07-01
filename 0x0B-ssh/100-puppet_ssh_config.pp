# Puppet manifest to set up SSH configuration for user

# Ensure the .ssh directory exists for the user
file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Ensure the SSH configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    PasswordAuthentication no',
  match  => '^PasswordAuthentication',  # match existing line if it exists
  after  => '^Host \*$',  # place after "Host *" line if it exists
}

# Specify the identity file
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',  # match existing line if it exists
  after  => '^Host \*$',  # place after "Host *" line if it exists
}
