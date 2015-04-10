from django.forms import ModelForm, Textarea, HiddenInput
from inbox.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content', 'sender']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
            'sender': HiddenInput()
        }
