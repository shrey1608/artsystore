from django import forms


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('c','CashOnDelivery')
)



class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'st paris'
    }))
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Apartment or suite'
    }))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    state = forms.CharField()
    country= forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)