import logging
import logging.config

logging.config.fileConfig('logging.cfg')

# create logger
logger = logging.getLogger('collectors')

logger = logging.LoggerAdapter(logger, {"cpeid":"123"})

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
