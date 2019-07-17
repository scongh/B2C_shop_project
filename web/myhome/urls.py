from django.conf.urls import url
from .views import IndexViews,LoginViews

urlpatterns = [
    # 首页
    url(r'^$',IndexViews.myhome_index,name="myhome_index"),
    # 列表页
    url(r'^list/$', IndexViews.myhome_list, name="myhome_list"),
    # 详情页
    url(r'^info/$', IndexViews.myhome_info, name="myhome_info"),


    # 登录
    url(r'^login/$', LoginViews.myhome_login, name="myhome_login"),
    # 执行登录
    url(r'^dologin/$', LoginViews.myhome_dologin, name="myhome_dologin"),
    # 退出登录
    url(r'^loginout/$', LoginViews.myhome_loginout, name="myhome_loginout"),

    # 注册
    url(r'^register/$', LoginViews.myhome_register, name="myhome_register"),
    # 执行注册
    url(r'^doregister/$', LoginViews.myhome_doregister, name="myhome_doregister"),
    # 短信发送
    url(r'^sendmsg/$', LoginViews.myhome_sendmsg, name="myhome_sendmsg"),

]
