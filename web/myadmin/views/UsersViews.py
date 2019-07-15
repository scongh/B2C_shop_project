from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password
from .. models import Users
import os

from web.settings import BASE_DIR
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
# 用户模型的管理

# 会员添加表单
def user_add(request):
    return render(request,'myadmin/users/add.html')

# 会员执行添加
def user_insert(request):
    # 接收表单数据
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')

    # 处理密码 加密
    data['password'] = make_password(data['password'], None, 'pbkdf2_sha256')

    # 头像上传
    # 接收上传的文件
    myfile = request.FILES.get('pic',None)
    if not myfile:
        # 没有选择头像上传,
        return HttpResponse('<script>alert("没有选择头像上传");history.back(-1);</script>')

    # 处理头像的上传  1.jpg ==> [1,jpg]
    data['pic_url'] = uploads_pic(myfile)
    
    try:
        # 创建模型,添加数据
        ob = Users(**data)
        ob.save()
        return HttpResponse('<script>alert("添加成功");location.href="/myadmin/user/index/";</script>')
    except:
        pass
    return HttpResponse('<script>alert("添加失败");history.back(-1);</script>')


# 会员列表
def user_index(request):
    # return HttpResponse('user_index')
    # 获取所有用户数据
    data = Users.objects.all()

    # 导入分页类
    from django.core.paginator import Paginator
    p = Paginator(data, 3) # 实例化
    # 获取当前的页码数
    page_index = request.GET.get('page',1)
    # 获取当前 页数
    user_list = p.page(page_index)
    # 总页数
    # pages = p.page_range # range()列表
    # pages = p.num_pages # 分页的总页数

    # print(pages[-1])
    # 分配数据
    # context = {'userlist': user_list,'pages': pages,'pages_max':pages[-1]}
    context = {'userlist': user_list}

    # 加载模板
    return render(request,'myadmin/users/index.html',context)


# 头像上传的处理代码objects
def uploads_pic(myfile):
    try:
        import time
        filename = str(time.time())+"."+myfile.name.split('.').pop()
        destination = open(BASE_DIR+"/static/uploads/"+filename,"wb+")
        for chunk in myfile.chunks():# 分块写入文件  
            destination.write(chunk)  
        destination.close()
        return '/static/uploads/'+filename
    except:
        return False


# 会员编辑
def user_edit(request):
    # 接受会员用户id
    uid = request.GET.get('uid')
    # 获取会员用户对象
    uob = Users.objects.get(id=uid)

    print(uid)
    # # 判读当前的请求方式
    if request.method == 'POST':
        # 执行更新操作
        if request.POST.get('password',None):
            uob.password = make_password(request.POST['password'], None, 'pbkdf2_sha256')

        # 判断头像是否更新
        myfile = request.FILES.get('pic',None)
        if myfile:
            # 有新头像上传，则先删除原头像
            os.remove(BASE_DIR+uob.pic_url)
            # 更新头像
            uob.pic_url = uploads_pic(myfile)

        # 更新其他数据
        uob.nikename = request.POST.get('nikename')
        uob.email = request.POST.get('email')
        uob.phone = request.POST.get('phone')
        uob.age = request.POST.get('age')
        uob.sex = request.POST.get('sex')
        uob.save()

        return HttpResponse('<script>alert("更新成功");location.href="/myadmin/user/index/";</script>')

    elif request.method == 'GET':
        # 显示编辑表单
        context = {'uinfo': uob}
        return render(request,'myadmin/users/edit.html/',context)
