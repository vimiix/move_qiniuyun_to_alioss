# coding:utf-8
"""
@Author: Vimiix[vimiix.py@gmail.com]
@Blog: www.vimiix.com
@License: Apache-2.0
"""

from lib.qiniu import QiniuCloud
from lib.alioss import AliOss
from config import myconfig


class Worker():
    def __init__(self, config):
        self.listbucket_data_path = config.listbucket_data_path
        self.data_path = "data/{}".format(config.qiniu_bucket)
        self.qiniu = QiniuCloud(
            config.qiniu_base_url,
            config.qiniu_bucket
        )
        self.alioss = AliOss(
            config.alioss_access_key_id,
            config.alioss_access_key_secret,
            config.alioss_host,
            config.alioss_bucket_name
        )

    def work(self):
        with open(self.listbucket_data_path) as f:
            for line in f:
                print('[-] Get line %s' % line.strip())
                filepath = line.split('\t')[0]
                self.qiniu.download(filepath, self.data_path)
                self.alioss.upload(filepath, self.data_path)


if __name__ == '__main__':
    worker = Worker(myconfig)
    worker.work()
