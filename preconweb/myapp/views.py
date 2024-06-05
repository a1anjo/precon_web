from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def warema(request):
    return render(request,'warema.html')

def overlap(request):
    return render(request,'overlap.html')

def thankyou(request):
    return render(request,'thankyou.html')

def contact(request):
    return render(request,'contact.html')

def serge(request):
    return render(request,'serge.html')

def origin(request):
    return render(request,'origin.html')

def other_products(request):
    return render(request,'other_products.html')

def brouchere(request):
    return render(request,'brouchere.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_email = 'alanantony96696@gmail.com'  # Specify the recipient's email address
        
        try:
            send_mail(
                subject,
                f'From: {name}\nEmail: {email}\n\n{message}',
                email,  # Sender's email address
                [recipient_email],  # Recipient's email address
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')

        return redirect('thankyou')  # Redirect to a thank you page or any desired page

    return render(request, 'thankyou.html')  # Render the template containing the contact form

