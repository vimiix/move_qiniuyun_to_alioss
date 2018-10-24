# coding:utf-8

from qiniu import QiniuCloud
from alioss import AliOss
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
            config.alioss_access_key_secret
        )
        self.alioss_bucket = self.alioss.bucket(
            config.alioss_host,
            config.alioss_bucket_name
        )

    def work(self):
        with open(self.listbucket_data_path) as f:
            for line in f:
                print('[-] Get line %s' % line.strip())
                filename = line.split('\t')[0]
                self.qiniu.request_and_save(
                    filename,
                    self.data_path
                )
                self.alioss.upload(
                    self.data_path,
                    filename,
                    self.alioss_bucket
                )


if __name__ == '__main__':
    worker = Worker(myconfig)
    worker.work()
