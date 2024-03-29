#Ensure Flask package is installed with the specified version

exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
}
