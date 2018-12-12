import json
import os
import subprocess
import sys

# cloned and adapted from https://github.com/raghavp96/dockernetes

with open('config.json') as json_file:  
    data = json.load(json_file)

dir_path = os.path.dirname(os.path.realpath(__file__))

def build():
    __build_containers()

def start():
    __build_containers()
    __create_network()
    __run()

def stop():
    __stop_and_remove_containers()
    __remove_network()

def restart():
    stop()
    start()

def __build_containers():
    for container in data["Network"]["Containers"]:
        s = subprocess.call(["docker", "build", "-t", container["ImageName"], dir_path +'/' + container["Folder"]])
        print(s)
    
def __create_network():
    s = subprocess.call(["docker", "network", "create", "--driver", "bridge", data["Network"]["Name"]])
    print(s)

def __run():
    for container in data["Network"]["Containers"]:
        s = subprocess.call(["docker", "run", "--name", container["ContainerName"], "--network", data["Network"]["Name"], "-p", container["ExternalPort"] + ":" + container["Port"], "--detach", container["ImageName"]])
        print(s)

def __stop_and_remove_containers():
    for container in data["Network"]["Containers"]:
        s = subprocess.call(["docker", "stop", container["ContainerName"]])
        print(s)
        s = subprocess.call(["docker", "container", "rm", container["ContainerName"]])
        print(s)

def __remove_network():
    s = subprocess.call(["docker", "network", "rm", data["Network"]["Name"]])
    print(s)

functions = {
    'build' : build,
    'start' : start,
    'stop' : stop,
    'restart' : restart
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())