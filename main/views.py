from django.http import HttpResponse
def index(response):
    return HttpResponse("<h1>witam gracza</h1>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")

