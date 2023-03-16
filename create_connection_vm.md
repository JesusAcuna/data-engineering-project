# VM connection

<p align="justify">
Whenever you want to connect to this instance locally, type the code below. 
</p>

    ssh -i  ~/.ssh/KEY_FILENAME USERNAME@EXTERNAL_IP

<code>KEY_FILENAME</code> and <code>USERNAME</code> is the key file name and username respectively that I entered in the part [`CREATE VM INSTANCE`](./create_vm_instance.md) to create the SSH key

<code>EXTERNAL_IP</code> is the external IP showed in the [4.2. SECTION](#42-creating-a-vm-on-google-compute-engine)

<p align="left">
  <img src="images\ssh_i.png">
</p>

**(IMPORTANT)** To avoid typing that command every time that we want to connect to the VM instance, let's create a <code>config</code> file for easy access.

<p align="center">
  <img src="images\touch_config.png">
</p>

In the config file type the command below:

    Host de-zoomcamp
        HostName 35.227.8.253
        User jesus
        IdentityFile c:/Users/jesus/.ssh/gcp


- Host: ALIAS
- HostName: EXTERNAL IP
- User: USERNAME
- IdentityFile: ~/.ssh/KEY_FILENAME


Type <code>ssh de-zoomcamp</code> to connect to the VM instance. 

<p align="center">
  <img src="images\ssh_de_zoomcamp.png">
</p>

Every time we want to turn on the VM instance, the external IP will change, so we will need to change the argument in <code>HostName</code> in the config file.









