"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.views.static import serve  # 处理静态文件
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from companyinfo.views import Index, ContactView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # django-jet 路由
    path('admin/', admin.site.urls),        # 后台管理系统
    path('', Index.as_view(), name='index'),   # 首页
    path('contactus/', ContactView.as_view(), name='contactus'),   # 接收用户留言
]

if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
