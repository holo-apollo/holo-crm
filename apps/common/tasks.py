import logging

from django.core.mail import EmailMultiAlternatives, mail_managers
from django.template import loader
from django.utils import translation

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_email(recipient, subject, text_content, html_content=None):
    msg = EmailMultiAlternatives(subject, text_content, to=[recipient])
    if html_content:
        msg.attach_alternative(html_content, "text/html")
    logger.info('Sending email')
    msg.send()


@shared_task
def broadcast_email(recipients, subject, text_content, html_content=None):
    msg = EmailMultiAlternatives(subject, text_content, bcc=recipients)
    if html_content:
        msg.attach_alternative(html_content, "text/html")
    logger.info('Sending emails')
    msg.send()


# NOTE: context should be JSON-serializable, so it's better to put rendering to string outside
# of the task
@shared_task
def send_template_email(recipient, subject_template_name, email_template_name, context,
                        html_email_template_name=None, language=None):
    prev_language = translation.get_language()
    if language:
        translation.activate(language)
    try:
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
        else:
            html_email = None
        send_email(recipient, subject, body, html_email)
    finally:
        translation.activate(prev_language)


@shared_task
def send_email_to_managers(subject, message):
    mail_managers(subject, message)
