from django import forms


class AddTwitterUser(forms.Form):
    username = forms.CharField(
        max_length=150
        )
    password = forms.CharField(
        widget=forms.PasswordInput()
        )
    display_name = forms.CharField(
        max_length=150
        )
    first_name = forms.CharField(
        max_length=30
        )
    last_name = forms.CharField(
        max_length=150
        )
    homepage = forms.URLField(
        required=False
        )
    age = forms.IntegerField(
        widget=forms.NumberInput()
        )
    email = forms.EmailField()
