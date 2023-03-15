# Google Compute Engine - VM

<p align="center">
  <img src="images\google_compute_engine.png">
</p>

---

## Steps to create a virtual machine VM on Google Compute Engine 

<p align="justify">
1. On Google Cloud Platform (GCP) select the hamburger icon, then select Compute Engine, and click on <code>VM instances</code>.
</p>

<p align="center">
  <img src="images\compute_engine_vm.png">
</p>

<p align="justify">
2. Enable the Compute Engine API
</p>

<p align="center">
  <img src="images\compute_engine_api.png">
</p>

<p align="justify">
3. Generate an SSH key, to establish secure shell sessions between  this VM instance and a local computer.

><b>SSH</b>, is a network communication protocol that enables two computers to communicate and share data.

><b>SSH key</b>,  are a pair of public and private keys that are used to authenticate and establish an encrypted communication channel between a client and a remove machine over the internet.
</p>

<p align="justify">
4. Create an SSH key pair. For this I'll use <code>Git bash terminal</code>, since it allows me to use linux commands in the terminal.

For more information about how to create an SSH key pair, check out the link below
</p>

> https://cloud.google.com/compute/docs/connect/create-ssh-keys

On Windows 10 or later (Git Bash):

    ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME -b 2048

Type space when the command prompt asks you to enter passphrase

<p align="center">
  <img src="images\ssh_key.png">
</p>

<p align="justify">
5. After the step 4, you'll have the public and private ssh key in the path selected. The public key will be needed for communicating with  the VM instance.
</p>

<p align="center">
  <img src="images\ssh_ls.png">
</p>

<p align="justify">
6. Add the pubic key to the Compute Engine metadata. For this select the hamburger icon, then select Compute and click on Metadata.
</p>

<p align="center">
  <img src="images\metadata_compute_engine.png">
</p>

Then click on <code>ADD SSH KEY</code>

<p align="center">
  <img src="images\public_key_added.png">
</p>

<p align="justify">
7. Copy the content of the public key, paste it the public SSH section and click on <code>SAVE</code>. This SSH public key is just an example  then I will change it to another for security reasons.
</p>

<p align="center">
  <img src="images\cat_gcp.png">
</p>

<p align="center">
  <img src="images\ssh_key_added.png">
</p>

<p align="justify">
7. Let's create a virtual machine instance.
</p>

<p align="center">
  <img src="images\create_vm_instance.png">
</p>

But before creating a VM instance, since I currently have a Free Tier account, first I have to see the features that my virtual machine should have in the link below.

   > https://cloud.google.com/free/docs/free-cloud-features

For compute engine I can use 1 non-preemptible e2-micro VM instance per month in one of the following US regions:

- us-west1
- us-central1
- us-east1

I called my VM instance with the name <code>de-zoomcamp</code>, then I chose us-east1 because is one of the regions which I have less ping.

<p align="center">
  <img src="images\name_vm.png">
</p>

Then I chose the machien type, which is e2-micro (2vCPU,1 core, 1GB memory)
<p align="center">
  <img src="images\e2_instance.png">
</p>

Then in <code>Boot disk</code> I chose as:

- Operating system: Ubuntu
- Version: Ubuntu 20.04 LTS 
- Boot disk type: Standar persistent disk
- Size: 20GB

<p align="center">
  <img src="images\boot_disk.png">
</p>

Finally click on <code>CREATE</code>

<p align="center">
  <img src="images\finally_create_vm.png">
</p>

<p align="justify">
8. 
</p>


 
