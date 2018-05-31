from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('urlizer/index.html')
    context = {
        'userInput': request.POST.get('userInput'),
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(template.render(context, request))
