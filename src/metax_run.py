import os

def run_metax():
    user_path = os.path.expanduser("~")
    os.chdir(user_path)
    f = open("metax_run.sh", "w")
    f.write("""\
    #! /bin/bash
    cd /opt/metax/
    ./bin/metax_web_api -f config.xml &
    """)
    f.close()
    os.system("chmod +x metax_run.sh")
    os.system("./metax_run.sh")

run_metax()
