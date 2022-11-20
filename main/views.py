from django.http import HttpResponse


def get_some(request):
    name = request.GET['name']
    message = request.GET['message']
    return HttpResponse(f"Hello, {name}!{message}!")
