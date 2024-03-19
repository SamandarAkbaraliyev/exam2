from typing import Any
from urllib.request import Request

from rest_framework import generics
from chat.models import Chat, Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from .serializers import ChatListSerializer, ChatSerializer, MessageSerializer
from django.db.models import Q
from django.shortcuts import redirect, reverse


# Create your views here.
@api_view(['POST'])
def start_chat(request, ):
    data = request.data
    username = data.pop('username')
    try:
        participant = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'You cannot chat with a non existent user'})

    chat = Chat.objects.filter(Q(initiator=request.user, receiver=participant) |
                                               Q(initiator=participant, receiver=request.user))
    if chat.exists():
        return redirect(reverse('get_conversation', args=(chat[0].id,)))
    else:
        conversation = Chat.objects.create(initiator=request.user, receiver=participant)
        return Response(ChatSerializer(instance=conversation).data)


@api_view(['GET'])
def get_chat(request, convo_id):
    chat = Chat.objects.filter(id=convo_id)
    if not chat.exists():
        return Response({'message': 'Conversation does not exist'})
    else:
        serializer = ChatSerializer(instance=chat[0])
        return Response(serializer.data)


@api_view(['GET'])
def chats(request):
    chat_list = Chat.objects.filter(Q(initiator=request.user) |
                                                    Q(receiver=request.user))
    serializer = ChatListSerializer(instance=chat_list, many=True)
    return Response(serializer.data)


class PostMessageAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        sender = self.request.user
        chat_id = self.kwargs.get('chat_id')
        content = self.request.POST.get('content')
        print(content)
        if content:
            message = Message.objects.create(sender=sender, chat=Chat.objects.get(id=chat_id), content=content)
        return Response({'data': 'Succcess'})

