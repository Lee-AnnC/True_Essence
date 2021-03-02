from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        message = request.POST['message']
        return render(request, 'contact/contact.html', {'first_name': first_name})

        # send an email
        send_mail()
        'message from' + 'first_name' + 'last_name', #subject
        message, #message
        email, # from email
        ['example@gmail.com'], # to email

    else:
        return render(request, 'contact/contact.html', {})
