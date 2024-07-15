#Configure a Nginx Server

# Update the packages in local server
exec { 'update-system':
  command  => '/usr/bin/apt-get update',
}

#Install the nginx package
package { 'nginx':
  ensure   => installed,
  require  => Exec['update-system']
}
# Create directories
$Base="/data"
file {["$Basedir","$Basedir/web_static", "$Basedir/web_static/releases", "$Basedir/web_static/shared", "$Basedir/web_static/releases/test/"]:
  ensure   => directory,
}
# Create a file and add content to the file
file { '/data/web_static/releases/test/index.html':
  content  => 'Holberton School',
}

# Create a symbolic link to the current folder in web_static
file { '/data/web_static/releases/test':
  ensure   => link,
  target   => '/data/web_static/current',
}
