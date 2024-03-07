from django import forms

class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=1000)
    bajada = forms.CharField(widget=forms.Textarea)


class TextoForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea)
    lugar = forms.IntegerField()


class ImagenForm(forms.Form):
    titulo = forms.CharField(max_length=1000)
    archivo = forms.ImageField()
    lugar = forms.IntegerField()
    