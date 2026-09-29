from django import forms
from .models import Issue

class IssueReportForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'location', 'image']