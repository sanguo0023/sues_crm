#coding=utf-8
from django.db import models

# Create your models here.
class Goods(models.Model):
	name = models.CharField(max_length=30, verbose_name="产品名")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
	description = models.TextField(blank = True, verbose_name="描述")

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Operator(models.Model):
	name = models.CharField(max_length=30, verbose_name="操作员姓名")
	level = models.PositiveSmallIntegerField(default=3, verbose_name="权限等级")
	account = models.CharField(max_length=30, unique=True, verbose_name="登录帐号")
	password = models.CharField(max_length=30, verbose_name="密码")

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Stock(models.Model):
	extra = models.PositiveIntegerField(verbose_name="库存数量")
	goods = models.ForeignKey(Goods)

	class Meta:
		ordering = ['extra']


class Outer(models.Model):
	number = models.PositiveIntegerField(verbose_name="出库数量")
	goods = models.ForeignKey(Goods)
	operator = models.ForeignKey(Operator)
	time = models.DateTimeField(verbose_name="出库时间", auto_now_add=True, editable=False)

class Inner(models.Model):
	number = models.PositiveIntegerField(verbose_name="入库数量")
	goods = models.ForeignKey(Goods)
	operator = models.ForeignKey(Operator)
	time = models.DateTimeField(verbose_name="入库时间", auto_now_add=True, editable=False)

class Customer(models.Model):
	name = models.CharField(max_length=30, verbose_name="客户姓名")
	tele_phone = models.PositiveIntegerField(blank=True, verbose_name="固定电话")
	mobile_phone = models.PositiveIntegerField(blank=True, verbose_name="移动点换")
	email = models.EmailField(blank=True, verbose_name="电子邮件")
	address = models.CharField(max_length=60, verbose_name="通讯地址")

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Order(models.Model):
	customer = models.ForeignKey(Customer)
	goods = models.ForeignKey(Goods)
	number = models.PositiveIntegerField(verbose_name="订购数量")
	time = models.DateTimeField(verbose_name="订购时间", auto_now_add=True, editable=False)

	def __unicode__(self):
		return self.name
