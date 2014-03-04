from main.models import *
from django.contrib import admin

# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'description', )
	search_fields = ('name', )
	list_filter = ('price', )
	fields = ('name', 'price', 'description', )

class StockAdmin(admin.ModelAdmin):
	list_display = ('goods', 'extra', )
	search_fields = ('goods', )
	list_filter = ('extra', )
	fields = ('goods', 'extra', )

class OuterAdmin(admin.ModelAdmin):
	list_display = ('goods', 'number', 'operator', )
	search_fields = ('goods', )
	list_filter = ('operator', )
	fields = ('goods', 'number', 'operator', )

class InnerAdmin(admin.ModelAdmin):
	list_display = ('goods', 'number', 'operator', )
	search_fields = ('goods', )
	list_filter = ('operator', )
	fields = ('goods', 'number', 'operator', )

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', )
	search_fields = ('name', 'address', )
	list_filter = ('address', )
	fields = ('name', 'tel', 'email', 'address', )

class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer', 'goods', 'number', )
	search_fields = ('customer', )
	list_filter = ('customer', )
	fields = ('customer', 'goods', 'number', )

class OperatorAdmin(admin.ModelAdmin):
	list_display = ('name', 'level', )
	search_fields = ('name', )
	list_filter = ('name', )
	fields = ('name', 'level', 'account', 'password', )

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Outer, OuterAdmin)
admin.site.register(Inner, InnerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Operator, OperatorAdmin)
