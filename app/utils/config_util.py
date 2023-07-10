import os

from dotenv import load_dotenv

load_dotenv()

class GlobalConfig:
    @staticmethod
    def get_log_path():
        return os.getenv('PATH_LOGGER_FILES')

    @staticmethod
    def get_log_filename():
        return os.getenv('LOG_FILENAME')
    
    @staticmethod
    def get_path_db():
        return os.getenv('PATH_DB')