from django import forms


def validate_no_spam(value):
    if 'spam' in value.lower():
        raise forms.ValidationError('Message contains prohibited word: spam')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=2, label='Your name')
    email = forms.EmailField(label='Email address')
    message = forms.CharField(widget=forms.Textarea, min_length=10, validators=[validate_no_spam])
