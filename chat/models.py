from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model


class Chat(BaseModel):
    initiator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='chat_initiator')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='chat_receiver')

    def __str__(self):
        return f'Chat to {self.receiver}'

    class Meta:
        unique_together = (('initiator', 'receiver'), ('receiver', 'initiator'))


class Message(BaseModel):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    content = models.TextField()

    file = models.FileField(upload_to='messages/')
