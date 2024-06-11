from utils.utils_config_parser import UtilsConfigParser

def config_from_file(file_path):
    config = UtilsConfigParser()
    config.read(file_path)
    return config
