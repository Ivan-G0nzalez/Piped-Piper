import logging
from logging import FileHandler

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.configure_logging()

    def configure_logging(self):
        # Eliminamos los posibles manejadores, si existen, del logger por defecto
        del self.logger.handlers[:]
        # Añadimos el logger por defecto a la lista de loggers
        handlers = []
        # Creamos un manejador para escribir los mensajes por consola
        # console_handler = StreamHandler()
        # console_handler.setLevel(logging.DEBUG)
        # console_handler.setFormatter(self.verbose_formatter())
        # handlers.append(console_handler)

        # Creamos un manejador para escribir los mensajes en un archivo
        file_handler = FileHandler('logger/logs.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self._verbose_formatter())
        handlers.append(file_handler)

        # Asociamos cada uno de los handlers a cada uno de los loggers
        for handler in handlers:
            self.logger.addHandler(handler)

        self.logger.propagate = False
        self.logger.setLevel(logging.DEBUG)    

    def _verbose_formatter(self):
        return logging.Formatter(
            '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )

