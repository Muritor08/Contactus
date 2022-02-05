import email
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == 'POST':
        msg_name = request.POST['msg_name']
        msg_email = request.POST['msg_email']
        msg = request.POST['msg']

        #send email

        send_mail(
            'Message from ' + msg_name, #subject
            msg ,# message
            msg_email ,#from email
            ['kamalspamemail8@gmail.com'], #toemail
        )
        
        return render(request, 'index.html',{'msg_name':msg_name})

    else:
        return render(request, 'index.html',{})