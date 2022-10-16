from django import forms
# import GeeksModel from models.py
from .models import GeeksModel

# creating a django form
class GeeksForm(forms.Form):
    # name = forms.CharField()
    # geeks_field = forms.ImageField()
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    date = forms.DateField(widget = forms.SelectDateWidget)
    
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]