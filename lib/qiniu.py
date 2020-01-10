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

    def download(self, filepath, save_path):
        print('[-] Downloading %s' % filepath)
        url = self.base_url
        url = url.endswith('/') and url or url + '/'
        resp = requests.get(url + filepath)
        dir_path, filename = os.path.split(filepath)
        save_path = os.path.join(save_path, dir_path)
        if resp.status_code == 404:
            print('[×] Not found file: %s' % filepath)
        elif resp.status_code == 200:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            with open(os.path.join(save_path + filename), "wb") as f:
                f.write(resp.content)
            print('[√] File: {} saved successful.'.format(filepath))
