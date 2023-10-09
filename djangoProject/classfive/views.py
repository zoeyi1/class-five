from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import InquiryForm
from django.conf import settings

# email stuff
import smtplib
from email.message import EmailMessage
import os

from .models import Event, Slide, Card, TeamMember

def home(request):
    slideInstances = Slide.objects.all()
    return render(request, "classfive/home.html", {"slideInstances": slideInstances})

def events(request):
    cardInstances = Card.objects.all()
    return render(request, "classfive/events.html", {"cardInstances": cardInstances})

def contact(request):
    form = InquiryForm()
    success_message = None
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            def send_email(subject, message, to_email):
                # Your Google account details
                gmail_user = 'superzoeyi@gmail.com'
                gmail_password = settings.EMAIL_HOST_PASSWORD
                #gmail_password =os.environ.get('EMAIL_HOST_PASSWORD')
                # Create a new email message
                msg = EmailMessage()
                msg.set_content(message)
                msg['Subject'] = subject
                msg['From'] = gmail_user
                msg['To'] = to_email

                # Connect to Gmail's SMTP server
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(gmail_user, gmail_password)
                        server.send_message(msg)
                        print("Email sent successfully!")
                        return InquiryForm(), "Thank you for your inquiry! We will get back to you soon."
                except Exception as e:
                    print(f"Failed to send email: {e}")
                    return InquiryForm(), None

            form, success_message = send_email(f'New Inquiry | Type: {form.cleaned_data["inquiry_type"]} | From: {form.cleaned_data["name"]}', 
                       f'Email: {form.cleaned_data["email"]}\n\nMessage: {form.cleaned_data["message"]}', 
                       "superzoeyi@gmail.com")
            '''
            try:
                # Your Google account details
                gmail_user = 'superzoeyi@gmail.com'
                gmail_password = 'egoi rrwz stys aypt'
                
                # Compose the email message
                subject = f'New Inquiry: {form.cleaned_data["inquiry_type"]} from {form.cleaned_data["name"]}'
                message = f'Email: {form.cleaned_data["email"]}\n\n{form.cleaned_data["message"]}'
                
                # Use Django's send_mail function
                send_mail(subject, message, gmail_user, ['superzoeyi@gmail.com'])
                
                print("Email sent successfully!")
                form = InquiryForm()  # Clear the form
                success_message = "Thank you for your inquiry! We will get back to you soon."
            except Exception as e:
                print(f"Failed to send email: {e}")
                form = InquiryForm()
                success_message = None
            '''

    return render(request, 'classfive/contact.html', {'form': form, 'success_message': success_message})

def philosophy(request):
    return render(request, "classfive/philosophy.html")

def merch(request):
    return render(request, "classfive/merch.html")

def training(request):
    return render(request, "classfive/training.html")

def team(request):
    teamMemberInstances = TeamMember.objects.all()
    return render(request, "classfive/team.html", {"teamMemberInstances": teamMemberInstances})

