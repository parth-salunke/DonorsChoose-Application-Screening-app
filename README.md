# DonorsChoose-Application-Screening-app


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

1. Templates.py --  it will create folder structure for our project
2. create conda env and create requirements.txt
3. run -  conda create -n dcenv310 python=3.8 -y
4. run -  pip install requirements.txt  aldo add -e.(to use local package in next step)
5. create setup.py - we will add project details here - version , repoName , authorName 
this setup.py will setup sec-donorchose dir as local package to use 
6. in src-donorchose __init__ we will add our logger module so we can use logger from local 
package donorchose --from donorschoose import logger--
7. utils - common.py  added some common functions - save json , read yaml 

8. starting our Project now 

    for each component i will follow this work flow 
    for 1st component i am following this steps and same will be for others

    a. Data Ingestigate -  
        download data and store data
        in src/component we will add new component as data_ingestion 
        in data ingestion we will create function to download data from Gdrive and 
        second function to extract data
    b.
        to download and store data we need source path from which we will download and 
        extract path where we will store 
        in Project we will create artifact folder which use is to store whatever artifact we do in our
        project .

    c. 
        config - so we need source path and extarct path to get and extract zip
        we will create  config/config.yaml - i will add var : path name

        """
        artifacts is Centralized Storage: 
        Keeping datasets in a centralized repository ensures easy access and management of data by
        multiple users or processes.

        generated artifacts will store in artifacts folder
        """


        entity - so in entity we have type of config  used for that particular component in this case it is data ingestion 
        so we  have config data for data ingestion from config , we need to use that accross whole project so we will create entity class which will only store that config in class object so we can use it accross project using that object
        var we are storing in config/config.yaml in entuity/config_entity

    d.
        we have 2 config.yaml and config_entity  now so we will use 
        src/constant __init__.py where i will store path for both
        because we will never going to change constant values 
    
    e.
        finally in src/configuration.py 
        we will manage config for 
            crate dir 
            create object for that particular config  
    f. 
        now all this run in  stage_01_data_ingestion 
        we need to call all function here 









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