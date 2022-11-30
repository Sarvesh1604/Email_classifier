from Add_Emails.forms import AddEmailForm
from django.shortcuts import render
from Add_Emails.models import Upload_Emails

# Create your views here.

def add_emails_view(request, *args, **kwargs):
    my_form = AddEmailForm()
    if request.method == "POST":
        my_form = AddEmailForm(request.POST, request.FILES)
        if my_form.is_valid():
            Upload_Emails.objects.create(**my_form.cleaned_data)
    context = {
        "form": my_form
    }
    return render(request, "add_emails.html", context)