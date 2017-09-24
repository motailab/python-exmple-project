from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text': 'Hello i\'am motailab', 'number': 50}
    return render(request, 'app/index.html', context)

def other(request):
    return render(request, 'app/other.html')

def relative(request):
    return render(request, 'app/relative_url_templates.html')