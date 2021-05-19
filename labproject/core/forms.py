from django import forms
from django.forms import ModelForm

from .models import *

PAYMENT_CHOICES = (
    ('S', 'Cash On Delivery'),
    ('P', 'Bkash')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)
    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class PaymentFormcod(forms.Form):
    save = forms.BooleanField(required=False)


class PaymentFormbkash(ModelForm):
    class Meta:
        model = Paymentfrombkash
        exclude = ('user','order',)
        help_texts = {
            "my_field": "This is case sensitive..."
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

