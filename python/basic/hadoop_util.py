#coding:utf8
import subprocess
import os
import inspect
import sys


reload(sys)
sys.setdefaultencoding('utf8')


class hadoop_util:
    def __init__(self,logger):
        self.logger = logger
        self.hadoop_streaming="hadoop jar /software/lib/hadoop-streaming-2.2.0.jar"
    
    def remove_dir_in_hdfs(self, hadoop_data_path):
        run_str = 'hadoop fs -rmr ' + hadoop_data_path
        self.logger.info(run_str)
        run = subprocess.Popen(run_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        run.wait()
        run_result = run.stdout.read().decode('utf8')[:-1]
        if run.returncode == 0:
            self.logger.info(run_str + ' messages: ' + run_result)
        elif run.returncode == 255:
            self.logger.info(run_str + ' messages: ' + run_result)
        else:
            self.logger.error(run_str + ' returncode: ' + str(run.returncode) + ' messages: ' + run_result)
            raise Exception(self.__class__.__name__ + '.' + str(inspect.stack()[1][4]) + ' ERROR!')

    def get_hdfs(self, hadoop_path,dir_path):
        run_str = 'hadoop fs -get ' + hadoop_path + ' ' + dir_path
        self.logger.info(run_str)
        run = subprocess.Popen(run_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        run.wait()
        run_result = run.stdout.read().decode('utf8')[:-1]
        if run.returncode == 0:
            self.logger.info(run_str + ' messages: ' + run_result)
        else:
            self.logger.error(run_str + ' returncode: ' + str(run.returncode) + ' messages: ' + run_result)
            raise Exception(self.__class__.__name__ + '.' + str(inspect.stack()[1][4]) + ' ERROR!')
    def mkdir_in_hdfs(self, hadoop_path):
        run_str = 'hadoop fs -mkdir ' + hadoop_path
        self.logger.info(run_str)
        run = subprocess.Popen(run_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        run.wait()
        run_result = run.stdout.read().decode('utf8')[:-1]
        if run.returncode == 0:
            self.logger.info(run_str + ' messages: ' + run_result)
        else:
            self.logger.error(run_str + ' returncode: ' + str(run.returncode) + ' messages: ' + run_result)
            raise Exception(self.__class__.__name__ + '.' + str(inspect.stack()[1][4]) + ' ERROR!')
    def streaming_run(self,cmd,output):
        if self.exists_dir(output):
            self.remove_dir_in_hdfs(output)
        run_str = self.hadoop_streaming + cmd
        self.logger.info(run_str)
        run = subprocess.Popen(run_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while 1:
            line = run.stdout.readline().decode('utf8')[:-1]
            if not line:
                break
            print line
        run.wait()
        run_result = run.stdout.read().decode('utf8')[:-1]
        if run.returncode == 0:
            self.logger.info(run_str + ' messages: ' + run_result)
            return 0
        else:
            self.logger.error(run_str + ' returncode: ' + str(run.returncode) + ' messages: ' + run_result)
            raise Exception(self.__class__.__name__ + '.' + str(inspect.stack()[1][4]) + ' ERROR!')
    def exists_dir(self,hadoop_data_path):
        run_str = 'hadoop fs -test -e ' + hadoop_data_path
        self.logger.info(run_str)
        run = subprocess.Popen(run_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        run.wait()
        run_result = run.stdout.read().decode('utf8')[:-1]
        if run.returncode != 0:
            self.logger.info(run_str + ' messages: ' + run_result)
            return False
        else:
            return True
if __name__ == "__main__":
    import logging
    logger = logging.getLogger("util test")  
    logger.setLevel(logging.DEBUG)  
    # create file handler which logs even debug messages  
    log_path="./test.log"
    fh = logging.FileHandler(log_path)  
    fh.setLevel(logging.DEBUG)  
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  
    fh.setFormatter(formatter)  
    # add the handlers to logger  
    logger.addHandler(fh)  
    hf = hadoop_util(logger)
    hf.remove_dir_in_hdfs('admin_test')
    hf.mkdir_in_hdfs('admin_test')

