from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from email.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
from .models import *
def index(request):
    portfolio_images=Portfolio_images.objects.all()
    about = About.objects.all()
    categoriya = Categoriya.objects.all()
    service = Service.objects.all()
    portfolio = Portfolio.objects.all()
    specialized = Specialized.objects.all()
    ctx = {
        "portfolio_images":portfolio_images,
        "about":about,
        "categoriya": categoriya,
        "service" : service,
        "portfolio" : portfolio,
        "specialized":specialized

    }

    return render(request, "main/index.html",ctx)

def portfolio(request,id):
    portfolio_images = Portfolio_images.objects.filter(portfolio_id=id)
    about = About.objects.all()
    categoriya = Categoriya.objects.all()
    service = Service.objects.all()
    portfolio = Portfolio.objects.all()
    specialized = Specialized.objects.all()
    ctx = {
        "portfolio_images": portfolio_images,
        "about": about,
        "categoriya": categoriya,
        "service": service,
        "portfolio": portfolio,
        "specialized": specialized

    }
    return render(request, "main/index.html", ctx)



def send_email(request):
    if request.method == "Post":
        name = request.Post["name"]
        sender_email = request.Post["sender_email"]
        subject = request.Post["subject"]
        msg = request.Post["msg"]

        email = EmailMessage(
            f'Sent by : {sender_email}',
            f'Name : {name}\n\n Subject : {subject}\n\n Message : {msg}',
            settings.EMAIL_HOST_USER,
            {sender_email}
        )
        email.fail_silently=True
        email.send()
        return HttpResponse("Sent successfully")
    else :
        return HttpResponse("Error")