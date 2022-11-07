from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader

#third party import
from rest_framework.views import APIView
from rest_framework.response import Response

#local import
from .serializers import emailsenderserializer

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
        '',    # TODO: Update this with your mail id
        [''],  # TODO: Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("Mail Sent!!")

class emailsender(APIView):
    def post(self,request):
        serializer = emailsenderserializer(data=request.data)
        if serializer.is_valid():
            try:
                send_mail(
                    'Congratulations!',
                    'You are lucky to receive this mail.',
                    serializer.data['email'],  # TODO: Update this with your mail id
                    [serializer.data['remail']],  # TODO: Update this with the recipients mail id
                    html_message=serializer.data['body'],
                    fail_silently=False,
                )
                return Response("Email sent")
            except:
                return Response("Email didn't sent")
        else:
            return Response(f'{serializer.errors}')


