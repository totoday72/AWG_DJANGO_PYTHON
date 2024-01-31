from django.urls import path

from core.views import AgenciaView, EmpleadosView, EmpleadosNew, EmpleadosEdit, MotivoNew, Motivosview, MotivoEdit, MotivoDel

urlpatterns = [path('core', AgenciaView.as_view(), name='agencia_list'),

               path('empleado', EmpleadosView.as_view(), name='empleado_list'),
               path('empleado/new', EmpleadosNew.as_view(), name='empleado_new'),
               path('empleado/edit/<int:pk>', EmpleadosEdit.as_view(), name='empleado_edit'),

               # ****************** MANTENIMIENTO DE MOTIVOS *********************
               path('motivo', Motivosview.as_view(), name='rhmotiv_list'),
               path('motivo/new', MotivoNew.as_view(), name='rhmotiv_new'),
               path('motivo/edit/<int:pk>', MotivoEdit.as_view(), name='rhmotiv_edit'),
               path('motivo/delete/<int:pk>', MotivoDel.as_view(), name='rhmotiv_del'),

               ]
