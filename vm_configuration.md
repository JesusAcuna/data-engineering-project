# VM Configuration

## Steps to setting up the virtual machine VM on Google Compute Engine 

<p align="justify">
1. First you need to access to your VM instance
</p>

<p align="center">
  <img src="images\ssh_de_zoomcamp.png">
</p>

<p align="justify">
2. Install Anaconda, for python libraries and environments. Choose 64-Bit(x86) installer
</p>

> https://www.anaconda.com/products/distribution

Type on console to download the shell script 

    wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

---
Run the shell script

    sh Anaconda3-2022.10-Linux-x86_64.sh

<p align="center">
  <img src="images\sh_anaconda.png">
</p>

When the installation is done type the code below:

    source .bashrc 

to run the .bashrc script for uploading the environment variables:

<p align="center">
  <img src="images\source_bash.png">
</p>

<p align="justify">
3. Install <code>Docker</code>, for containerize the images that I'll create.
</p>
But before doing that, I need  update the libraries on Ubuntu

    sudo apt-get update

Now we can install docker

    sudo apt-get install docker.io

<p align="justify">
4.  If you don’t want to preface the <code>docker</code> command with <code>sudo</code>, create a Unix group called docker and add users to it. </p>

Source:
> https://docs.docker.com/engine/install/linux-postinstall/

For this you need  to create the <code>docker</code> group and add you user:

- 4.1. Create the docker group

        sudo groupadd docker

- 4.2. Add you user to the docker group

        sudo usermod -aG docker $USER

- 4.3. Log out and log back in so that your group membership is re-evaluated.

    You can also run the following command to activate the changes to groups:

        newgrp docker

- 4.4. Verify that you can run docker commands without sudo

        docker run hello-world

<p align="center">
  <img src="images\docker_run_hw.png">
</p>

<p align="justify">
5.  Install docker compose, from the latest one releases choose <code> docker-compose-linux-x86_64</code> . </p>

> https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64

Create a bin folder where I put all the executable files, then download and rename it as 'docker-compose'

    cd 
    mkdir bin
    cd bin
    wget https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -O docker-compose


Convert docker-compose file to an executable file

    chmod +x docker-compose

Add this executable file to the Path, edit .bashrc file and type this:

    cd 
    nano .bashrc

<p align="center">
  <img src="images\docker_compose_path.png">
</p>

Add the code below to the bottom of the file, like the image above:

    export PATH="${HOME}/bin:${PATH}"

Press Ctrl+O and then ENTER to save the file and Ctrl+X to exit from the text editor 

<p align="center">
  <img src="images\docker_compose_added.png">
</p>