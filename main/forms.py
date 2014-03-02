#coding=utf-8
#!/usr/bin/env python
from django import forms

class ContactForm(forms.Form):
	customer = models.ForeignKey(Customer)
	goods = models.ForeignKey(Goods)
	number = models.PositiveIntegerField()

