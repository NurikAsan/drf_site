from django.shortcuts import render
from rest_framework import generics, viewsets
from women.models.women import *
from women.serializers.women_serializer import WomenSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenApiView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# class WomenApiView(APIView):
#     def get(self,request):
#         women = Women.objects.all()

#         return Response({'women':WomenSerializer(women, many=True).data})

#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'women':serializer.data})


#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({'errors':'Not Allowed'})
        
#         women = Women.objects.get(pk=pk)
#         serializer = WomenSerializer(data=request.data, instance=women)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'women':serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({'errors':'Not Allowed'})
        
#         women = Women.objects.get(pk=pk)
#         women.delete()
#         return Response({'women':'deleted'})


# @extend_schema_view(
#     list=extend_schema(
#             summary="Получить список женщин",
#         ),
# )
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    