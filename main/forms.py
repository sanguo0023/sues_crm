#coding=utf-8
#!/usr/bin/env python
from django import forms
from models import *

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('goods', 'number')
