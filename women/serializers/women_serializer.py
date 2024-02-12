from rest_framework import serializers
from women.models.women import Women
from rest_framework.renderers import JSONRenderer



class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('__all__')



# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance
    


def encode():
    model = Women('Angelina','Aktrica')
    ser_model = WomenSerializer(model)
    print(ser_model.data)
    json = JSONRenderer().render(ser_model.data)
