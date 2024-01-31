from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Rhagencia, Rhempleado, Rhmotiv
from core.forms import Empleadoform, Rhmotiv_Form
from generales.views import SinPrivilegios


# Create your views here.
class AgenciaView(LoginRequiredMixin, generic.ListView):
    model = Rhagencia
    template_name = 'core/agencia_list.html'
    context_object_name = "obj"
    login_url = 'generales:login'


class EmpleadosView(LoginRequiredMixin, generic.ListView):
    model = Rhempleado
    template_name = 'core/empleado_list.html'
    context_object_name = "obj"
    login_url = 'generales:login'


class EmpleadosNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.CreateView):
    permission_required = "core.add_rhempleado"
    model = Rhempleado
    template_name = "core/empleado_form.html"
    context_object_name = 'obj'
    form_class = Empleadoform
    success_url = reverse_lazy("core:empleado_list")
    success_message = "Empleado Creado Satisfactoriamente"


class EmpleadosEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "core.add_rhempleado"
    model = Rhempleado
    template_name = 'core/empleado_form.html'
    context_object_name = 'obj'
    form_class = Empleadoform
    success_url = reverse_lazy("core:empleado_list")
    success_message = "Empleado Actualizado Satisfactoriamente"


# ****************** MANTENIMIENTO DE MOTIVOS *********************
class Motivosview(LoginRequiredMixin, generic.ListView):
    model = Rhmotiv
    template_name = 'core/rhmotiv_list.html'
    context_object_name = "obj"
    login_url = 'generales:login'


class MotivoNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.CreateView):
    permission_required = "core.add_rhmotiv"
    model = Rhmotiv
    template_name = "core/rhmotiv_form.html"
    context_object_name = 'obj'
    form_class = Rhmotiv_Form
    success_url = reverse_lazy("core:rhmotiv_list")
    success_message = "Motivo Creado Satisfactoriamente"


class MotivoEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "core.add_rhmotiv"
    model = Rhmotiv
    template_name = 'core/rhmotiv_form.html'
    context_object_name = 'obj'
    form_class = Rhmotiv_Form
    success_url = reverse_lazy("core:rhmotiv_list")
    success_message = "Motivo Actualizado Satisfactoriamente"
