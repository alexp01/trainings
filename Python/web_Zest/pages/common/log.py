import logging
import datetime

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename = datetime.datetime.today().strftime('%d-%m-%Y %H_%M_%S') + '_logs.txt',
    filemode = "w"
)
logger = logging.getLogger('test_logger')
