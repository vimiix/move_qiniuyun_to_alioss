# coding:utf-8
"""
@Author: Vimiix[vimiix.py@gmail.com]
@Blog: www.vimiix.com
@License: Apache-2.0
"""

import os
import requests


class QiniuCloud:
    def __init__(self, base_url, bucket):
        self.bucket = bucket
        self.base_url = base_url

    def download(self, filename, save_path):
        print('[-] Downloading %s' % filename)
        url = self.base_url
        url = url.endswith('/') and url or url + '/'
        resp = requests.get(url + filename)
        if resp.status_code == 404:
            print('[×] Not found file: %s' % filename)
        elif resp.status_code == 200:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            with open(save_path + '/{}'.format(filename), "wb") as f:
                f.write(resp.content)
            print('[√] File: {} saved successful.'.format(filename))
