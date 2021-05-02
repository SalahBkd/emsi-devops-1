# intalling puppet-lint version 2.1.1
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}
package { 'puppet-lint':
  ensure => '2.1.1',
}
