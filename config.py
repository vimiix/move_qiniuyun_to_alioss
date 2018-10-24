# coding:utf-8


class MyConfig:
    # 提前使用 qshell listbucket 指令生成的文件路径
    # 如果在当前文件，就直接写文件名
    listbucket_data_path = 'listbucket.txt'

    # 七牛云的外链域名
    # (例如 http://omfis13un.bkt.clouddn.com)
    qiniu_base_url = 'http://omfis13un.bkt.clouddn.com'
    # 七牛云bucket名
    qiniu_bucket = 'vimiix-blog-data'

    # ALIOSS access_key 的 id 和 secret
    # 请保密，不要上传到公开网络
    alioss_access_key_id = ''
    alioss_access_key_secret = ''

    # ALIOSS 概览中外网访问的 EndPoint（地域节点）
    alioss_host = 'oss-cn-qingdao.aliyuncs.com'
    alioss_bucket_name = 'vimiix-blog'


myconfig = MyConfig()
