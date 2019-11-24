# encoding=utf-8
import logging
import time
# log_path是存放日志的路径
import os
import logging.handlers


cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class ColoredFormatter(logging.Formatter):
    '''A colorful formatter.'''
 
    def __init__(self, fmt = None, datefmt = None):
        logging.Formatter.__init__(self, fmt, datefmt)
 
    def format(self, record):
        # Color escape string
        COLOR_RED='\033[1;31m'
        COLOR_GREEN='\033[1;32m'
        COLOR_YELLOW='\033[1;33m'
        COLOR_BLUE='\033[1;34m'
        COLOR_PURPLE='\033[1;35m'
        COLOR_CYAN='\033[1;36m'
        COLOR_GRAY='\033[1;37m'
        COLOR_WHITE='\033[1;38m'
        COLOR_RESET='\033[1;0m'
        # Define log color
        LOG_COLORS = {
            'DEBUG': '%s',
            'INFO': COLOR_GREEN + '%s' + COLOR_RESET,
            'WARNING': COLOR_YELLOW + '%s' + COLOR_RESET,
            'ERROR': COLOR_RED + '%s' + COLOR_RESET,
            'CRITICAL': COLOR_RED + '%s' + COLOR_RESET,
            'EXCEPTION': COLOR_RED + '%s' + COLOR_RESET,
        }
        level_name = record.levelname
        msg = logging.Formatter.format(self, record)
        return LOG_COLORS.get(level_name, '%s') % msg


class Log(object):

    def __init__(self, level='DEBUG', log_name='root'):
        # 文件的命名
        self.log_name = log_name
        self.logname = os.path.join(log_path, '%s.%s.log' % (log_name, time.strftime('%Y_%m_%d')))
        print(self.logname)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(level)#logging.DEBUG)
        # 日志输出格式
        self.cmdfmt = '[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s'
        self.cmddatefmt = '%Y-%m-%d %H:%M:%S'
        # self.formatter = logging.Formatter(fmt=self.cmdfmt, datefmt=self.cmddatefmt)
        self.formatter = ColoredFormatter(self.cmdfmt, self.cmddatefmt)
        # 每天 rotate 一次日志，保留 7 天日志
        
        handler = logging.handlers.TimedRotatingFileHandler(
            self.logname, interval=1, when='D', backupCount=7) #"./log/%s.log" % self.log_name
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)


    def __console(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

# encoding=utf8
# import sys

# reload(sys)

# sys.setdefaultencoding('utf-8')
# from log_init import Log
# log = Log()
# print log.logname
# log.info("愤怒的小猥琐");
