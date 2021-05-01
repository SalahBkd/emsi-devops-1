#creating holberton file with the "i love puppet" string in it, plus 0744 permission and owner,group www-data
file { '/tmp/holberton':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',

}
