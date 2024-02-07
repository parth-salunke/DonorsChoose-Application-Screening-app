# DonorsChoose-Application-Screening-app

Project Jupyter Notebook : 
[Exploratory_data_analysis Notebook](research/01_Exploratory_data_analysis.ipynb)
[Preprocessing data Notebook](research/02_Preprocessing_data.ipynb)
[Data modeling ML Notebook](research/03_Data_modeling_ML.ipynb)
[Data modeling LSTM Notebook](research/04_Data_modeling_LSTM.ipynb)

Currently i am Working on MLops Pipeline for Project....

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/parth-salunke/DonorsChoose-Application-Screening-app
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create --name dcenv310 python=3.10 -y
```

```bash
conda activate dcenv310
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



### Project Flow

## Step 1: Creating the Folder Structure
- Use `Templates.py` to kickstart the project by setting up the initial folder structure.

## Step 2: Setting up Conda Environment and Dependencies
- Create a Conda environment named `dcenv310` with Python 3.8 to manage dependencies effectively.
- Generate a `requirements.txt` file to track and install project dependencies.

## Step 3: Initializing the Conda Environment
- Run `conda create -n dcenv310 python=3.8 -y` to set up the Conda environment.

## Step 4: Installing Project Dependencies
- Install necessary dependencies listed in `requirements.txt` using pip.
- Include any local packages using the `-e` flag if required.

## Step 5: Configuring Project Details
- Define project specifics such as version, repository name, and author within `setup.py`.
- Ensure `setup.py` configures the `src-donorchose` directory as a local package.

## Step 6: Setting Up Logging
- Configure logging functionality within `src-donorchose/__init__.py` for effective debugging.
- Example: `from donorschoose import logger`.

## Step 7: Implementing Utility Functions
- Create common utility functions like saving JSON and reading YAML within `utils/common.py`.

## Step 8: Starting the Project
- Begin the project by following a systematic workflow for each component.

---

## Workflow for Each Component

# Data Ingestion
- Download and store necessary data for the project.
- Establish a `data_ingestion` component in `src/component` and implement data retrieval functions.

# Artifact Management
- Set up an `artifacts` folder at the project root to manage generated artifacts efficiently.

# Configuration Setup
- Define source and extract paths within `config/config.yaml`.
- Utilize a `config_entity` class to store and manage configuration data effectively.

# Constants Declaration
- Store constant values such as file paths within `src/constant/__init__.py`.

# Configuration Management
- Develop `src/configuration.py` to handle configuration-related tasks like directory creation and object instantiation.

# Execution
- Execute defined functions for each component, starting with `stage_01_data_ingestion`.

---

