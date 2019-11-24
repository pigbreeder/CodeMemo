# encoding=utf8
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
from log_init import Log
log = Log()
print log.logname
log.info("愤怒的小猥琐");
