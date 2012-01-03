from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from checkin.models import Pan

def index(request):
	pans = Pan.objects.all()
	return render_to_response('checkin/index.html', {'pans' : pans})
#   return HttpResponse("Hello BookStore!")

def detail(request, pan_id):
  pan =  get_object_or_404(Pan, id = pan_id)
  return render_to_response('checkin/detail.html', {'pan' : pan})