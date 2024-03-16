from django.shortcuts import render

# Create your views here.

def pick_and_speech(request):
    return render(request,"pick_and_speech.html")

def index(request):
    return render(request,"index.html")

def speed_typing(request):
    return render(request,"speed_typing.html")

def photography(request):
    return render(request,"photography.html")

def ppt(request):
    return render(request,"ppt.html")

def madad(request):
    return render(request,"madad.html")

def quiz(request):
    return render(request,"quiz.html")

def video(request):
    return render(request,"video.html")

def stressinterview(request):
    return render(request,"stressinterview.html")

def treasurehunt(request):
    return render(request,"treasurehunt.html")

def model(request):
    return render(request,"model.html")

def code(request):
    return render(request,"code.html")
