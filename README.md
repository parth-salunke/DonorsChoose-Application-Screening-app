# DonorsChoose-Application-Screening-app

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

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



## Project Steps

Templates.py --  it will create folder structure for our project
create conda env and create requirements.txt
run -  conda create -n dcenv310 python=3.8 -y
run -  pip install requirements.txt
create setup.py - we will add project details here - version , repoName , authorName 
