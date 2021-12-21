# IDE-application-with-pyqt
New IDE application with server and pyqt
This is the README file of Metax IDE project developed by PontemLab

Contents
  1. CREATORS
	2. REQUIREMENTS
	3. COMPILATION
	4. USAGE
	5. DOCUMENTATION


1. CREATORS
Margaryan Arsen
Musikyan Tsolak
Sedrakyan Vahe
Chaloyan David
Hokhanyan Khachatur
Vardazaryan Hayk

2. REQUIREMENTS

Metax IDE requirements:
The following tools and libraries should be installed before the compilation.

Tools:
	g++
	make
	pkg-config
	Metax 1.2.13
	rxvt
Libraries:
	libss
	libssl-dev
	POCO 1.8.1
	PyQt5

To install requirements on Ubuntu Linux:

3. COMPILATION

Do the following steps to compile the METAX IDE

cd /opt/metax/src

./build_metax.sh
./build_term.sh

4. USAGE

cd /opt/metax/src
python3 main.py
