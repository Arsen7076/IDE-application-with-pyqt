pip install pyqt5
sudo apt install rxvt-unicody
######
cp .Xresources ~/ 
xrdb -merge ~/.Xresources

######
sudo rm -rf /opt/metax/config.xml 
sudo cp config.xml  /opt/metax/config.xml

echo "now run  <python3 main.py>"

