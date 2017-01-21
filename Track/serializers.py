from rest_framework.serializers import ModelSerializer
from Track.models import Tracks

class dataSearializer(ModelSerializer):

    class Meta:
        model = Tracks
        fields = '__all__'