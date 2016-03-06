from django.http import HttpResponse
import datetime

def home_page(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>HELLO</h1>It is now %s.</body></html>" % now
    return HttpResponse(html)