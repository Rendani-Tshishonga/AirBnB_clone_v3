#!/usr/bin/env bash
# A bash script for the deployment of web_static

# We will begin by updating and installing nginx if it doesnt exist
sudo apt-get update

# We will check that nginx is installed if not install the package
PKG="nginx"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $PKG | grep "installed ok installed")
echo Checking for $PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
	echo "No $PKG. Setting up $PKG."
	sudo apt-get -y $PKG
fi

# We will create the necessary directories and files for our deployment
# of web_static.
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/tests/

# We will create a fake file to test nginx configuration
sudo echo "
<html>
	<head>
	</head>
	<body>
	Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/tests/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/tests/ /data/web_static/current

# Give ownership to the user and group for the data folder
sudo chown -R ubuntu:ubuntu /data/

# Update the nginx configuration to serve content to hbnb_static
sudo sed -i '53i \\t location \/hbnb_static {\n\t\t alias /data/web_static/current;\n}' /etc/nginx/sites-available/default

# Restart nginx to persist nginx configuration
sudo service nginx restart
