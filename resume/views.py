from django.http import HttpResponse

def http_test(request):
    return HttpResponse("<h1> this is my first views</h1>")