from django.forms import ModelForm
from .models import Wishes

class WishesForm(ModelForm):
    class Meta:
        model = Wishes
        fields = ['description', 'quantity']
    