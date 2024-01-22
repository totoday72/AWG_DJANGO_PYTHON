from django.urls import path

from core.views import AgenciaView, EmpleadosView, EmpleadosNew

urlpatterns = [path('core', AgenciaView.as_view(), name='agencia_list'),
               path('empleado', EmpleadosView.as_view(), name='empleado_list'), path('empleado/new', EmpleadosNew.as_view(), name='empleado_new'),]
