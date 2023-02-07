# Docker Basics

Getting started with Docker

Docker is a popular platform for developers to create, deploy and run applications within containers. 
Containers offer an isolated and lightweight environment for applications to run, which makes it easier to manage and deploy applications in various environments.

Here are the steps to get started with Docker on Windows:

1. Install Docker Desktop: Download and install the Docker Desktop application from the Docker website. 
It will include both the Docker Engine and Docker CLI, which are required to run containers.

2. Run Docker on Windows: After installing Docker Desktop, launch the application and log in to your Docker account. 
You should see the Docker whale icon in your system tray, indicating that Docker is running.

> ## Note
>
> If you don't have Window Subsystem for Linux
>
> - After installing docker it will recommend to download from microsoft website
>
> [Link to WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
> - After downloading WSL install and reopen the Docker


3. Pull an Image: Docker images are pre-built applications that you can use as a starting point to create your own containers. 
To get started, pull a popular image such as the "Hello World" image by running the following command in a Command Prompt or Windows Terminal window:

````console
docker pull hello-world
````

4. Run a Container: Once you have pulled an image, you can run it as a container. Run the following command to start the "Hello World" container:

````console
docker run hello-world
````

5. Explore Docker Hub: <a href="https://hub.docker.com/search?q=" target="_blank">Docker Hub</a> is a repository for Docker images. 
You can find images for a wide range of applications, from databases to web servers, and even development tools. Browse the Docker Hub to find the images you need for your project.

6. Create your own Dockerfile: A Dockerfile is a script that contains instructions for building a Docker image. 
You can use a Dockerfile to define the environment your application needs to run, including the software and libraries it requires.

7. Build your Image: Use the 'docker build' command to build an image from your Dockerfile. 
This will create a new image with the changes you specified in your Dockerfile.

With these basic steps, you are now ready to start using Docker on Windows. 
From here, you can explore the many features and benefits of Docker, including scaling, networking, and volumes. Happy containerizing!


## Docker CLI Commands

Docker provides a command line interface to interact with the Docker Engine. The following is a list of some of the commonly used Docker CLI commands with examples.

1. docker run

This command is used to run a Docker container. For example:

````console
docker run ubuntu:18.04
````

2. docker ps

This command is used to list the running containers. For example:

````console
docker ps
````

3. docker pull

This command is used to download an image from the Docker Hub. For example:

````console
docker pull ubuntu:18.04
````

4. docker images

This command is used to list the images present on the local system. For example:

````console
docker images
````

5. docker inspect

This command is used to inspect the details of a Docker container or image. For example:

````console
docker inspect ubuntu:18.04
````

6. docker logs

This command is used to view the logs of a Docker container. For example:

````console
docker logs my_container
````

7. docker stop

This command is used to stop a running Docker container. For example:

````console
docker stop my_container
````

8. docker rm

This command is used to remove a Docker container. For example:

````console
docker rm my_container
````

9. docker rmi

This command is used to remove a Docker image. For example:

````console
docker rmi ubuntu:18.04
````

10. docker cp

This command is used to copy files/folders between a Docker container and the host system. For example:

````console
docker cp my_container:/file/path/within/container /host/path/destination
````

11. docker start

This command is used to start a stopped Docker container.
````console
docker start <Container-ID>
````

These are just a few of the commonly used Docker CLI commands. To view the complete list of Docker commands, you can use the docker command followed by the --help flag.


### Up next [Running Ubuntu in Docker](https://github.com/jagadishb1409/docker-basics/tree/main/Running%20ubuntu%20in%20docker)
