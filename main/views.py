#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from json import loads
from main.models import *
from main.forms import *

# Create your views here.
def index(request):
	return render_to_response('index.html', {})

def sns(request):
	return render_to_response('sns.html', {})

def show(request):
	goods = Goods.objects.all()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/index/')
	else:
		form = OrderForm()
	return render_to_response('show.html', {'goods': goods, 'form': form})

def load_css(request):
	str = 'http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css';
	return HttpResponse(str)

def show_image(request, path):
	image_data = open("static/images/" + path, "rb").read()
	return HttpResponse(image_data, mimetype="image/png")

def crm(request):
	json_text = open("static/json/info.json", "r").read()
	info = loads(json_text)
	return render_to_response('info.html', {'info': info})

