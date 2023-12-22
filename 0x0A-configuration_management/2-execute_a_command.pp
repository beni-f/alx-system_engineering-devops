# Kill the process called killmenow
exec { 'pkill killmenow':
  path    => '/usr/bin',
}