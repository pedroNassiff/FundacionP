from .models import Publicacion
from django import forms


class publicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['titulo', 'texto']

class contactoForm(forms.Form):
    tema = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)