exec { 'kill':
  command => 'pkill -fkillmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
