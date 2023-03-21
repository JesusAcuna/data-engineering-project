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

---

INFO: There are two ways to execute shell scripts:

- One way is typing <code>./file_name.sh </code>, where the shell scripts will be executed in a child process (level 2 shell) and they will return to the parent process (level 1 shell), where all the variables executed will not be.

- The second way is typing <code>source file_name.sh </code>, where the shell scripts will be executed in a parent process (level 1 shell), where all the variables executed will be.

Note that after open another terminal, the variables will be removed.

- <code>export variable</code> is used so that parent processes can inherit their variables to child processes, not the other way around.

---

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

Add the location of docker-compose to the Path, edit .bashrc file and type this:

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

<p align="justify">
6.  For installing Spark, we need first to download <code>OpenJDK 11</code> or <code>Oracle JDK 11</code> (It's important that the version 11- spark requires 8, 11 or 17)</p>

I used OpenJDK, in the link below there is a link with all the versions:

> https://jdk.java.net/archive/

> https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz

Create a spark folder, and download the tar.gz file

    cd 
    mkdir spark
    cd spark
    wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz

Untar and decompress the file 

<p align="center">
  <img src="images\tar_xzvf.png">
</p>

--- 
NOTE: it's important the order of -xzvf for executing well the command.

- x – instructs tar to extract the files from the zipped file
- z – instructs tar to decompress the files – without this, you’d have a folder full of compressed files
- v – means verbose, or to list out the files it’s extracting
- f – tells tar the filename you want it to work on
---

Add the code below, to add the location of java to the Path:

    cd 
    nano .bashrc

<p align="center">
  <img src="images\java_path.png">
</p>

Add the code below to the bottom of the file, like the image above:

    export JAVA_HOME="${HOME}/spark/jdk-11.0.2"
    export PATH="${JAVA_HOME}/bin:${PATH}"

Press Ctrl+O and then ENTER to save the file and Ctrl+X to exit from the text editor

<p align="center">
  <img src="images\which_java.png">
</p>

<p align="justify">
7. Install Spark.
</p>
<p align="justify">
Apache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface for programming clusters with implicit data parallelism and fault tolerance
</p>

You can take a look what versions are available in the link below:


> https://spark.apache.org/downloads.html

But I used this version 
> https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz

In the spark folder, download the .tgz file

    cd 
    cd spark
    wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz

Untar and decompress the file

<p align="center">
  <img src="images\tar_spark.png">
</p>

Add the code below, to add the location of Spark to the Path:

    cd 
    nano .bashrc

<p align="center">
  <img src="images\bashrc_spark.png">
</p>

Add the code below to the bottom of the file, like the image above:


    export SPARK_HOME="${HOME}/spark/spark-3.3.2-bin-hadoop3"
    export PATH="${SPARK_HOME}/bin:${PATH}"

Press Ctrl+O and then ENTER to save the file and Ctrl+X to exit from the text editor

<p align="center">
  <img src="images\which_pyspark.png">
</p>

Type <code>spark-shell</code> 

<p align="center">
  <img src="images\spark_shell.png">
</p>

Type <code>:quit</code> to exit from scala 


If you want to see more information about Spark you can check it out down below: 

> https://spark.apache.org/docs/latest/quick-start.html


---
IMPORTANT: Every time we want to use pyspark we must first export the python spark path:

    export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
    export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"

<code>py4j-0.10.9.5-src.zip </code> is variable, so you need to fin the name in your path

<p align="center">
  <img src="images\pythonpath.png">
</p>  

---



