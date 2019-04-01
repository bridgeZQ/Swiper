from django.shortcuts import render
from django.http import JsonResponse

from lib.sms import send_sms
from lib.http import render_json
# Create your views here.


def submit_phone(request):
    """先提交手机号码"""
    phonenum = request.POST.get('phone')
    # 拿到手机号码去发短信
    send_sms(phonenum)
    return render_json(data=None)

def submit_vcode(request):
    """获取验证码登录注册"""
    return

def get_profile(request):
    """获取个人资料"""
    return

def edit_profile(request):
    """修改个人资料"""
    return

def upload_avatar(request):
    """头像上传"""
    return