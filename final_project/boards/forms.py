from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'placeholder': 'Enter Your Message'}),
                              max_length=4000,
                              help_text="The max Length Of The Text 4000")
    class Meta:
        model = Topic
        fields = ['subject', 'message']