from django.forms import ModelForm
from .models import Crypto


class CryptoForm(ModelForm):
    class Meta:
        model = Crypto
        fields = "__all__"
        