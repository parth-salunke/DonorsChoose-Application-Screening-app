from donorschoose.config.configuration import ConfigurationManager
from donorschoose.components.data_transform import DataTransformation
from donorschoose.utils.common import save_csv
from donorschoose import logger

STAGE_NAME = "Data transformation stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        data_Config = ConfigurationManager()
        data_transform = DataTransformation(data_Config.get_data_transform_config())
        data_transform.read_files()
        data_transform.split_data("project_is_approved")
        data_transform.tfIdef_text("essay")

        onehot_columns_list =['teacher_prefix', 'school_state', 'project_grade_category']
        data_transform.onehotencoding_feature(onehot_columns_list)

        data_transform.feature_hash("clean_categories" , 500)
        data_transform.feature_hash("clean_subcategories" ,100)

        data_transform.normalize_column("price")
        data_transform.normalize_column("quantity")

        data_transform.save_transformed_data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e