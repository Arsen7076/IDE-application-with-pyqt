# #!/bin/bash
 
### install metax
wget https://greenhosting.am:444/db/get/metax_1.2.13.zip?id=1452a7fb-0af2-4f66-865a-2d684894b7bf -O metax.zip
unzip metax.zip
sudo rm metax.zip
sudo rm -rf /opt/metax
sudo mv metax /opt/
cd /opt/metax/
sudo apt-get install g++ make pkg-config libssl-dev
sudo apt autoremove
make -j8

### install poco
wget https://pocoproject.org/releases/poco-1.8.1/poco-1.8.1-all.tar.bz2
tar xvf poco-1.8.1-all.tar.bz2 
sudo apt-get install libpoco-dev
cd poco-1.8.1-all/
sudo make -j8 install
./configure --no-tests --no-samples --omit=CppUnit,Data,MongoDB,PageCompiler,Redis,Zip
sudo make install
make

cd ..
make setup
make

## run metax
### ./bin/metax_web_api -f config.xml 
echo "now run  <./build_term.sh>"

