from django.forms import ModelForm
from .models import *


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class EditNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content")
