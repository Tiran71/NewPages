from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields=['title', 'text', 'date']

        widgets = {
            'title': widgets.TextInput(attrs={'placeholder':'глава'}),
            'text' : widgets.Textarea(attrs={'placeholder':'текст'}),
            'date': widgets.DateInput(attrs={'placeholder':'дата'})
        }