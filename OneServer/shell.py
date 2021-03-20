from db.models import KeyWord
from db.serializers import KeyWordSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = KeyWord(name='toandz',des='Toan dep trai')
snippet.save()

snippet = KeyWord(name='toandong',des='Toan cho dien')
snippet.save()

serializer = KeyWordSerializer(snippet)
serializer.data