import logging

def setup_logger(name, log_level):
    logger = logging.getLogger(name)
    level = logging.getLevelName(log_level)
    logger.setLevel(level)

    # log to console output
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # use the format: [INFO] tests - message
    formatter = logging.Formatter("[%(levelname)s] %(name)s - %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger
