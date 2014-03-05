#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from json import loads
from main.models import *
from main.forms import *
from json import loads
import urllib, urllib2, csv

# Create your views here.
def index(request):
	return render_to_response('index.html', {})

def sns(request):
	if 'code' in request.GET:
		#if 'access_token' not in request.session:
		params = urllib.urlencode({	'client_id': '1342064535', 
				'redirect_uri': 'http://127.0.0.1:8000/sns/',
				'client_secret': '9cc2ae929687f61cb3455c70093ce225',
				'grant_type': 'authorization_code', 
				'code': request.GET['code'], })

		data = urllib.urlopen('https://api.weibo.com/oauth2/access_token', params).read()
		token = loads(data)
		request.session['access_token'] = token['access_token']

		params = urllib.urlencode({	'uid': '5057273373', 'access_token': request.session['access_token'] })
		req = urllib2.Request('https://api.weibo.com/2/statuses/user_timeline.json', params)
		req.add_header('Content-Type', "application/x-www-form-urlencoded")
		data = urllib2.urlopen(req).read()
		titles = loads(data)

		params = urllib.urlencode({	'uid': '5057273373', 'access_token': request.session['access_token'] })
		req = urllib2.Request('https://api.weibo.com/2/comments/to_me.json', params)
		req.add_header('Content-Type', "application/x-www-form-urlencoded")
		data = urllib2.urlopen(req).read()
		comments = loads(data)

		return render_to_response('sns.html', {'titles': titles, 'comments': comments, 'token': token})
	else:
		return render_to_response('sns.html', {'data': ''})

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

def info(request):
	json_text = open("static/json/info.json", "r").read()
	info = loads(json_text)
	return render_to_response('info.html', {'info': info})

