
## Cloud  

NIST defines cloud as three main category with additional subcategories. They are:
- Essential characteristics
  - Broad network access
  - Rapid elasticity
  - Measured service
  - On-demand self-service
  - Resource Pooling
- Service models
  - SaaS
  - PaaS
  - IaaS
- Deployment models
  - Public
  - Private
  - Hybrid
  - Community

Some benefits of containers include:
- Consistency for deployment automation
- Simplified lightweight image files measured in MB rather then GB
- Providing only what the app needs and nothing else
- Ability to work the same production as in a developer's laptop
- Ability to deploy applications in seconds

Notes about serverless:
- Of course there is still a server. but you dont need to work about the server at all.
- This is the idea that you write code, upload the code to a server and the server just runs the code.
- Works well if you just need a bit of code to run periodically.
- Can also be called function as a service.
- Advantages of serverless deployment
  - Cost
  - Scalability
  - Easier to use and write code for
- Disadvantages of serverless deployment
  - Latency to spin up the service when needed
  - Resource constraints
  - Monitoring and debugging
  - Security and privacy
  - Vendor lock-in

## DevOps

DevOps has five guiding principles
- Culture
  - For DevOps to work, organizational culture must change. 
  - This is the most important and more difficult part of DevOps
- Automation
- Lean
  - Reducing wasted efforts and streamlining the process.
- Measurement
  - If you never measure your results, you will never know what to improve or if you are improving.
- Sharing
  - Feedback and sharing is key to reach the ultimate goal.

### Putting devops into practice. The Three ways
First way: Systems and flow  
The following are key characteristics of the first way
- Make work visible
- Reduce batch sizes
- Reduce intervals of work
- Build in quality by preventing defects from being passed downstream 

Second way: Feedback loop
The following are key characteristics of the second way
- Amplify feedback to prevent problems from happening again
- Enable faster detection and recovery
- See problems as they occur and swarm them until they are fixed
- Maximize opportunities to learn and improve

Third way: Continuous Experimentation and Learning
The following are key characteristics of the third way
- Conduct dynamic, disciplined experimentation and risk taking
- Define time to fix issues and make the system better
- When things go wrong, don't point fingers
- Create shared code repositories

### DevOps Implementation
The stages for implementing DevOps generally follows these steps:
- Continuous integrations
  - This part involves merging dev code with production code and introduces automated testing.
- Continuous delivery
  - This stage involves a software package delivery mechanism for releasing code to staging for review and inspection.
- Continuous deployment
  - This stage relies on continuous integration and continuous delivery to automatically replace code into production as soon as it is ready.


## Docker
What is docker?  
Docker is a containerization platform. You can take your application and run it on any OS that can run docker. Docker image will consist of all the componants you need to run an application. Docker also helps with tools to manage your containers.

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

#### Docker Architecture
The docker engine is the central component of the docker architecture. Docker architecture consists of three primary parts: the client, the docker host and the docker registry.
- The client is a command-line utility that talks to the REST API of the Docker daemon. The client can communicate to a local or remote docker instance.
- The Docker host is where the Docker daemon resides. The Docker daemon is a service that runs on the host operating system.
- The registry is a place to store container images; it is also known as the repository for the container infrastructure. 

#### Using Docker

<b>Working with containers</b>
When working with containers, the key commands are as follows:
- create: Create a container from an image
- start: start an existing container
- run: create a new container and start it.
- ls: list running containers.
- inspect: get detailed information regarding the container.
- logs: Print run logs from the containers's execution.
- stop: Gracefully stop running the container.
- kill: Stop the main process in the container abruptly.
- rm: Delete a stopped container.

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
- build: Builds an image form Dockerfile.
- push: Pushes a local image to an remote registry for storage and sharing.
- ls: List images stored locally.
- history: Shows the creating and build process for an image.
- inspect: Provides detailed information on all aspects of an image, including layer detail.
- rm: Deletes an image from local storage.