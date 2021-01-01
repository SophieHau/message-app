from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    READ = 'READ'
    UNREAD = 'UNREAD'

    MESSAGE_STATUS_CHOICES = [
        (READ, 'Read'),
        (UNREAD, 'Unread'),
    ]

    sender = models.ForeignKey(
        User, related_name='senders', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(
        User, related_name='receivers', on_delete=models.DO_NOTHING)
    message = models.TextField()
    subject = models.CharField(max_length=500)
    status = models.CharField(
        max_length=50, choices=MESSAGE_STATUS_CHOICES, default=UNREAD)
    creation_date = models.DateField(auto_now_add=True)
