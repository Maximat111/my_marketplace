from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category', 'image', 'phone_number', 'email']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
