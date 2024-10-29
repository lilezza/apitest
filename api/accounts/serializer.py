from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import User

class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "id" ,
            "first_name" ,
            "last_name" ,
            "age" ,
            "published_date" ,
            "detail_url"
        ]
    def get_detail_url(self , obj):
        request = self.context.get('request')
        return reverse('userpostdetail' , kwargs = {'pk' : obj.pk} , request=request)
