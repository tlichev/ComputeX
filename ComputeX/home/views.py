from django.shortcuts import render

# Create your views here.
def show_index(request):
    return render(request, template_name='home/index.html')