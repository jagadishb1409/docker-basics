# Running Ubuntu in Docker

Once you have installed the Docker let's start by running a Ubuntu.

1. Open Command prompt in windows and then pull the Ubuntu Image: The first step is to pull the Ubuntu image from Docker Hub. 
Run the following command in a Command Prompt or Terminal window:

````console
docker pull ubuntu
````

2. Run the Container: Once you have pulled the Ubuntu image, you can run it as a container. Run the following command to start the Ubuntu container:

````console
docker run -it ubuntu
````

Output:

![Output](https://github.com/jagadishb1409/docker-basics/blob/27cfbdcefe7f87e71f1e0ef3b8a6549615d485d5/images/docker%20run.png)

3. As you can see, we are already a root user we don't need to run commands with sudo. Run the command to update packages. If it throws an error sudo not found, u can use this command to install sudo

````console
apt-get update && apt-get install sudo
````
Then run this command

````console
apt update
````

4. Once updated, u can start installing any packages you want to install

5. If you want to exit from Ubuntu use:

````console
exit
````

6. U can check which containers are running by suing command:

````console
docker ps -a
````

Output:

![Output](https://github.com/jagadishb1409/docker-basics/blob/27cfbdcefe7f87e71f1e0ef3b8a6549615d485d5/images/docker%20ps.png)

The output is the result of the 'docker ps -a' command, which lists all containers, including those that have exited. The output shows the following columns:

- **CONTAINER ID**: the unique identifier for each container.
- **IMAGE**: the image used to create the container.
- **COMMAND**: the command used to run the container.
- **CREATED**: the date and time the container was created.
- **STATUS**: the current status of the container (e.g., "Exited").
- **PORTS**: the ports exposed by the container and their bindings.
- **NAMES**: the human-readable name given to the container.

7. From these you might have already noticed that the Ubuntu container we ran has already stopped as we ran it in interactive mode, 
hence when we come out of it, it stops running
