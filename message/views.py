from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Message
import json


@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        req_body = json.loads(request.body)
        new_message = Message(**req_body)
        new_message.save()
        return JsonResponse({'message': 'mesage sent successfully'})

    else:
        return JsonResponse({'error': 'try a post request'})


def get_all_messages_for_user(request, user_id):
    try:
        queryset = Message.objects.filter(receiver_id=user_id).all()
        messages = list(queryset.values())
        return JsonResponse({"messages": messages})
    except:
        return JsonResponse({{"error": "no messages found"}})


def get_unread_messages_for_user(request, user_id):
    try:
        queryset = Message.objects.filter(
            receiver_id=user_id, status="UNREAD").all()
        messages = list(queryset.values())
        return JsonResponse({"messages": messages})
    except:
        return JsonResponse({"error": "no unread messages found"})


def get_message(request, message_id):
    try:
        message = Message.objects.filter(pk=message_id).values()[0]
        return JsonResponse({"message": message})
    except:
        return JsonResponse({"error": "message not found"})


def delete_message(request, message_id):
    message = Message.objects.filter(pk=message_id)
    if message:
        message.delete()
        return JsonResponse({"message": f"message {message_id} deleted"})
    else:
        return JsonResponse({"error": "message not found"})
