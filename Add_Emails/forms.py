from django import forms
from django.db.models import fields
from django.db.models.query import QuerySet
from .models import Upload_Emails
from django.contrib.auth.models import User

queryset = set()
class AddEmailForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AddEmailForm, self).__init__(*args, **kwargs)
    #     # access object through self.instance...
    #     queryset = Upload_Emails.objects.filter(company=self.instance.User)

    class Meta:
        model = Upload_Emails
        fields = [
            'title', 
            'email', 
            'remarks',
            'owner'
        ]

# class RawAddEmailForm(forms.Form):
#     title   = forms.CharField()
#     email   = forms.FileField()
#     remarks = forms.CharField()
#     # owner   = forms.ModelChoiceField()
#     # owner   = forms.ModelChoiceField(queryset=Upload_Emails.objects.filter(owner = User))
#     # form.rate.queryset = Rate.objects.filter(company_id=the_company.id)
