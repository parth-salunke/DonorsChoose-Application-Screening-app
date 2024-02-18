from donorschoose.config.configuration import ConfigurationManager
from donorschoose.components.data_modeling_ml import ModelTraining
from donorschoose.utils.common import save_csv
from donorschoose import logger

STAGE_NAME = "Data Modeltraining ml stage"


class DatamodelingmlPipeline:
    def __init__(self):
        pass

    def main(self):
        data_Config = ConfigurationManager()
        Model_training = ModelTraining(data_Config.get_model_training_config())
        Model_training.read_files()
        Model_training.train_log_reg()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DatamodelingmlPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e