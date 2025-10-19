# operations/logging_observer.py

import logging
from operations.observer import Observer

class LoggingObserver(Observer):
    def update(self, calculation_state: dict):
        logging.info(f"📝 LoggingObserver: {calculation_state}")
