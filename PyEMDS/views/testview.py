import datetime
from django.http import HttpResponse

__author__ = 'Max'


def testview(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
