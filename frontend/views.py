from django.shortcuts import render, redirect
from django.contrib import messages

from account.forms import ComplaintForm

def home_view(request):
    return render(request, 'frontend/index.html')

def about_view(request):
    return render(request, 'frontend/about.html')

def services_view(request):
    return render(request, 'frontend/services.html')

def contact_view(request):
    return render(request, 'frontend/contact.html')

def file_complaint_view(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your complaint has been submitted successfully. We will get back to you as oon as possible.")
            return redirect("frontend:file_complaint")
        else:
            messages.error(request, "Please correct the errors below and resubmit the form.")
    else:
        form = ComplaintForm()

    return render(request, 'frontend/file_complaint.html', {"form": form})


