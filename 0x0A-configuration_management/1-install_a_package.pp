#Ensure Flask package is installed with the specified version

exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0',
}
