from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from message.models import Message
from message.serializers import MessageSerializer
# Kafka
from kafka import KafkaProducer
import pickle

# class CreateUser(APIView):
#     def post(self,request, format = None):
#         # Создайте пользователя и сохраните его в базе данных
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = User.objects.create_user(username, '', password)
#         token = get_tokens_for_user(user)
#         print(token)
#         # Обновите поля и сохраните их снова
#         user.save()
#         return Response('User created', status=status.HTTP_201_CREATED)

class CreateMessage(APIView):
    def post(self,request, format = None):
        serializer = MessageSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        kfk(serializer.data)
        return Response(serializer.data, status= status.HTTP_201_CREATED)
        #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ReceiveMessage(APIView):
    def post(self,request, format = None):
        msg = Message.objects.get(id=request.data.get("id"))
        if request.data.get("success") == 'False':
            msg.status = 'correct'
        else:
            msg.status = 'blocked'
        msg.save()
        return Response({"success": True}, status=status.HTTP_201_CREATED)

def kfk(data):
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    v = data
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    producer.send('testnum', serialized_data)
    return HttpResponse(200)


# def get_tokens_for_user(user):
#      refresh = RefreshToken.for_user(user)
#
#      return {
#      'refresh': str(refresh),
#     'access': str(refresh.access_token),
# }
