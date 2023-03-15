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
- 4.[Instructions on how to run the project](#7-instructions-on-how-to-run-the-project)
  - 4.1.[Setting up Google Cloud Platform account](#41-setting-up-google-cloud-platform-account)
  - 4.2.[Creating a VM on Google Compute Engine](#42-creating-a-vm-on-google-compute-engine)
- 5.[Importing data](#5-importing-data)
- 6.[Notebook](#6-notebook)
  - 6.1.[Exploratory Data Analysis (EDA)](#61-exploratory-data-analysis-eda)
  - 6.2.[Model selection and parameter tuning](#62-model-selection-and-parameter-tuning)
- 7.[Instructions on how to run the project](#7-instructions-on-how-to-run-the-project)
- 8.[Locally deployment](#8-locally-deployment)
- 9.[Google Cloud deployment (GCP)](#9-google-cloud-deployment-gcp)
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
  - <b>Pre-pregnancy IMC. The physical state</b>: use and interpretation of anthropometry. Report of the OMS Expert Committee, Technical Report Series 854, Geneva, Switzerland. OMS, 1995.
  - <b>Weight gain</b>: Institute of Medicine: Weight Gain During Pregnancy: Reexamining the Guidelines. Washington, National Academy Press, 2009.
- <b>Diagnosis of Anemia</b>: OMS-MINSA ranges. Prevention and Control of Iron Deficiency Lima, 2000. Adapted according to altitude.


## 4. Instructions on how to run the project

### 4.1. Setting up Google Cloud Platform account

<p align="justify">

In this part I created my project called `sien-project`, if you want to see the steps to create a project, just check out the instructions here [setup_gcp.md](./setup_gcp.md).

</p>

<p align="center">
  <img src="images\new_project_gcp.png">
</p>

### 4.2. Creating a VM on Google Compute Engine










## 10. References

  Surveillance of the Nutritional Status Information System in EESS
  
  https://web.ins.gob.pe/es/alimentacion-y-nutricion/vigilancia-alimentaria-y-nutricional/vigilancia-del-sistema-de-informacion-del-estado-nutricional-en-%20EESS

  Management Report SIEN-HIS 2021
  
  https://web.ins.gob.pe/sites/default/files/Archivos/cenan/van/informes/2021/Inf%20Gerencial%20SIEN-HIS%202021.pdf
