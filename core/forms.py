from django import forms

from core.models import Rhempleado

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
