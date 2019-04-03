"""用户相关逻辑"""
import os
from urllib.parse import urljoin

from django.conf import settings

from common import keys
from lib import qiniu
from swiper import config
from worker import celery_app


def save_upload_file(filename, avatar):
    """保存上传的文件到本地路径"""
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return filepath

@celery_app.task
def handle_upload_avatar(user, avatar):

    filename = keys.AVATAR_KEY % user.id
    filepath = save_upload_file(filename, avatar)
    # 上传七牛
    qiniu.upload_qiniu(filename, filepath)

    user.avatar = urljoin(config.QN_CLOUD_URL, filename)
    user.save()






