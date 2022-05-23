from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
    apellidos = forms.CharField(label='apellidos',max_length=200, required=True)
    email = forms.EmailField(label='nombre',max_length=200, required=True)
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
    nombre = forms.CharField(label='nombre',max_length=200, required=True)
