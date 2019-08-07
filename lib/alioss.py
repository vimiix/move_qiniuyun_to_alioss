# coding:utf-8
"""
@Author: Vimiix[vimiix.py@gmail.com]
@Blog: www.vimiix.com
@License: Apache-2.0
"""

import oss2


class AliOss:
    def __init__(self, ak_id, ak_secret, host, bucket_name):
        self._ak_id = ak_id
        self._ak_secret = ak_secret
        self.host = host
        self.bucket_name = bucket_name
        self.auth = self._auth()
        self.bucket = self._bucket()

    def _auth(self):
        auth = oss2.Auth(self._ak_id, self._ak_secret)
        return auth

    def _bucket(self):
        return oss2.Bucket(self.auth, self.host, self.bucket_name)

    def upload(self, filename, data_path):
        self.bucket.put_object_from_file(
            filename,
            "{}/{}".format(data_path, filename)
        )
        print('[√] Upload file %s to alioss successful.' % filename)
