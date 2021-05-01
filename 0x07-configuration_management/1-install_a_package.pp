# intalling puppet-lint version 2.1.1
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'puppet-lint':
  install_options => ['-v','2.1.1'],
  ensure          => 'installed',
}
