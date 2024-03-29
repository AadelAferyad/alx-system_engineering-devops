#Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmeno':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}
