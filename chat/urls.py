from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_chat, name='start_convo'),
    path('<int:convo_id>/', views.get_chat, name='get_conversation'),
    path('', views.chats, name='conversations'),

    path('<int:chat_id>/post/', views.PostMessageAPIView.as_view()),
]
