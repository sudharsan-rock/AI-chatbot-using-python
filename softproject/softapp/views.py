from django.shortcuts import render
from chatbotse.chatbot1 import chat

# Create your views here.

def homepage(request):
    if request.method=='POST':
        userinput = request.POST.get('text')
        reply=chat(userinput)
        return render(request,'softapp/index.html',{'input':userinput,'response':reply})
    else:
        return render(request,'softapp/index.html')

