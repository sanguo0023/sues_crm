from django.contrib import admin

# Register your models here.
from main.models import *
admin.site.register(Goods)
admin.site.register(Stock)
admin.site.register(Outer)
admin.site.register(Inner)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Operator)
