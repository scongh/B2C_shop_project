from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myadmin import models
from django.contrib.auth.hashers import make_password, check_password


# 登录注册视图
# 登录
def myhome_login(request):

    return render(request,'myhome/login/login.html')

# 执行登录
def myhome_dologin(request):
    try:
        # 验证手机号 用户是否存在
        obj = models.Users.objects.get(phone=request.POST['phone'])
        # 用户输入的密码与数据库解析的密码进行对比
        ps = check_password(request.POST['password'],obj.password)
        if ps:
            request.session['VipUser'] = {'uid':obj.id,'nikename':obj.nikename,'phone':obj.phone,'pic_url':obj.pic_url}
            return HttpResponse("<script>alert('登录成功');location.href='/'</script>")
    except:

        return HttpResponse("<script>alert('手机号或密码不正确');location.href='/login/'</script>")

# 退出登录
def myhome_loginout(request):
    # 删除
    del request.session['VipUser']
    return HttpResponse("<script>alert('退出登录');location.href='/'</script>")


# 注册
def myhome_register(request):

    return render(request,'myhome/login/register.html')

# 执行注册
def myhome_doregister(request):

    # 接收表单注册的数据
    obj = request.POST.dict()
    obj.pop('csrfmiddlewaretoken')

    obj.pop('vcode')
    # print(obj)

    # 验证手机号是否存在
    res = models.Users.objects.filter(phone=request.POST.get('phone'))
    if res:
        return HttpResponse("<script>alert('该手机号已注册');history.back(-1)</script>")
    else:
        obj['password'] = make_password(request.POST['password'], None, 'pbkdf2_sha256')
        obj = models.Users(**obj)
        obj.save()
        return HttpResponse("<script>alert('可使用');location.href='/login/'</script>")


# 短信验证
def myhome_sendmsg(request):
    phone = request.GET.get('phone')
    print(phone)

    return JsonResponse({'msg':'successful','code': 0})