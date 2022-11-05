from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader


def index(request):
    # inject the respective values in HTML template
    html_message = loader.render_to_string(
        'email_sender_app/message.html',
        {
            # TODO: Enter the recipient name
            'name': 'Recipient Name',
            # TODO:  Update with your own body
            'body': 'This email is to verify whether we can send email in Django from Gmail account.',
            # TODO: Update the signature
            'sign': 'Sender',
        })
    send_mail(
        'Congratulations!',
        'You are lucky to receive this mail.',
        '',  # TODO: Update this with your mail id
        [],  # TODO: Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("Mail Sent!!")
