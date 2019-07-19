from django.db import models

# Create your models here.


# 定义会员模型
class Users(models.Model):
    nikename = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=77)
    # phone = models.CharField(max_length=11,unique=True)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    pic_url = models.CharField(max_length=100)
    SEX_CHOICES = (
        (0, '女'),
        (1, '男'),
    )
    sex = models.CharField(max_length=1,null=True,choices=SEX_CHOICES)
    # 0 正常  1禁用  2 删除 ....
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)

# 商品分类  -- 无限分类(一般2~3级)
class Cates(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)

# 商品模型
class Goods(models.Model):
    # 所属分类id 、商品name、商品标题、价格、数量、图片-路径、商品的描述、销量、点击次数
    cateid = models.ForeignKey(to='Cates', to_field='id') # 多对一
    goodsname = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    goodsnum = models.IntegerField()
    pic_url = models.CharField(max_length=255)
    goodsinfo = models.TextField()
    ordernum = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    # 状态--0新品、1热卖、2推荐、3下架   、 添加时间
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)

    