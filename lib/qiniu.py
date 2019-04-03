from qiniu import Auth, put_file, etag

from swiper import config


#需要填写你的 Access Key 和 Secret Key
access_key = config.QN_ACCESS_KEY
secret_key = config.QN_SECRET_KEY

def upload_qiniu(filename, filepath):
    # 构建鉴权对象
    qiniu_auth = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = config.QN_BUCKET_NAME

    # 上传后保存的文件名
    # filename = filename

    # 生成上传 Token，可以指定过期时间等
    token = qiniu_auth.upload_token(bucket_name, filename, 3600)

    # 要上传文件的本地路径
    # localfile = filepath
    ret, info = put_file(token, filename, filepath)
    print(ret)
    print(info)
