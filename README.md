# Nutritional Status Information System - SIEN 

<p align="center">
  <img src="images\SIEN.png">
</p>

---

<p align="justify">
In 2003, the INS/CENAN, which is the National Institute of Health(Perú), implemented the Nutritional Status Information System - SIEN, based on a continuous and systematic process that records, processes, reports and analyzes information about the nutritional status of children under five years old,  and pregnant women, who attend to health establishments at the first level of care of the Ministry of Health.
</p>

---
## Index

- 1.[Description of the problem](#1-description-of-the-problem)
- 2.[Objective](#2-objective)
- 3.[Technologies](#3-technologies)
  - 3.1.[Alternative A - Local](#31-alternative-a---local)
  - 3.2.[Alternative B - Cloud](#32-alternative-b---cloud)
- 4.[Data Architecture](#4-data-architecture)
- 5.[Data description](#5-data-description)
- 6.[Instructions on how to replicate the project](#6-instructions-on-how-to-replicate-the-project)
  - 6.1.[Setting up Google Cloud Platform account](#61-setting-up-google-cloud-platform-account)
  - 6.2.[Creating a VM Instance on Google Compute Engine](#62-creating-a-vm-instance-on-google-compute-engine)
  - 6.3.[VM instance connection configuration](#63-vm-instance-connection-configuration)
  - 6.4.[Setting up VM instance](#64-setting-up-vm-instance)
- 7.[Alternative A - Local](#7-alternative-a---local)
  - 7.1.[Creating a docker-compose](#71-creating-a-docker-compose)
  - 7.2.[Running a docker-compose](#72-running-a-docker-compose)
  - 7.3.[Port Forwarding](#73-port-forwarding)
  - 7.4.[Testing the pipeline](#74-testing-the-pipeline)
  - 7.5.[Orchestrating with prefect](#75-orchestrating-with-prefect)
- 8.[Alternative B - Cloud](#8-alternative-b---cloud)
  - 8.1.[Creating service account](#81-creating-service-account)
  - 8.2.[Edit Permissions](#82-edit-permissions)
  - 8.3.[Installing Terraform](#83-installing-terraform)
  - 8.4.[Setting up Terraform files](#84-setting-up-terraform-files)
  - 8.5.[Orchestrating with prefect](#85-orchestrating-with-prefect)
  - 8.6.[Deployment with prefect](#86-deployment-with-prefect)
  - 8.7.[Running Prefect flows on docker containers](#87-running-prefect-flows-on-docker-containers)
  - 8.8.[Dbt](#88-dbt)
  - 8.9.[Looker Studio](#89-looker-studio)
- 9.[Future enhancements ](#9-future-enhancements)
- 10.[References](#10-references)
---

## 1. Description of the problem

<p align="justify">
The improvement of child and pregnant women health indicators correspond to equity measures, since these groups are the most vulnerable, so their monitoring and analysis is a priority in the development of the nation. In children under five years of age, the monitoring of indicators of chronic, global and acute malnutrition, overweight, obesity and anemia are the most relevant from the point of view of nutritional status, likewise in pregnant women are the deficit of weight, overweight and anemia, and how they affect childbirth and the newborn.
</p>

<p align="justify">
You can take a look at the 2021 Managment Report to see its structure, I think that the most important points are:
</p>

- Introduction
  
  - Objective

- Methodology
  
  - Population (Sample)
  - Techniques and Instruments
  - Variables
  - Procedures

- Results
- Recomendations

Source (Spanish) :

> https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf

## 2. Objective

<p align="justify">
Develop a <code>BIG DATA ARCHITECTURE</code> to handle the ingestion, processing and data analysis, including a dashboard for users to perform advanced analytics  and prediction models , with the purpose of generating timely information about the nutritional status of the population, for decision-making and thus contribute to the improvement of quality of life of children and pregnant women.
</p>

## 3. Technologies

For setting up the VM Instance or Local Machine I installed these tools:

- Anaconda environment
- Docker
- Docker-Compose
- Java
- Spark

### 3.1. Alternative A - Local
- <p align="justify">
  <b>Docker-compose</b> : for creating a relational database managment system (POSTGRESQL) and a web-based GUI tool to interact with the postgres database(PGADMIN).
  </p>

- <p align="justify">
  <b>Prefect</b>: is an open-source orchestration tool, which allows you to define, schedule and monitor your data pipelines.
  </p>

- <p align="justify">
  <b>Data Build Tool (dbt)</b>: is a framework that combines modular SQL and  allows you to automate data quality testing, deploy the code, and deliver trusted data with documentation side-by-side with the code
  </p>

- <p align="justify">
  <b>Metabase</b>: is an open-source business intelligence platform that lets users explore and learn from their data.
  </p>

### 3.2. Alternative B - Cloud

- <p align="justify">
  <b>Terraform</b>:  is an open-source infrastructure-as-code software tool. Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.
  </p>

- <b>Google Cloud Platform</b>:

  -	Google Cloud Storage
  -	Big Query
  -	Google Compute Engine

- <b>Prefect</b>

- <b>Data Build Tool (dbt)</b>

- <p align="justify">
  <b>Looker Studio</b>: a free tool that turns your data into informative, easy to read, easy to share, and fully customizable dashboards and reports.
  </p>

## 4. Data Architecture

<p align="justify">
I created a data architecture flow for data engineering zoomcamp 2023, this flows is for batch processing, since in my project data is uptaded monthly. 
</p>

<p align="justify">
 I did the graphics in power point, and the  file is uploaded in <code>power_point</code>, so you can edit it
</p>

<p align="center">
  <img src="images\data_architecture.png">
</p>

There are many ways to generate an ETL process, but for the development of this project I chose this path

<p align="center">
  <img src="images\data_architecture_chosen.png">
</p>


## 5. Data description

<p align="justify">
The source of information is secondary, that means that I don't have access to more personal data. Also, this data is provided by the open data platform of Peru and it corresponds to the information registered in the Clinical Histories of the Health Establishments of the Ministry of Health(Perú).
</p>

<p align="justify">
This information is provided in excel format, where each of them represents a <code>category</code> for a given month. Besides the information uploaded is not monthly but every three months.
</p>

<b>Categories:</b>

- Children under five years of age
- Children under three years of age
- Foreign Children under five years of age
- Foreign Children under three years of age
- VRAEM Children under five years of age
- VRAEM Children under three years of age
- Pregnant women

<p align="center">
  <img src="images\informes_sien.png">
</p>

There are levels of grouping according to the care establishment where the children and pregnant women were cared for.

<b>Levels:</b>

- Department
- DIRESA
- District

<p align="center">
  <img src="images\establishment_level.png">
</p>

<p align="justify">
Each sheet has the number of children or pregnant women evaluated, the cases positives and the rate for each of the indicators.
</p>

<b>Indicators:</b>
 
- <b>Children </b>:
  - Chronic Malnutrition
  - Global Malnutrition
  - Acute malnutrition, Overweight, Obesity
  - Mild, Moderate and Severe Anemia
- <b>Pregnant women</b>: 
  - Low, adequate and high weight gain, according to IMC Pre-pregnancy Weight
  - Mild, Moderate and Severe Anemia

<p align="center">
  <img src="images\indicator_sien.png">
</p>

## 6. Instructions on how to replicate the project

### 6.1. Setting up Google Cloud Platform account

In this part I created my project called <code>sien-project</code>, if you want to see the steps to create a project on Google Cloud Platform, just check out the instructions here [`CREATE GCP PROJECT`](./create_gcp_project.md).

<p align="center">
  <img src="images\new_project_gcp.png">
</p>

### 6.2. Creating a VM Instance on Google Compute Engine

For this part I created my VM instance called <code>de-zoomcamp</code>, if you want to see the steps to create a VM instance, just check out the instructions here [`CREATE VM INSTANCE`](./create_vm_instance.md).

<p align="center">
  <img src="images\vm_instance_name.png">
</p>

### 6.3. VM instance connection configuration

In this part I created a config file with the alias <code>de-zoomcamp</code> to connect to the VM instance , if you want to see these steps, just check out the instructions here [`CREATE CONNECTION VM`](./create_connection_vm.md).

<p align="center">
  <img src="images\ssh_de_zoomcamp.png">
</p>

### 6.4. Setting up VM instance

For this part I installed these listed tools in my virtual machine instance on GCP:

- Anaconda environment
- Docker 
- Docker-compose 
- Java
- Spark

If you want to see the steps for installing those tools,just check it out here [`VM CONFIGURATION`](./vm_configuration.md)


## 7. Alternative A - Local

After finishing point [6.4. Setting up VM instance](#44-setting-up-instance) I created an open-source relational database managemnet system that emphasizes SQL extensibility and compliance (<code>POSTGRESQL</code>).

<p align="justify">
And a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well (<code>PGADMIN</code>).</p>

### 7.1. Creating a docker-compose 

I created a subfolder data-engineering/baics_setup

    cd 
    mkdir data-engineering
    cd data-engineering
    mkdir basics_setup
    touch docker-compose.yaml

which contains the <code>docker-compose.yaml</code> file, and its content is:

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

### 7.2. Running a docker-compose 
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

### 7.3. Port Forwarding

To use Visual Studio Code, we can connect to a remote machine using SSH. check the instructions here to create a [`REMOTE SSH`](./remote_ssh.md).

Let's port-forwarding port 5432 for the server, and 8080 for pg-admin

<p align="center">
  <img src="images\port_forwarding.png">
</p>

<p align="justify">
In your browser type: http://localhost:8080/ for accessing to the pg-admin 
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

### 7.4. Testing the pipeline

<code>'notebooks/ingest_data.py'</code> is a pipeline which does the webscraping, downloads xlsx files, and uploads the tables to the postgresql server. So I used this pipeline to test the process of extraction and load with little data

<code>'notebooks/read_parameters_2'</code> is a script that has the parameters to be able to convert an excel file to several dataframes, since a single excel file contains several sheets.

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

---

**(OPTIONAL)** Alternatively you can run the pipeline into a docker .

notebooks/Dockerfile

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


### 7.5. Orchestrating with prefect

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

<code>'ingest_data_2.py'</code> is a pipeline orchestrated by Prefect, which does the webscraping, downloads xlsx files, tranform xlsx files into dataframes, and uploads the tables to the postgresql server.


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

---
**IMPORTANT**

Alternative A - Local  needs to be finished

---

## 8. Alternative B - Cloud

After finishing point [6.4. Setting up VM instance](#44-setting-up-instance) I created an open-source infrastructure-as-code software tool (<code>Terraform</code>).

<p align="justify">
Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.
</p>


### 8.1. Creating service account

In this part I created my service account called <code>terraform-sien</code>, if you want to see the steps to create a service account, just check out the instructions here [`CREATE SERVICE ACCOUNT`](./create_service_account.md).

<p align="center">
  <img src="images\export_google_credentials.png">
</p>

### 8.2. Edit Permissions 

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

### 8.3. Installing Terraform 

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

### 8.4. Setting up Terraform files

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

### 8.5. Orchestrating with prefect

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

### 8.6. Deployment with prefect

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

### 8.7. Running Prefect flows on docker containers

prefect/cloud/Dockerfile

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

---
**IMPORTANT**

  If you have problems running the container try to delete all cache decoraters in  <code>'ingest_data_6.py'</code>

---

### 8.8. Dbt

Create two envirornments one for development, and one for production.
<p align="center">
  <img src="images\environments_dbt.png">
</p>

- Development:

<p align="justify">
'seeds' is a folder is a folder which contains flat files, this in order to build lookup tables.
</p>

<p align="justify">
'lon_lat.csv' is a csv file which contains information about each department such as longitude and latitude, these ones will allow me later to buil a bubble map in looker studio
</p>

<p align="center">
  <img src="images\seed_dbt.png">
</p>

**staging** is a folder which contains tables with slight modifications, here I merged several tables according to category and date.

<p align="center">
  <img src="images\staging_dbt.png">
</p>


**core** is a folder which contains final queries with all the transformation, information that will help us build a dashboard.

In this folder I created two tables one for nutritional status and other for anemia

<p align="center">
  <img src="images\core_dbt.png">
</p>

This graph is for Anemia information

<p align="center">
  <img src="images\lineage_dbt.png">
</p>

- Deployment:

For deployment I created a schema in Big Query called 'production',
then I created a job, in this job I can run the queries that I made in core folder and even I can schedule it.

<p align="center">
  <img src="images\production_dbt.png">
</p>

### 8.9. Looker Studio

In looker Studio I can connect to Big Query and do a dashboard with the core queries, with a bubble map, pie chart and bar charts. 

<p align="center">
  <img src="images\dashboard.png">
</p>

Let's check it out:

<center>

[Nutritional Status Information System - 2022](https://lookerstudio.google.com/reporting/9d1cd82d-354f-4869-85ab-69ed7764f742)

</center>

## 9. Future enhancements 

- Fix 'read_parameters.py' so that the pipeline can work with data from 2021 backwards, since there are many excel files  that have different sizes of columns.
- Finish Alternative A Local
- Testing, Documentaton in dbt
- CI/CD in dbt
- Spark pipelines 

## 10. References

  - Surveillance of the Nutritional Status Information System in EESS
  
     https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS

  - Management Report SIEN-HIS 2021
  
    https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf
