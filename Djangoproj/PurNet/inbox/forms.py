from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from inbox.models import Message

def InvalidUsernameValidator(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError('Enter a valid username.')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].validators.append(InvalidUsernameValidator)

    def clean(self):
        super(MessageForm, self).clean()
        subject = self.cleaned_data.get('subject')
        content = self.cleaned_data.get('content')
        recipient = self.cleaned_data.get('recipient')
        return self.cleaned_data