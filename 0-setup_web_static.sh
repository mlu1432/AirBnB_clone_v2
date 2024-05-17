#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update the package list and install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create (or recreate) the symbolic link to the test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/^\tserver_name/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

exit 0
