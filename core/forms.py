from django import forms

from core.models import Rhempleado, Rhmotiv


class Empleadoform(forms.ModelForm):
    class Meta:
        model=Rhempleado
        fields=['agecod','nombres','apellidos']
        labels={
            'agecod':'Agencia',
            'nombres':'Nombres',
            'apellidos':'Apellidos'}
        widget={'nombres':forms.TextInput(), 'apellidos':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['agecod'].empty_label="Seleccione Agencia"


class Rhmotiv_Form(forms.ModelForm):
    class Meta:
        model = Rhmotiv
        fields = ['codmot', 'nommot']
        labels = {
            'codmot': 'Codigo de Motivo',
            'nommot': 'Descripcion de Motivo'}
        widget = {'Cod.': forms.TextInput(), 'Descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        # self.fields['agecod'].empty_label="Seleccione Agencia"
