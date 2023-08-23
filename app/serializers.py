from rest_framework.serializers import ModelSerializer
from .models import News

class NewSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title','text')