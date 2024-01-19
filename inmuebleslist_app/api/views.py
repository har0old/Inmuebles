from rest_framework.response import Response
from rest_framework import status
from inmuebleslist_app.models import  Inmueble, Empresa, Comentario
from inmuebleslist_app.api.serializers import  InmuebleSerializer, EmpresaSerializer, ComentarioSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins 

class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    
    def perfom_create(self, serializer):
        pk = self.kwargs['pk']
        inmueble = Inmueble.objects.get(pk=pk)
        serializer.save(inmueble=inmueble)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class ComentarioList(generics.ListCreateAPIView):
    #queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(inmueble=pk).order_by('pk')
    
    
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

#metodo para generer visatas genericas 
"""
OTRA FORMA DE HACERLO LO DE ARRIBA
class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    
class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
       queryset = Comentario.objects.all()
       serializer_class = ComentarioSerializer
       
       def get(self, request, *args, **kwargs):
           return self.retrieve(request, *args, **kwargs)
"""       
    
class InmuebleListAV(APIView):
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    def post(self, request):
        de_serializer = InmuebleSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class InmuebleDetalleAV(APIView):
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            serializer = InmuebleSerializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk): 
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            de_serializer = InmuebleSerializer(inmueble, data=request.data)
            if de_serializer.is_valid():
                de_serializer.save()
                return Response(de_serializer.data)
            else:
                return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            inmueble.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)



class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context={'request':request})
        return Response(serializer.data)
    def post(self, request):
        de_serializer = EmpresaSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
            serializer = EmpresaSerializer(empresa, context={'request':request})
            return Response(serializer.data)
        except Empresa.DoesNotExist:
            return Response({'Error':'La Empresa no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
            de_serializer = EmpresaSerializer(empresa, data=request.data, context={'request':request})
            if de_serializer.is_valid():
                de_serializer.save()
                return Response(de_serializer.data)
            else:
                return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Empresa.DoesNotExist:
            return Response({'Error':'La Empresa no existe'}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
            empresa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Empresa.DoesNotExist:
            return Response({'Error':'La Empresa no existe'}, status=status.HTTP_404_NOT_FOUND)













"""
OTRA FORMA DE REALIZARLO 

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
       
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        de_serializer = InmuebleSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    if request.method == 'GET':
        try:  
            inmueble = Inmueble.objects.get(pk=pk)
            serializer = InmuebleSerializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=pk)
        de_serializer = InmuebleSerializer(inmueble, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
    if request.method == 'DELETE':
        try:  
            inmueble = Inmueble.objects.get(pk=pk)
            inmueble.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
            
            
             """