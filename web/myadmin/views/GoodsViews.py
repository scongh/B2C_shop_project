from django.shortcuts import render
from django.http import HttpResponse

from . CatesViews import get_cates_all # 商品分类下拉框函数
from . UsersViews import uploads_pic # 图片处理函数
from .. models import Cates,Goods

from django.db.models import Q

# Create your views here.

# 商品添加 -- 内容填写页面
def good_add(request):
    # 下拉框
	catelist = get_cates_all()
	# 分配
	context = {'catelist': catelist} # catelist 为里面的数据
	

	return render(request,'myadmin/goods/add.html',context)

# 商品添加-执行
def good_insert(request):
	# 接收表单数据
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    # print(111,data)
    # return HttpResponse('添加成功')
    data['cateid'] = Cates.objects.get(id = data['cateid'])

    # 头像上传
    # 接收上传的文件
    myfile = request.FILES.get('pic',None)
    if not myfile:
        # 没有选择头像上传,
        return HttpResponse('<script>alert("没有商品图片上次上传");history.back(-1);</script>')

    # 处理头像的上传  1.jpg ==> [1,jpg]
    data['pic_url'] = uploads_pic(myfile)

    print(data)
    
    try:
        # 创建模型,添加数据
        ob = Goods(**data)
        ob.save()
        return HttpResponse('<script>alert("添加成功");location.href="/myadmin/good/index/";</script>')
    except:
        pass
    return HttpResponse('<script>alert("添加失败");history.back(-1);</script>')


# 商品列表
def good_index(request):
	data = Goods.objects.all()

	# 获取搜索条件
	types = request.GET.get('types',None)
	keywords = request.GET.get('keywords',None)
    # 搜索判断
	if types=="all":
		data = data.filter(Q(id__contains = keywords) | Q(goodsname__contains = keywords))
    #     data = data.filter(id__contains = keywords)
	elif types:
		search = {types+'__contains': keywords}
		data = data.filter(**search)

    # 导入分页类
	from django.core.paginator import Paginator
	p = Paginator(data, 10) # 实例化
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


	return render(request,'myadmin/goods/index.html',context)
	


