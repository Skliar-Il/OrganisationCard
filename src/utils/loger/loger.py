import logging


class Logger(logging.Logger):

    def __init__(self, name: str, level: int = logging.NOTSET):
        super().__init__(name, level)
        self.__console_handler = logging.StreamHandler()
        self.__console_handler.setLevel(level)
        self.__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.__console_handler.setFormatter(self.__formatter)
        self.addHandler(self.__console_handler)

