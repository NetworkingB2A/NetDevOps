
## Docker
What is docker?  
Docker is a containerization platform. You can take your application and run it on any OS that can run docker. Docker image will consist of all the components you need to run an application. Docker also helps with tools to manage your containers.

### Understanding Docker
Docker containers use two capabilities in the linux kernel:  
#### Namespaces
Namespaces are essential for providing isolation for containers. Six namespaces are used for this purpose
- mnt (mountpoints): This namespace is used for mapping access to host operating system storage resources to the container process.
- pid (processes): This namespace is used to create a new process ID for an application.
- net (network): This namespace is responsible for network access and mapping communication ports.
- ipc (System V IPC): Inert-process communications controls how the application can access shared memory locations between applications within containers.
- uts (hostname): This namespace controls host and domain names, allowing unique values per process.
- user (UIDs): This namespace is used to map unique user rights to processes
#### Cgroups
Cgroups or control groups are used to mange resource consumption for each container. These values can be tweaked to limit how much resources a container can use at one time.
- Control groups provide:
  - Resource limiting
    - Resources that can be limited.
      | Resource | cgroup |
      |-|-|
      | CPU | cpu, cpuset|
      | Memory | memory|
      | Storage | blkio |
      | Network | net_cls, net_prio |
  - Prioritization
  - Accounting

#### Docker Architecture
The docker engine is the central component of the docker architecture. Docker architecture consists of three primary parts: the client, the docker host and the docker registry.
- The client is a command-line utility that talks to the REST API of the Docker daemon. The client can communicate to a local or remote docker instance.
- The Docker host is where the Docker daemon resides. The Docker daemon is a service that runs on the host operating system.
- The registry is a place to store container images; it is also known as the repository for the container infrastructure. 
![Docker Architecture](../../images/Docker%20Arch.png)

#### Using Docker

<b>Working with containers</b>
QUICK NOTE
- If you want to supply the ID of a container or a image, you only need to provide the first 5 characters of the id. 
- If you have a sql server, as soon as you destroy that container you lose all the data that was in that container. if you want to save your data even after your destroy that container, you must map a directory outside of your container.
When working with containers, the key commands are as follows:
- create: Create a container from an image
- start: start an existing container
- run {image-name}:{tag_name}
  - Running a container from an image. if you already have the image, docker will just create a container based on that local image. if you don't have the image downloaded, docker will try and pull down the image from dockhub.
  - if you just run the `docker run {image}` command you will run in attached mode and you will not be able to interact with the console. The console will be showing the output logs from the container. 
  - if you want to run the container in detached mode you would use `docker run -d {image}` this will allow you to interact with the console.
- ps
  - list running containers and some basic info. ID and name are automatically created for you.
  - if you use a `-a` option you will see all running, stopped or perviously exited containers. 
- pull {image-name}
  - This will download an image to your local machine and make it ready for docker to use.
- inspect {container-id|container-name}
  - get detailed information regarding the container.
- exec {container-id|container-name} {command}
  - this will run a command on the docker container
- images
  - This will show a list of images available locally to you. Also some details about the images will be present.
- logs {container-id|container-name}
  - Print run logs from the containers's execution.
- stop {container-id|container-name}
  - Gracefully stop running the container. You must provide the ID or the name
  - This does not remove the container, running this command means the container will still take up space.
- kill {container-id|container-name}
  - Stop the main process in the container abruptly.
- rm {container-id|container-name}
  - Delete a stopped container. you must supply the name or ID.
- rmi {image-id|image-name}
  - Deletes an docker image. Ensure that no containers are running off that image. Provide ID or name of image.



## Common run command flags
|Flag|description|
|---|---|
|-p {docker_container_port}:{docker_host_port} | port mapping |
|-d | detached mode, allows you to run the contina without watching the containers logs. useful for web apps. 
|-i| Interactive mode -it are used together frequently|
|-t| Terminal mode -it are used together frequently|
|-v {docker_host_directory}:{docker_container_directory}| Used to mount an external folder to your internal docker container.
|{image_name}:{tag_name}| used to say which image tag you would like to use. |

## Docker building blocks
![Docker building blocks](../../images/Docker%20building%20blocks.png)

<b>Dockerfiles</b>
A Dockerfile is a script that is used to create a container image to your specification. A Dockerfile is simply a text file with a structured set of commands that Docker executes while building this image. Some of the most common commands are as follows:
- FROM: Selects the base image used to start the build process or can be set to scratch to build a totally new image.
- MAINTAINER: Lets you select a name and email address for the image creator.
- RUN: creates image layers and executes commands within a container.
- CMD: Executes a single command within a container. Only one can exist in a Dockerfile.
- WORKDIR: Sets the path where the command defined with the CMD is to be executed.
- ENTRYPOINT: Executes a default application every time a container is created with the image.
- ADD: Copies the files from the local host or remotely via a URL into the container's file system.
- ENV: Set environment variables within the container.
- EXPOSE: Associates a specific port for network binding.
- USER: Sets the UID for a user that is to run the container.
- VOLUME: Sets up shareable directory that can be mapped to a local host directory.
- LABEL: Provides a label to identify the created Docker image.

<b>Docker Images</b>
When working with Docker images, you primarily use the following commands:
All start with commands start with "docker image"
- build: Builds an image form Dockerfile.
- push: Pushes a local image to an remote registry for storage and sharing.
- ls: List images stored locally.
- images: This will show a list of the local docker images.
- history: Shows the creating and build process for an image.
- inspect: Provides detailed information on all aspects of an image, including layer detail.
- rm: Deletes an image from local storage.


Actually building a docker file
- Create the docker file
- run the following command "docker build  -t appname:latest ."
- run the docker container with the following command "docker run -d -p 5000:5000  dockerfile"

Here is an example of a simple dockerfile  
<code>
FROM ubuntu:18.04  
MAINTAINER Adam Angell  
RUN apt-get update -y && apt-get install -y   python3-pip python3-dev  
CMD [ "ufw allow 5000" ]  
COPY ./requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip3 install -r requirements.txt  
COPY  ./myAPI.py /app  
ENTRYPOINT [ "python3" ]  
CMD [ "myAPI.py" ]  
</code>

Here is another example of a dockerfile
User this part to install docker
```sh
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker $USER # do this so your dont have to run docker with sudo
logout and relogin
```
```sh
FROM node:current-slim
WORKDIR /usr/scr/app
COPY package.json .
RUN npm install
EXPOSE 8111
COPY . .
CMD ["node", "server.js"]
```


Steps to add container to the dockerhub  
<code> 
docker tag "image ID"  "name of dockerhub repo":latest  
docker push "name of dockerhub repo"
</code>


FROM ubuntu:focal
WORKDIR /
RUN apt-get update
RUN apt-get install -y python3 python3-distutils python3-pip
RUN pip install virtualenvwrapper
RUN export WORKON_HOME=~/Envs
RUN mkdir -p $WORKON_HOME
RUN source /usr/local/bin/virtualenvwrapper.sh
CMD mkvirtualenv env1