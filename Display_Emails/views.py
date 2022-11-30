from django.shortcuts import render

# Create your views here.
def show_emails_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, "show_emails.html", {})