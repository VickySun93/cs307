from django.contrib import admin
from inbox.models import Message

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
