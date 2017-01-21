from rest_framework.serializers import ModelSerializer
from Genre.models import Genres

class dataSearializer(ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'