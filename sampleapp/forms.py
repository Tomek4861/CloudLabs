from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Input your name", 'class': "form-control mb-3"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Input your email", 'class': "form-control mb-3"}),
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Input your message", 'class': "form-control mb-3", 'rows': 4}),
    )
