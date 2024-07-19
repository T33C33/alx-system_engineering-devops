# Creating a custom HTTP header response with Puppet.
class { 'nginx':
  # Install Nginx package
  package_ensure => 'installed',
}

file { '/etc/nginx/conf.d/custom_headers.conf':
  # Create a custom configuration file for Nginx
  ensure  => present,
  content => "add_header X-Served-By $::hostname;",
  require => Class['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  # Ensure Nginx service is running and enabled
  ensure => running,
  enable => true,
}
