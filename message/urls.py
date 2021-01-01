from django.urls import path
from . import views

urlpatterns = [
    path('add', views.post_message),
    path('<int:user_id>', views.get_all_messages_for_user),
    path('<int:user_id>/unread', views.get_unread_messages_for_user),
    path('message/<int:message_id>', views.get_message),
    path('delete/<int:message_id>', views.delete_message),
]
