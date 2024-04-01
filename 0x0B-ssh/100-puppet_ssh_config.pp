#make change of configration file

file_line { 'file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  line   => 'PasswordAuthentication no',
}
