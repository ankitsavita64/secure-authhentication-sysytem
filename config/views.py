from django.http import HttpResponse

def Home(request):
    return HttpResponse("this is my secure authentication system project")

