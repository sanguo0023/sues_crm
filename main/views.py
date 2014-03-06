#coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from json import loads
from main.models import *
from main.forms import *
from json import loads
import urllib, urllib2, csv

# Create your views here.
def index(request):
	return render_to_response('index.html', {})

def to_csv(request):
	response = HttpResponse(mimetype='text/csv')
	response['Content-Disposition'] = 'attachment; filename=unruly.csv'

	writer = csv.writer(response)
	customer = Customer.objects.all()
	writer.writerow(['客户姓名', '固定电话', '移动电话', '电子邮件', '通讯地址'])
	for item in customer:
		data = zip([item.name, item.tele_phone, item.mobile_phone, item.email, item.address])
		writer.writerow(data)

	return response

def crm(request):
	customer = Customer.objects.all()
	return render_to_response('crm.html', {'customer': customer})


def show(request):
	goods = Goods.objects.all()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/show/')
	else:
		if not request.session.get('customer_id'):
			return HttpResponseRedirect('/login/')
		else:
			form = OrderForm()
			user = request.session
			return render_to_response('show.html', {'goods': goods, 'form': form, 'user': user})

def show_image(request, path):
	image_data = open("static/images/" + path, "rb").read()
	return HttpResponse(image_data, mimetype="image/png")

def info(request):
	json_text = open("static/json/info.json", "r").read()
	info = loads(json_text)
	return render_to_response('info.html', {'info': info})

def doc(request):
	return render_to_response('doc.html', {})

def login(request):
	if request.method == 'POST':
		data = request.POST
		try:
			user = Customer.objects.get(account=data['account'], password=data['password'])
		except Customer.DoesNotExist:
			return render_to_response('login.html', {'error': '用户名或密码错误'})
		else:
			request.session['customer_id'] = user.id
			request.session['customer_name'] = user.name
			return HttpResponseRedirect('/show/')
	else:
		return render_to_response('login.html', {})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			form.save()
			request.session['customer_id'] = Customer.objects.get(account=data['account']).id
			request.session['customer_name'] = data['name']
			return HttpResponseRedirect('/show/')
		else:
			return render_to_response('register.html', {'error': '您输入的表单不符合规范，请重新输入', 'form': form})
	return render_to_response('register.html')
