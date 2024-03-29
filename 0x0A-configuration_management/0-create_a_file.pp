#create a file and set owner and group and permissions
file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
