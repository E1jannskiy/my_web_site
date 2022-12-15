from django.forms import ModelForm, TextInput, Textarea
from .models import Fruits


class FruitForm(ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'description', 'img']

        widgets = {
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'form-control'
            }),
            'description' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter text'
        })
    }