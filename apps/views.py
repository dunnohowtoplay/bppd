from django.shortcuts import render

# Create your views here.
app_name = 'apps'
def index(request):
    return render(request, 'apps/index.html')