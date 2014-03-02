from django.db import models

# Create your models here.
class Goods(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField(blank = True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Operator(models.Model):
	name = models.CharField(max_length=30)
	level = models.PositiveSmallIntegerField(default=3)
	account = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Stock(models.Model):
	extra = models.PositiveIntegerField()
	goods = models.ForeignKey(Goods)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['extra']


class Outer(models.Model):
	number = models.PositiveIntegerField()
	goods = models.ForeignKey(Goods)
	operator = models.ForeignKey(Operator)

	def __unicode__(self):
		return self.name

class Inner(models.Model):
	number = models.PositiveIntegerField()
	goods = models.ForeignKey(Goods)
	operator = models.ForeignKey(Operator)

	def __unicode__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=30)
	tel = models.PositiveIntegerField(blank=True)
	email = models.EmailField(blank=True)
	address = models.CharField(max_length=60)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Order(models.Model):
	customer = models.ForeignKey(Customer)
	goods = models.ForeignKey(Goods)
	number = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name

