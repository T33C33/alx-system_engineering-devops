# Change the OS configuration for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 4096',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  user    => 'root',
}

# Increase the maximum number of open files for the holberton user
file { '/etc/security/limits.conf':
  ensure  => 'file',
  content => "holberton hard nofile 4096\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Reload the OS configuration
exec { 'reload-os-configuration':
  command => 'sysctl -p',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  user    => 'root',
}
