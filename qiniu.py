# coding:utf-8

import os
import requests


class QiniuCloud:

    def __init__(self, base_url, bucket):
        self.bucket = bucket
        self.base_url = base_url

    def request_and_save(self, filename, data_path):
        print('[-] Downloading %s' % filename)
        url = self.base_url
        url = url.endswith('/') and url or url + '/'
        resp = requests.get(url + filename)
        if resp.status_code == 404:
            print('[×] Not found file: %s' % filename)
        elif resp.status_code == 200:
            if not os.path.exists(data_path):
                os.makedirs(data_path)
            with open(data_path + '/{}'.format(filename), "wb") as f:
                f.write(resp.content)
            print('[√] File: {} saved successful.'.format(filename))


if __name__ == "__main__":
    print('Test Begin')
    URL_PATTERN = "http://omfis13un.bkt.clouddn.com/"
    qiniu = QiniuCloud(URL_PATTERN, "vimiix-blog-data")
    qiniu.request_and_save(
        '图片1.png',
        "data/vimiix-blog-data")
    print('Done')
