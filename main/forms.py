#coding=utf-8
#!/usr/bin/env python
from django import forms
from models import *

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('goods', 'number')

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('account', 'password')

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Customer
