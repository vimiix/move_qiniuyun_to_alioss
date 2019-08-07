# coding:utf-8
"""
@Author: Vimiix[vimiix.py@gmail.com]
@Blog: www.vimiix.com
@License: Apache-2.0
"""


class MyConfig:
    # 提前使用 qshell listbucket 指令生成的文件路径
    # 如果在当前文件，就直接写文件名
    listbucket_data_path = 'listbucket.txt'

    # 七牛云的外链域名
    # (例如 http://omfis13un.bkt.clouddn.com)
    qiniu_base_url = ''
    # 七牛云bucket名
    qiniu_bucket = ''

    # ALIOSS access_key 的 id 和 secret
    # 请保密，不要上传到公开网络
    alioss_access_key_id = ''
    alioss_access_key_secret = ''

    # ALIOSS 概览中外网访问的 EndPoint（地域节点）
    alioss_host = ''
    alioss_bucket_name = ''


myconfig = MyConfig()
