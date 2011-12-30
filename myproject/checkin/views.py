from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from checkin.models import Pan

def index(request):
    pans = Pan.objects.all()
	return render_to_response('checkin/index.html', {'pans' : pans})
#   return HttpResponse("Hello BookStore!")

#def detail(request, book_id):
#  book =  get_object_or_404(Book, id = book_id)
#  return render_to_response('book/detail.html', {'book' : book})