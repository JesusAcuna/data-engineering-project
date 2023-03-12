# Nutritional Status Information System - SIEN 

<p align="center">
  <img src="https://github.com/JesusAcuna/data-engineering-project/blob/main/images/SIEN.png">
</p>

---
## Index

- 1.[Description of the problem](#1-description-of-the-problem)
- 2.[Objective](#2-objective)
- 3.[Data description](#3-data-description)
- 4.[Setting up the virtual environment](#4-setting-up-the-virtual-environment)
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
- `images`: directory of images to README.md
- `static`: directory of css, js files and images for frontend 
- `templates`: directory of html files for frontend 
- `Dockerfile`: archive to containerize the project
- `app.py`: python script to make the web service for classification with `Flask`  <b>FRONTEND</b>
- `best_model.h5`: file of best chosen model 
- `best_model.tflite`: file with extension tensorflow lite of best chosen model
- `convert_to_tflite.py`: python script to convert a 'h5' file to 'tfile' file
- `model.py`: python script to enter image, do normalization and prediction <b>BACKEND</b>
- `requirements.txt`: file with dependencies and libraries
- `train.py`: python script to tune parameters and train a best model, from this script you get the directory `Kitchenware_data` and the file `best_model.h5`
- `Kitchenware_Classification.ipynb`: python notebook where the analysis and modeling is done

## 1. Description of the problem
