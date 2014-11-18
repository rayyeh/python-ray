import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

from checkin.models import Pan


def index(request):
    pans = Pan.objects.all()
    return render_to_response('checkin/index.html', {'pans': pans})


# return HttpResponse("Hello BookStore!")

def detail(request, pan_id):
    pan = get_object_or_404(Pan, id=pan_id)
    return render_to_response('checkin/detail.html', {'pan': pan})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
  
