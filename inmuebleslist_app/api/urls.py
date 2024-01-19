from django.urls import path
#from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalleAV, EmpresaAV, EmpresaDetalleAV, ComentarioList, ComentarioDetail, ComentarioCreate

urlpatterns = [
    path('inmuebles/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('inmuebles/<int:pk>', InmuebleDetalleAV.as_view(), name='inmueble-detail'),
    
    path('empresas/', EmpresaAV.as_view(), name='empresa-list'),
    path('empresas/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),
    
    path('inmuebles/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('inmuebles/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('inmuebles/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail')
]

""" 
OTRA FORMA
urlpatterns = [
    path('list/', inmueble_list, name='inmueble-list'),
    path('<int:pk>', inmueble_detalle, name='inmueble-detalle')
]

"""

