from donorschoose.config.configuration import ConfigurationManager
from donorschoose.components.data_cleaning import DataCleaning
from donorschoose.utils.common import save_csv
from donorschoose import logger

STAGE_NAME = "Data Cleaning stage"


class DataCleaningTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_clean_config = config.get_data_clean_config()
        data_clean = DataCleaning(config=data_clean_config)
        data_clean.read_files()
        data_clean.merge_csv()

        data_clean.clean_text_column("project_subject_categories")
        data_clean.clean_text_column("project_subject_subcategories")
        data_clean.clean_text_column("project_grade_category")
        data_clean.clean_text_column("teacher_prefix")
        data_clean.clean_text_column("school_state")

        data_clean.preprocess_text("project_title")

        data_clean.add_two_column("essay" , "project_essay_1")
        data_clean.add_two_column("essay" , "project_essay_2")
        data_clean.add_two_column("essay" , "project_essay_3")
        data_clean.add_two_column("essay" , "project_essay_4")
        data_clean.preprocess_text("essay")
        data_clean.rename_column("project_subject_categories" ,"clean_categories")
        data_clean.rename_column("project_subject_subcategories" ,"clean_subcategories")
        drop_columns_list = ["project_essay_1",
                        "project_essay_2",
                        "project_essay_3",
                        "project_essay_4",
                        "teacher_id",
                        "project_submitted_datetime",
                        "id"]
        data_clean.drop_colums(drop_columns_list)
        save_csv(data_clean.train_df ,data_clean_config.save_clean_datafile)



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataCleaningTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e