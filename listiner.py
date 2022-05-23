# importing the required modules
import pickle
import re

from testrerikom.wsgi import *
import requests
from kafka import KafkaConsumer
my_consumer = KafkaConsumer(
    'testnum',
     bootstrap_servers = ['localhost : 9092'],
     api_version=(0,10,1),
     auto_offset_reset = 'ea rliest',
     enable_auto_commit = True,
     group_id = 'my-group',
     #value_deserializer = lambda x : loads(x.decode('utf-8'))
     )
for msg in my_consumer:
    deserialized_data = pickle.loads(msg.value)
    if re.search(r'\абракадабра\b', deserialized_data['message'].lower()):
        post_data = {'id': deserialized_data['id'], 'success': True}
        response = requests.post('http://127.0.0.1:8000/api/v1/message_confirmation/', post_data)
    else:
        post_data = {'id': deserialized_data['id'], 'success': False}
        response = requests.post('http://127.0.0.1:8000/api/v1/message_confirmation/', post_data)
