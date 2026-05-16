from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def traffic(request):
    return render(request, 'traffic.html')

def logs(request):
    return render(request, 'logs.html')

def analytics(request):
    return render(request, 'analytics.html')

def blocks(request):
    return render(request, 'blocks.html')