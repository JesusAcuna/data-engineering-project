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

- 6.[Alternative B](#6-alternative-b)
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

### 5.1. Creating a docker-compose 

<p align="justify">

After finishing point [4.4. Setting up VM instance](#44-setting-up-instance) we need to create an open-source relational database managemnet system that emphasizes SQL extensibility and compliance (<code>POSTGRESQL</code>).

And a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well (<code>PGADMIN</code>).

</p>

For that, I created a subfolder

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

To use Visual Studio Code, we can connect to a remote machine using SSH. check the instructions here to use [`REMOTE SSH`](./remote_ssh.md).

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




## 6. Alternative B 

After finishing [4.4. Setting up VM instance](#44-setting-up-instance)

## 10. References

  Surveillance of the Nutritional Status Information System in EESS
  
  https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS

  Management Report SIEN-HIS 2021
  
  https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf
