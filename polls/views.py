from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext


# Create your views here.
from models import Client

# def client_info(request,cli_id):
#     client=Client.objects.get(cli_clientid=cli_id)
#     return_data = {'client':client}


#     return render(request,"feedback/call_me.html",return_data)

def client_info(request): 
	clients=Client.objects.filter(cli_isused=0)
	if 'view_hidden' in request.GET:
		clients = clients.filter(display=0)
	else:
		clients = clients.filter(display=1)	
	print "pppppppppppppppppppppppp"	
	return render(request,'client/client_list.html',{'clients':clients}) 



def client_details(request,id):
	client=Client.objects.get(id =id)
	# client.delete()
	# client_record={}

	return render(request,'client/client_data.html',{'client':client}) 


def client_insert(request): 
	var={}
	if request.POST:
 		import pdb; pdb.set_trace()
		client=Client()
		client.name=request.POST.get('c_name')
		client.mobile=request.POST.get('c_phone')
		client.phone=request.POST.get('c_mobile')
		client.address=request.POST.get('c_address')
		client.save()
	print "ppppppppXXXXXXXXXppppppppp"

	return render_to_response('client/client_insert.html',var,context_instance = RequestContext(request))


	# return render(request,'client/client_insert.html',var) 


	








