from django import forms
from api.models import Vendas


class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = '__all__'