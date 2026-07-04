from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hi my self Ankit this is my secure authentication system deployed by AWS(EC2 Server).")

