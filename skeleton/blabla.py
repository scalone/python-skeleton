import logging

class Blabla(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def sum(self, a, b):
        return a + b

    def log(self):
        logging.basicConfig(level=logging.NOTSET)
        logging.info("Info - Blabla")
        logging.warning("Warning - Blabla")
        logging.debug('Debug - Blabla')
        return None

