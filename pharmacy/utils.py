from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings


def send_html_email(subject, to_list, template, context, cc_list=['mohan@webchirpy.com','vasanth@webchirpy.com'], from_email=settings.DEFAULT_FROM_EMAIL,file_list=None ):
    if template:
        html_message = render_to_string(
            f"{template}",context
        )
    plain_message = strip_tags(html_message)
    # email=send_mail(subject=subject,message=plain_message,from_email=settings.EMAIL_HOST_USER, recipient_list=to_list,fail_silently=True)

    msg=EmailMultiAlternatives(subject=subject,body=plain_message,from_email=from_email,to=to_list,bcc=cc_list)
    if type(file_list) is list:
        for file in file_list:
            msg.attach(file)
    msg.send()
    print(msg,"msg")
    return "success"