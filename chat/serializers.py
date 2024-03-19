from .models import Chat, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'file')


class ChatListSerializer(serializers.ModelSerializer):
    initiator = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()

    class Meta:
        model = Chat
        fields = ['initiator', 'receiver']


class ChatSerializer(serializers.ModelSerializer):
    initiator = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['initiator', 'receiver', 'messages']
