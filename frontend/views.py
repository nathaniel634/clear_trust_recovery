from django.shortcuts import render, redirect
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
            return redirect("frontend:complaint_success")
    else:
        form = ComplaintForm()
    return render(request, 'frontend/file_complaint.html', {"form": form})

