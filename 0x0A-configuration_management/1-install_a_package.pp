#Ensure Flask package is installed with the specified version
exec { 'flask':
    command => '/usr/bin/env pip3 install flask==2.1.0',
}
