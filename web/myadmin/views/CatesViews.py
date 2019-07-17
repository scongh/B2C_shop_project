from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from .. models import Cates

# 商品类别添加
def cate_add(request):
    if(request.method == 'POST'):
    	# 接收数据
    	data = {}
    	data['name'] = request.POST.get('name')
    	data['pid'] = request.POST.get('pid')
    	# data['path'] = '0,'

    	if data['pid']== '0':
    		data['path'] = '0,'
    	else:
    		# 获取父级路径
    		pob = Cates.objects.get(id = data['pid'])
    		# 拼接path
    		data['path'] = pob.path + data['pid'] + ','
    	print(data)

    	# 数据添加
    	ob = Cates(**data)
    	ob.save()
    	return HttpResponse('<script>alert("添加成功");location.href="/myadmin/cate/index/";</script>')
    else:
    	# 获取当前已有的 分类数据
    	# catelist = Cates.objects.all()
    	catelist = get_cates_all()
    	# 分配
    	context = {'catelist': catelist} # catelist 为里面的数据
    	# 加载商品模板页面
    	return render(request,'myadmin/cates/add.html',context)


# 商品类别列表
def cate_index(request):
	data = get_cates_all()
	# data = Cates.objects.all()
	context = {'catelist': data}
	return render(request,'myadmin/cates/index.html',context)

# 排序+缩减格式化
def get_cates_all():
	# 排列方式 
	# sql = "SELECT *,CONCAT(path,id) AS paths FROM myadmin_cates ORDER BY paths;"
	# sql注入 -- 容易出现漏洞
	# data = Cates.objects.raw(sql)s

	# django的排序
	data = Cates.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')

	# 缩进处理
	for i in data:
		# lens = len(i.path.split(',')) - 2
		lens = i.path.count(',') - 1
		i.tab = '|——'*lens
		# print(lens)

		if i.pid == 0:
			i.pname = '顶级'
		else:
			pob = Cates.objects.get(id = i.id)
			i.pname = pob.name
	return data

# 商品分类删除
def cate_del(request):

	# this window--窗体对象 --> 文档对象(DOM), location(地址对象), history(历史对象)

	# 接收id，获取对象
	cid = request.GET.get('cid')

	# 判断分类下是否有子类
	res = Cates.objects.filter(pid=cid).count()
	if res:
		return JsonResponse({'msg':'该类别下还有分类，不可删除','code':1})

	# 分类下是否有商品--后期完成

	# 执行删除
	ob = Cates.objects.get(id=cid)
	ob.delete()

	return JsonResponse({'msg':'删除成功','code':0})

# ---name编辑
def cate_edit(request):
	try:
		# 接收id
		cid = request.GET.get('cid')
		# 接收修改后的name
		newname = request.GET.get('newname')

		# 入库
		ob = Cates.objects.get(id=cid)
		ob.name = newname
		ob.save()
		data = {'msg': '更新成功', 'code': 0}
	except:
		data = {'msg': '更新失败，请重新操作', 'code': 1}

	return JsonResponse(data)