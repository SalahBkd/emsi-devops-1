# killing killmenow process 
exec { 'kill killmenow':
  provider => 'shell',
  command  => 'pkill killmenow',
}
