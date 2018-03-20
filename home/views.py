from django.shortcuts import render

def render_home_index(request):
    return render(request, 'home/index.html')