from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
               'class': 'form-control custom-input',
                'placeholder': 'Eliud Thuku Johnson',  
            }),
            'age': forms.TextInput(attrs={
               'class': 'form-control custom-input',
                'placeholder': '2 Years 5 Month',  
            }),
            'title': forms.TextInput(attrs={
               'class': 'form-control custom-input',
                'placeholder': 'which occasion are you celebrating with your kid? My Baby Boy Just Turned 2 Years Old',  
            }),
            'desc': forms.TextInput(attrs={
               'class': 'form-control custom-input',
                'placeholder': 'On This Day I Organised A Birthday Party For My Little Boy To Celebrate His Life Journey Together, We Visited Nairobi National Park',  
            }),
            'location': forms.TextInput(attrs={
               'class': 'form-control custom-input',
                'placeholder': 'Nairobi',  
            }),
            'display_image': forms.ClearableFileInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Select banner image',
            }),
        }