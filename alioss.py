# coding:utf-8

import oss2


class AliOss:

    def __init__(self, ak_id, ak_secret):
        self._ak_id = ak_id
        self._ak_secret = ak_secret
        self.auth = self._auth()

    def _auth(self):
        auth = oss2.Auth(self._ak_id, self._ak_secret)
        return auth

    def bucket(self, alioss_host, bucket_name):
        return oss2.Bucket(self.auth, alioss_host, bucket_name)

    @staticmethod
    def upload(data_path, filename, bucket_instance):
        bucket_instance.put_object_from_file(
            filename,
            "{}/{}".format(data_path, filename)
        )
        print('[√] Upload file %s to alioss successful.' % filename)


if __name__ == '__main__':
    print('Begin')
    alioss = AliOss('', '')
    bucket = alioss.bucket('oss-cn-qingdao.aliyuncs.com', 'vimiix-blog')
    alioss.upload('data/vimiix-blog-data', '图片1.png', bucket)
    print('Done')

