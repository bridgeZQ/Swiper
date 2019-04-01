"""发短信"""
import random
import requests

from swiper import config


def gen_vcode(length=4):
    start = 10 ** (length - 1)
    end = 10 ** (length) -1
    return random.randint(start,end)

def send_sms(phonenum):
    vcode = gen_vcode()
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS.copy()
    params['param'] = vcode
    params['mobile'] = phonenum
    resp = requests.post(url=url,json=params)
    # 对结果做一些检查
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return  True,result['msg']
        else:
            return False,result['msg']
    else:
        return '短信服务通信有误'