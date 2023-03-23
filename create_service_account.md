# Service Account

## Steps to create a service account

<p align="justify">
1. On Google Cloud Platform (GCP) select the hamburger icon, then select Cloud overview, click on Dashboard and finally click on CREATE PROJECT
</p>

<p align="center">
  <img src="images\IAM_sien_project.png">
</p>

<p align="justify">
2. Click on <code>+CREATE SERVICE ACCOUNT</code>
</p>
<p align="center">
  <img src="images\create_service_account.png">
</p>
<p align="justify">
3. Choose your service account name. I chose as service account name: terraform-sien
</p>
<p align="center">
  <img src="images\terraform-sien.png">
</p>
<p align="justify">
4. Assign the role of viewer for now, and click on <code>DONE</code>
</P>

<p align="center">
  <img src="images\service_basic_viewer.png">
</p>
<p align="justify">
5.  We need to access to this service account by Google Cloud CLI, for that generate a <CODE>Manage keys</CODE>, and choose JSON file.
</p>
<p align="center">
  <img src="images\generate_key_service_account.png">
</p>

<p align="justify">
6. Save the file in the next path </p>

        cd 
        mkdir .gc

<p align="center">
  <img src="images\gc_file_json.png">
</p>

<p align="justify">
7. Transfer the JSON file to the VM instance by sftp, so type the command below:
</p>

    sftp de-zoomcamp
    mkdir .gc
    put sien-project.json


<p align="center">
  <img src="images\sftp_sien_project.png">
</p>

8.Authenticate with Google Cloud SDK

    export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/sien-project.json

    gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS


<p align="center">
  <img src="images\export_google_credentials.png">
</p>