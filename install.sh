#!/bin/sh

echo "Copying plugin data to ~/.local/share/gedit/plugins"

cp hot_reloader.py hot_reloader_info.plugin ~/.local/share/gedit/plugins

echo "Copying Shell Script to ~"

cp hot_reload_flutter ~

cd

echo "Attempting to make hot reloader shell script executable ..."
sudo chmod 777 hot_reload_flutter

echo "All Set!"

echo "Remeber, to launch your flutter project with --pid-file /tmp/flutter.pid flag"
