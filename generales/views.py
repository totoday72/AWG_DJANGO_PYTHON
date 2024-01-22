from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
class SinPrivilegios(PermissionRequiredMixin):
    login_url='generales:sin_privilegios'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('pagina inicio')
    
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name='generales/home.html'
    login_url='generales:login'

class HomeSinPrivilegios(generic.TemplateView):
    template_name="generales/sin_privilegios.html"