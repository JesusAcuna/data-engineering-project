# Nutritional Status Information System - SIEN 

<p align="center">
  <img src="images\SIEN.png">
</p>

---

<p align="justify">
In 2003, the INS/CENAN, which is the National Institute of Health(Perú), implemented the Nutritional Status Information System - SIEN, based on a continuous and systematic process that records, processes, reports and analyzes information on the nutritional status of children under five years of age and pregnant women, who attend to health establishments at the first level of care of the Ministry of Health.
</p>

---
## Index

- 1.[Description of the problem](#1-description-of-the-problem)
- 2.[Objective](#2-objective)
- 3.[Data description](#3-data-description)
- 4.[Instructions on how to create the project](#7-instructions-on-how-to-create-the-project)
  - 4.1.[Setting up Google Cloud Platform account](#41-setting-up-google-cloud-platform-account)
  - 4.2.[Creating a VM on Google Compute Engine](#42-creating-a-vm-on-google-compute-engine)
  - 4.3.[VM instance connection configuration](#43-vm-instance-connecntion-configuration)
  - 4.4.[Setting up VM instance](#44-setting-up-instance)


- 5.[Alternative A - Local](#5-alternative-a---local)
  - 5.1.[Creating a docker-compose](#51-creating-a-docker-compose)
  - 5.2.[Running a docker-compose](#52-running-a-docker-compose)
  - 5.3.[Port Forwarding](#53-port-forwarding)
  - 5.4.[Testing with little data](#54-testing-with-little-data)
  - 5.5.[Orchestrating with prefect](#55-orchestrating-with-prefect)


- 6.[Alternative B - Cloud](#6-alternative-b---cloud)
  - 6.1.[Setting up Terraform ](#61-setting-up-terraform)
  - 6.2.[Edit Permissions](#62-edit-permissions)
  - 6.3.[Installing Terraform](#63-installing-terraform)
  - 6.4.[Setting up Terraform files](#64-setting-up-terraform-files)
  - 6.5.[Orchestrating with prefect](#65-orchestrating-with-prefect)
  - 6.6.[Deployment with prefect](#66-deployment-with-prefect)



- 10.[References](#10-references)
---
## Structure of the repository

The repository contains the next files and folders:

- `Kitchenware_data`: directory with 4 subdirectories: 
    - `Full_train`: Image training set
    - `Test`      : Image testing set
    
    By modifying the train size of `Full_train`, you can get a small set for a fast training 
    
    - `Train`     : Small image training set from `Full_train`
    - `Val`       : Small image testing set from `Full_train`
- `data`: directory of image dataset

## 1. Description of the problem

<p align="justify">
The improvement of child and pregnant women health indicators correspond to equity measures, since these groups are the most vulnerable, so their monitoring and analysis is a priority in the development of the nation. In children under five years of age, the monitoring of indicators of chronic, global and acute malnutrition, overweight, obesity and anemia are the most relevant from the point of view of nutritional status, likewise in pregnant women are the deficit of weight, overweight and anemia, and how they affect childbirth and the newborn.
</p>

<p align="justify">
Among the indicators that are evaluated in children under fiver years of age "<b>Chronic child malnutrition</b>" is one of the main public health problems in Perú, which negatively affects their health and education, and therefore their future. 
</p>
<p align="justify">
During the period from 2009 to 2021 <b>chronic child malnutrition</b> has been slowly reduced from 25.2% to 15.1%, about 1% per year.
</p>

<div align="center">

ADD GRAPHIC

| Indicators           | 2009    | 2020    | 2021   |
| :------------------: | :-----: | :-----: | :----: |
| Chronic Malnutrition | 25.2%   | 16.5%   |  15.1% |
| Acute Malnutrition   | 3.0%    | 1.6%    |  1.8%  |
| Global Malnutrition  | 5.5%    | 3.5%    |  3.8%  |

</div>

Source:
> https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf

## 2. Objective

<p align="justify">
Develop a data infrastructure including data pipelines and a dashboard for users to perform advanced analytics, this is for the purpose of generating timely information each month on the nutritional status of the population, for decision-making and intervention planning at the local, regional and that contribute to improve the quality of life in Perú. 
</p>

Workflow:

- Select a dataset.
- Create a pipeline for processing this dataset and putting it to a data-lake.
- Create a pipeline for moving the data from the lake to a data warehouse.
- Transform the data in the data warehouse: prepare it for the dashboard.
- Create a dashboard.

## 3. Data description

<p align="justify">
The source of information is secondary, it corresponds to the information registered in the Clinical Histories of the Health Establishments of the Ministry of Health(Perú). The processing and cleaning of the databases, generation of reports through tables and graphs, management reports are the responsibility of the INS/CENAN, financed by the articulated nutritional budget program (PAN).
</p>

*** CHANGE  ***

<b>Analysis Unit:</b>

- <b>Children under five years of age</b>
- <b>Pregnant women</b>

<b>Collected Variables:</b>

- <b>Children under five years of age</b>: weight, height, age, hemoglobin or hematocrit
- <b>Pregnant women</b>: current weight, height, age, pre-pregnancy weight, gestational week, type of pregnancy

<b>Indicators:</b>
 
- <b>Children under five years of age</b>:
  - Height/Age (Chronic Malnutrition)
  - Weight/Age (Global Malnutrition)
  - Weight/Height (Acute malnutrition, overweight, obesity)
  - Hemoglobin and Hematocrit (mild, moderate and severe anemia)
- <b>Pregnant women</b>: 
  - Low, adequate and high weight gain, according to IMC Pre-pregnancy Weight
  - Hemoglobin and Hematocrit (mild, moderate and severe anemia)

<b>Reference standards</b>

- <b>Nutritional status of children under five years of age</b>
  - Growth patterns OMS 2006
- <b>Nutritional status of pregnant women</b>:
emy Press, 2009.
- <b>Diagnosis of Anemia</b>: OMS-MINSA ranges. Prevention and Control of Iron Deficiency Lima, 2000. Adapted according to altitude.


## 4. Instructions on how to create the project


### 4.1. Setting up Google Cloud Platform account

In this part I created my project called <code>sien-project</code>, if you want to see the steps to create a project, just check out the instructions here [`CREATE GCP PROJECT`](./create_gcp_project.md).

<p align="center">
  <img src="images\new_project_gcp.png">
</p>

### 4.2. Creating a VM on Google Compute Engine

For this part I created my VM instance called <code>de-zoomcamp</code>, if you want to see the steps to create a VM instance, just check out the instructions here [`CREATE VM INSTANCE`](./create_vm_instance.md).

<p align="center">
  <img src="images\vm_instance_name.png">
</p>

### 4.3. VM instance connection configuration

In this part I created a config file with the alias <code>de-zoomcamp</code> to connect to the VM instance , if you want to see these steps, just check out the instructions here [`CREATE CONNECTION VM`](./create_connection_vm.md).

<p align="center">
  <img src="images\ssh_de_zoomcamp.png">
</p>

### 4.4. Setting up VM instance

For this part I installed in the virtual machine instance:

- Anaconda environment
- Docker 
- Docker-compose 
- Java
- Spark

If you want to see the steps above, check it out here [`VM CONFIGURATION`](./vm_configuration.md)


## 5. Alternative A - Local

After finishing point [4.4. Setting up VM instance](#44-setting-up-instance) we need to create an open-source relational database managemnet system that emphasizes SQL extensibility and compliance (<code>POSTGRESQL</code>).

<p align="justify">
And a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well (<code>PGADMIN</code>).</p>

### 5.1. Creating a docker-compose 

I created a subfolder data-engineering/baics_setup

    cd 
    mkdir data-engineering
    cd data-engineering
    mkdir basics_setup
    touch docker-compose.yaml

that contains the <code>docker-compose.yaml</code> file, and its content is:

    services:
      pgdatabase:
        image: postgres:13
        environment:
          - POSTGRES_USER=root
          - POSTGRES_PASSWORD=root
          - POSTGRES_DB=sien
        volumes:
          - "./sien_postgres_data:/var/lib/postgresql/data:rw"
        ports:
          - "5432:5432"
      pgadmin:
        image: dpage/pgadmin4
        environment:
          - PGADMIN_DEFAULT_EMAIL=admin@admin.com
          - PGADMIN_DEFAULT_PASSWORD=root
        volumes:
          - "./pgadmin_conn_data:/var/lib/pgadmin:rw"
        ports:
          - "8080:80"

The structure of the localhost would look like this


<p align="center">
  <img src="images\docker_compose_structure.png">
</p>

### 5.2. Running a docker-compose 
<p align="justify">
To run the docker-compose, just type <code>docker-compose up</code>, but before doing that, we first need to set up the permissions of two directories, where all the dependencies will be mapped, both local and container.
</p>

    cd 
    cd data-engineering/basics_setup
    mkdir pgadmin_conn_data
    mkdir sien_postgres_data

    sudo chown 5050:5050 pgadmin_conn_data
    sudo chown 5050:5050 sien_postgres_data

<p align="center">
  <img src="images\files_permissions.png">
</p>


After doing the code above, type:

    docker-compose up

If you want to verify that that docker container is running type 

    docker ps

<p align="center">
  <img src="images\docker_compose_ps.png">
</p>

And to close the container, type:

    docker-compose down 

### 5.3. Port Forwarding

To use Visual Studio Code, we can connect to a remote machine using SSH. check the instructions here to create a [`REMOTE SSH`](./remote_ssh.md).

Let's port-forwarding port 5432 for the server, and 8080 for pg-admin

<p align="center">
  <img src="images\port_forwarding.png">
</p>

<p align="justify">
In your prefer favorite browser type: http://localhost:8080/ for accessing to the pg-admin, 
</p>

Log in: 

- user_default_email = admin@admin.com
- pgadmin_default_password = root

Create a Server
<p align="center">
  <img src="images\name_server.png">
</p>

Connection:
 
- hostname=pgdatabase
- port=5432
- postgres_user=root
- postgres_password=root

<p align="center">
  <img src="images\connection_pgadmin.png">
</p>

<p align="center">
  <img src="images\pgadmin_browser.png">
</p>

### 5.4. Testing with little data


<code>'ingest_data.py'</code> is a pipeline which does the webscraping, downloads xlsx files, and uploads the tables to the postgresql server. So I used this pipeline to test the process of extraction and load with little data

<code>'read_parameters_2'</code> is a script that has the parameters to be able to convert an excel file to several dataframes, since a single excel file contains several sheets.

First install psycopg2 

    conda install psycopg2

Run <code>ingest_data.py</code> in console:

    URL="https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS"
    python ingest_data.py \
      --user root \
      --password root \
      --host localhost \
      --port 5432 \
      --db sien \
      --URL ${URL} \
      --years 2022


<p align="center">
  <img src="images\python_ingest_data.png">
</p>

<p align="center">
  <img src="images\pg_admin_ingest_data.png">
</p>

**(OPTIONAL)** Alternatively you can run the pipeline into a docker .

Dockerfile

    FROM python:3.9

    RUN pip install pandas sqlalchemy psycopg2 requests beautifulsoup4 openpyxl lxml
    WORKDIR /app

    COPY ingest_data.py ingest_data.py
    COPY read_parameters_2.py read_parameters_2.py

    ENTRYPOINT [ "python","ingest_data.py" ]

- Build

      docker build --rm -t sien_ingest:v001 .

- Entrypoing bash

      docker run --rm -it --entrypoint bash sien_ingest:v001

- Run   

      URL="https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS"
      docker run --rm -it \
        --network basics_setup_default \
        sien_ingest:v001 \
        --user root \
        --password root \
        --host basics_setup-pgdatabase-1 \
        --port 5432 \
        --db sien \
        --URL ${URL} \
        --years 2022


### 5.5. Orchestrating with prefect

Localte inside the prefect/local folder, and run the below codes:

Create an environment

    conda create -n zoomcamp

And activate that environment

    conda activate zoomcamp

If you don't have pip, install it

    conda install pip

Intall the requirements

    pip install -r requirements


Also we need more libraries

    pip install beautifulsoup4 openpyxl lxml

<code>'ingest_data_2.py'</code> is a pipeline orchestrated by Prefect, which does the webscraping, downloads xlsx files, tranform xlsx files to dataframes, and uploads the tables to the postgresql server.


Use prefect orion to visualize all the flow and tasks, which the pipeline has.

    prefect orion start

<p align="center">
  <img src="images\orion_prefect.png">
</p>


Check out the dashboard 

<p align="center">
  <img src="images\prefect_orion_dashboard.png">
</p>

Create a block -> SQLAlchemyConnector

<p align="center">
  <img src="images\prefect_orion_block.png">
</p>

You can run it 

    python ingest_data_2.py

<p align="center">
  <img src="images\prefect_ingest_data_2.png">
</p>



## 6. Alternative B - Cloud

After finishing point [4.4. Setting up VM instance](#44-setting-up-instance) we need to create an open-source infrastructure-as-code software tool(<code>Terraform</code>).

<p align="justify">
Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.
</p>


### 6.1. Creating service account

In this part I created my service account called <code>terraform-sien</code>, if you want to see the steps to create a project, just check out the instructions here [`CREATE SERVICE ACCOUNT`](./create_service_account.md).

<p align="center">
  <img src="images\export_google_credentials.png">
</p>

### 6.2. Edit Permissions 

Let's add more permissions such as:

- Storage Admin
- Storage Object Admin
- Big Query Admin

In IAM section edit the terraform-sien service account.

<p align="center">
  <img src="images\edit_permissions_terraform_sien.png">
</p>

Click on <code>+ ADD ANOHTER ROLE</code> and add the Roles below:
<p align="center">
  <img src="images\more_permissions_terraform.png">
</p>

Activate two APIs

- Identity and Access Management (IAM) API
- IAM Service Account Credentials API

<p align="center">
  <img src="images\IAM_API.png">
</p>

<p align="center">
  <img src="images\IAM_API_2.png">
</p>

### 6.3. Installing Terraform 

Install terraform, in the description below is the link

> https://developer.hashicorp.com/terraform/downloads

Select Binary donwload for Linux

> https://releases.hashicorp.com/terraform/1.4.2/terraform_1.4.2_linux_amd64.zip

Type the commands below to download it and execute it:

    cd
    cd bin 
    wget https://releases.hashicorp.com/terraform/1.4.2/terraform_1.4.2_linux_amd64.zip
    sudo apt-get install unzip
    unzip terraform_1.4.2_linux_amd64.zip

<p align="center">
  <img src="images\unzip_terraform.png">
</p>

Terraform is already in the Path, so I don't need to add it.
<p align="center">
  <img src="images\terraform_version.png">
</p>

Google Cloud SDK Authentication

    export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/sien-project.json

    gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

Alternatively, you can authenticate using OAuth

    gcloud auth application-default login

### 6.4. Setting up Terraform files

In this part I used a remote SSH for modifying terraform files, so you can take a look how to create a remote SSH  here [`REMOTE SSH`](./remote_ssh.md). 

First I created a directory called terraform withe three files:

- .terraform-version 
- main.tf
- variables.tf

Locate in the terraform directory to initialize and install, type:

    terraform init

<p align="center">
  <img src="images\terraform_init.png">
</p>

Match changes against the previous state

    terraform plan

<p align="center">
  <img src="images\terraform_plan.png">
</p>

Apply changes to cloud

    terraform apply


<p align="center">
  <img src="images\terraform_apply.png">
</p>

If tou want to remove your stack from cloud, you can type 

    terraform destroy

### 6.5. Orchestrating with prefect

Localte inside the prefect/cloud folder, and run the below codes:

Create an environment

    conda create -n zoomcamp

And activate that environment

    conda activate zoomcamp

If you don't have pip, install it

    conda install pip

Intall the requirements

    pip install -r requirements

Also we need more libraries

    pip install beautifulsoup4 openpyxl lxml

<code>'ingest_data_6.py'</code> is a pipeline orchestrated by Prefect, which does the webscraping, tranform xlsx files to dataframes, and uploads the tables to Google Cloud Storage


Use prefect orion to visualize all the flow and tasks, which the pipeline has.

    prefect orion start

<p align="center">
  <img src="images\orion_prefect.png">
</p>

Create a block -> GCS Bucket, for that copy the key generated when I created the service account and paste it, take a look how generate the key here [`CREATE SERVICE ACCOUNT`](./create_service_account.md)

<p align="center">
  <img src="images\gcs_bucket_block.png">
</p>

### 6.6. Deployment with prefect

    prefect deployment build ./ingest_data_6.py:main_flow -n "Parameterized ETL"

<p align="center">
  <img src="images\deployment_build_cmd.png">
</p>

<p align="center">
  <img src="images\deployment_build.png">
</p>

    prefect deployment apply main_flow-deployment.yaml

<p align="center">
  <img src="images\deployment_apply.png">
</p>

In deployment I chose <code>"Quick Run"</code>

<p align="center">
  <img src="images\quick_run.png">
</p>

    prefect agent start  --work-queue "default"

<p align="center">
  <img src="images\apply_agent.png">
</p>

    prefect deployment build ./ingest_data_6.py:main_flow -n "etl2" --cron "0 0 * * *" -a

### 6.7. Running Prefect flows on docker containers

Dockerfile

    FROM prefecthq/prefect:2.7.7-python3.9

    COPY docker-requirements.txt .

    RUN pip install -r docker-requirements.txt --trusted-host pypi.python.or --no-cache-dir

    WORKDIR  /de-zoomcap

    COPY ingest_data_6.py ingest_data_6.py
    COPY read_parameters.py read_parameters.py 

--- 
    docker image build -t jesus6105/prefect:zoom .

<p align="center">
  <img src="images\docker_build_prefect.png">
</p>

    docker image push jesus6105/prefect:zoom

<p align="center">
  <img src="images\docker_push_prefect.png">
</p>

Set up a docker block

<p align="center">
  <img src="images\docker_block_prefect.png">
</p>

<p align="center">
  <img src="images\docker_block_configuration.png">
</p>

    python docker_deploy.py
<p align="center">
  <img src="images\docker_deploy_py.png">
</p>

    prefect deployment run Main Flow/docker-flow --parameters '{"URL":"https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS","years":[2022]}'

  when run the above command try to delete all cache decoraters in  <code>'ingest_data_6.py'</code>


## 10. References

  Surveillance of the Nutritional Status Information System in EESS
  
  https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS

  Management Report SIEN-HIS 2021
  
  https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf
