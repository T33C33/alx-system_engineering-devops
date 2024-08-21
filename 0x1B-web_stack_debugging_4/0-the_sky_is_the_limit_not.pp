# This Puppet manifest file is used to fix the web server setup featuring Nginx
# We need to address the issue of failed requests and aim to get them to 0

# Install the required package for ApacheBench
package { 'apache2-utils':
  ensure => installed,
}

# Configure Nginx to handle more concurrent connections
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "worker_processes auto;\nevents { worker_connections 1024; };\n",
  notify  => Service['nginx'],
}

# Restart the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Run ApacheBench to test the web server setup after the changes
exec { 'ab-test':
  command => 'ab -c 100 -n 2000 localhost/',
  path    => '/usr/bin',
  logoutput => true,
  require => Service['nginx'],
}
