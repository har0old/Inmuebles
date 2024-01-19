from rest_framework import serializers
from inmuebleslist_app.models import Inmueble, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        #exclude = ['inmueble']
        fields = '__all__'

class InmuebleSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only =True)
    class Meta:
        model = Inmueble
        fields = '__all__'
        #fields =['id', 'direccion', 'pais','descripcion', 'imagen']
        #exclude = ['id']
    def to_representation(self, instance):
        # Obtén la representación original del objeto serializado
        data = super(InmuebleSerializer, self).to_representation(instance)

        # Mueve el campo "comentarios" al final del objeto JSON
        comentarios = data.pop('comentarios')
        data['comentarios'] = comentarios

        return data
class EmpresaSerializer(serializers.ModelSerializer): #identificador ID
#class EmpresaSerializer(serializers.HyperlinkedModelSerializer):# identificador seria la url 
    InmuebleList = InmuebleSerializer(many=True, read_only = True) #devuele todo los campos de inmuebles
    #InmuebleList = serializers.StringRelatedField(many=True) # devuelve el str de models Inmuebles
    #InmuebleList = serializers.PrimaryKeyRelatedField(many=True, read_only = True) # devuelve los ID
    """
    InmuebleList = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only = True,
        view_name='inmueble-detail'
        )
    """ #devuelve los enponint 
    
    class Meta:
        model = Empresa
        fields = '__all__'

    def to_representation(self, instance):
        # Obtén la representación original del objeto serializado
        data = super(EmpresaSerializer, self).to_representation(instance)

        # Mueve el campo "comentarios" al final del objeto JSON
        InmuebleList = data.pop('InmuebleList')
        data['InmuebleList'] = InmuebleList

        return data


        
    # METODOS DE VALIDACION
        
    # def get_longitud_direccion(self, obj): 
    #     direccion = obj.direccion
    #     longitud = len(direccion)
    #     return longitud
    
    # #validacion de la data funcion (validate) preexistente dentro de django
    # def validate(self, data):
    #     if data['direccion'] ==data['pais']:
    #         raise serializers.ValidationError("La direccion y el pais deben ser diferenres")
    #     else:
    #         return data

        
    # def validate_imagen(self, data):
    #     if len(data) < 9:
    #         raise serializers.ValidationError("La Url de la imagen es muy corta")
    #     else:
    #         return data
        




#Validation
# def column_longitud(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("El valor es demasiado corto")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud], required=True)
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField(validators=[column_longitud])
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
#     fecha = serializers.DateTimeField(read_only=True)
    
    
#     def create(self, validate_data):
#         return Inmueble.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.direccion = validate_data.get('direccion', instance.direccion)
#         instance.pais = validate_data.get('pais', instance.pais)
#         instance.descripcion = validate_data.get('descripcion', instance.descripcion)
#         instance.imagen = validate_data.get('imagen', instance.imagen)
#         instance.active = validate_data.get('active', instance.active)
#         instance.fecha = validate_data.get('fecha', instance.fecha)
#         instance.save()
#         return instance
    
#     #validacion de la data funcion (validate) preexistente dentro de django
#     def validate(self, data):
#         if data['direccion'] ==data['pais']:
#             raise serializers.ValidationError("La direccion y el pais deben ser diferenres")
#         else:
#             return data

        
#     def validate_imagen(self, data):
#         if len(data) < 9:
#             raise serializers.ValidationError("La Url de la imagen es muy corta")
#         else:
#             return data
