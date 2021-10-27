#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019-07-03 16:47"
from django.contrib import admin

from .models import CompanyInfo, Supers, Aboutus, Services, Customers, Pricing, Employees, Contact


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'info1', 'info2', 'phone', 'address', 'web']
    list_filter = ['name']
    search_fields = ['name']


class PricingAdmin(admin.ModelAdmin):
    list_display = ['info', 'item']
    list_filter = ['info', 'item']
    search_fields = ['info', 'item']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Supers)
admin.site.register(Aboutus)
admin.site.register(Services)
admin.site.register(Customers)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Employees)
admin.site.register(Contact)
