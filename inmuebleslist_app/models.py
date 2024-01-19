from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "Nombre: "+str(self.nombre) +" - Web: "+str(self.website)

# Create your models here.
class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="InmuebleList") #entidad relacion y al eliminar una empres se eliminan sus inmuebles
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion + ' ' + self.descripcion + ' ' + self.pais 
    

class Comentario(models.Model):
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name="comentarios") #relacion con la entidad Inmueble 
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Calificacion: "+str(self.calificacion)+" texto: "+self.texto +" - Inmueble:  " + self.inmueble.direccion
    