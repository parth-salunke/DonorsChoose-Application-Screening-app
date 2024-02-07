# DonorsChoose-Application-Screening-app

Project Jupyter Notebook : 
1. [Exploratory_data_analysis Notebook](research/01_Exploratory_data_analysis.ipynb)
   
•	Performed exploratory data analysis (EDA) to understand the characteristics and patterns in the dataset.
•	Analyzed data distributions, correlations, and outliers to gain insights into the underlying structure.
•	Used visualizations and statistical summaries to uncover trends and relationships within the data.

3. [Preprocessing data Notebook](research/02_Preprocessing_data.ipynb)

•	Incorporated preprocessing techniques tailored for text data, including tokenization, stop word removal, and stemming or lemmatization.
•	Performed text-specific tasks such as vectorization (e.g., TF-IDF or word embeddings) to convert text data into numerical format for model training.
•	Implemented text cleaning steps to remove noise, such as special characters and punctuation, and standardized text formatting for consistency.

3. [Data modeling ML Notebook](research/03_Data_modeling_ML.ipynb)

•	Applied machine learning algorithms including Logistic Regression, Support Vector Machines (SVM), Random Forest, and Decision Trees for modeling.
•	Tuned hyperparameters and evaluated model performance using metrics such as accuracy, precision, recall, and F1-score.
•	Selected the best-performing model based on validation results to deploy for predictive tasks.

4. [Data modeling LSTM Notebook](research/04_Data_modeling_LSTM.ipynb)

•	Implemented a Long Short-Term Memory (LSTM) neural network for deep learning modeling.
•	Incorporated TF-IDF data within the interquartile range (25th to 75th percentile) for enhanced feature representation.
•	Trained and optimized the LSTM model to capture temporal dependencies in sequential data, improving predictive accuracy.


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



## Project Flow

### Step 1: Creating the Folder Structure
- Use `Templates.py` to kickstart the project by setting up the initial folder structure.

### Step 2: Setting up Conda Environment and Dependencies
- Create a Conda environment named `dcenv310` with Python 3.8 to manage dependencies effectively.
- Generate a `requirements.txt` file to track and install project dependencies.

### Step 3: Initializing the Conda Environment
- Run `conda create -n dcenv310 python=3.8 -y` to set up the Conda environment.

### Step 4: Installing Project Dependencies
- Install necessary dependencies listed in `requirements.txt` using pip.
- Include any local packages using the `-e` flag if required.

### Step 5: Configuring Project Details
- Define project specifics such as version, repository name, and author within `setup.py`.
- Ensure `setup.py` configures the `src-donorchose` directory as a local package.

#### Step 6: Setting Up Logging
- Configure logging functionality within `src-donorchose/__init__.py` for effective debugging.
- Example: `from donorschoose import logger`.

### Step 7: Implementing Utility Functions
- Create common utility functions like saving JSON and reading YAML within `utils/common.py`.

### Step 8: Starting the Project
- Begin the project by following a systematic workflow for each component.

---

## Workflow for Each Component

#### Data Ingestion
- Download and store necessary data for the project.
- Establish a `data_ingestion` component in `src/component` and implement data retrieval functions.

####  Artifact Management
- Set up an `artifacts` folder at the project root to manage generated artifacts efficiently.

####  Configuration Setup
- Define source and extract paths within `config/config.yaml`.
- Utilize a `config_entity` class to store and manage configuration data effectively.

####  Constants Declaration
- Store constant values such as file paths within `src/constant/__init__.py`.

####  Configuration Management
- Develop `src/configuration.py` to handle configuration-related tasks like directory creation and object instantiation.

####  Execution
- Execute defined functions for each component, starting with `stage_01_data_ingestion`.

---

