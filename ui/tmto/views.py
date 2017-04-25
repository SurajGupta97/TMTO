from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from iteration import *

def title(request):
	return render(request, 'index.html', {'title': 'TMTO'})

def function1(request):
	# data = None
	# if(request.GET.get('N')):
	# 	data = ( int(request.GET.get('N')) )
	# 	print data
	# if data is None:
	# 	data = "Kindly provide necessary inputs"	

	return render(request, 'function1.html', {'title': 'TMTO'})

def function2(request):
	return render(request, 'function2.html', {'title': 'TMTO'})

def function3(request):
	return render(request, 'function3.html', {'title': 'TMTO'})

@csrf_exempt
def function1_oninput(request):
	
	n = None
	plainText = None
	iter = None
	cipher = None
	key = None

	data = ""

	if(request.POST.get('N')):
		n = ( int(request.POST.get('N')) )

	if(request.POST.get('plainText')):
		plainText = int(request.POST.get('plainText'))

	if(request.POST.get('iter')):
		iter = ( int(request.POST.get('iter')) )

	if(request.POST.get('cipher')):
		cipher = request.POST.get('cipher')

	# if(request.POST.get('key')):
	# 	key = request.POST.get('key')				

	# data = str(plainText)+str(iter)+str(cipher)+str(key)
	data = function11(cipher,n,plainText,iter)
	return HttpResponse(data)

@csrf_exempt
def function2_oninput(request):
	
	n = None
	m = None
	t = None
	plainText = None
	iter = None
	cipher = None
	key = None

	data = ""

	if(request.POST.get('N')):
		n = ( int(request.POST.get('N')) )

	if(request.POST.get('m')):
		m = ( int(request.POST.get('m')) )

	if(request.POST.get('t')):
		t = ( int(request.POST.get('t')) )

	if(request.POST.get('plainText')):
		plainText = int(request.POST.get('plainText'))

	if(request.POST.get('iter')):
		iter = ( int(request.POST.get('iter')) )

	if(request.POST.get('cipher')):
		cipher = request.POST.get('cipher')

	# if(request.POST.get('key')):
	# 	key = request.POST.get('key')				

	# data = str(m)+str(t)+str(plainText)+str(iter)+str(cipher)+str(key)
	data = "Accuracy observed is: " + str(function22(cipher,m,t,n,plainText,iter))
	return HttpResponse(data)

@csrf_exempt
def function3_oninput(request):
	
	n = None
	m = None
	t = None
	plainText = None
	cipher = None
	key = None

	data = ""

	if(request.POST.get('N')):
		n = ( int(request.POST.get('N')) )

	if(request.POST.get('m')):
		m = ( int(request.POST.get('m')) )

	if(request.POST.get('t')):
		t = ( int(request.POST.get('t')) )

	if(request.POST.get('plainText')):
		plainText = int(request.POST.get('plainText'))

	if(request.POST.get('cipher')):
		cipher = request.POST.get('cipher')

	if(request.POST.get('key')):
		key = request.POST.get('key')				


	# data = str(m)+str(t)+str(plainText)+str(cipher)+str(key)
	fl, key =  function33(cipher,m,t,n,plainText)
	data = None
	if fl==False:
		data = "Key not found"
	else:
		data = "Key: " + str(key)

	return HttpResponse(data)