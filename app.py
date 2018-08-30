import json
import os
import subprocess
import sys
import docker
docker_client = docker.from_env()

with open('config.json') as json_file:  
    data = json.load(json_file)

dir_path = os.path.dirname(os.path.realpath(__file__))

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
        # s = subprocess.Popen(["docker", "build", "-t", container["Name"], "."], cwd=dir_path + "/" + container["Folder"])
        docker_client.images.build(path=dir_path +'/' + container["Folder"], tag=container["Name"], rm=True)
        # print(s)
    
def __create_network():
    # s = subprocess.call(["docker", "network", "create", data["Network"]["Name"]])
    docker_client.networks.create(data["Network"]["Name"], driver="bridge")
    # print(s)

def __run():
    for container in data["Network"]["Containers"]:
        # s = subprocess.Popen(["docker", "run", "-d", "--network", data["Network"]["Name"], "--publish", container["ExternalPort"] + ":" + container["Port"], "--name", container["Name"], container["Name"]], cwd=dir_path + "/" + container["Folder"], shell=True)
        docker_client.containers.run(name=container["Name"], image=container["Name"], detach=True, network=data["Network"]["Name"], ports={container["Port"] + '/tcp': container["ExternalPort"]}, publish_all_ports=True )
        # print(s)

def __stop_and_remove_containers():
    for container in data["Network"]["Containers"]:
        s = subprocess.call(["docker", "stop", container["Name"]])
        print(s)
        s = subprocess.call(["docker", "container", "rm", container["Name"]])
        print(s)

def __remove_network():
    s = subprocess.call(["docker", "network", "rm", data["Network"]["Name"]])
    print(s)

functions = {
    'start' : start,
    'stop' : stop,
    'restart' : restart
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())