from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Complaint

def login_view(request):
    if request.user.is_authenticated:
        return redirect('account:admin_dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('account:admin_dashboard')
        else:
            messages.error(request, "Invalid username or password. Please check the details and try again")

    return render(request, 'frontend/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('account:login')

@login_required()
def admin_dashboard(request):

    reports = Complaint.objects.all().order_by('-created_at')

    report_count = reports.count()
    pending_count = reports.filter(status=Complaint.STATUS_PENDING).count()
    reviewed_count = reports.filter(status=Complaint.STATUS_REVIEWED).count()

    context = {
        'reports': reports,
        'report_count': report_count,
        'pending_count': pending_count,
        'reviewed_count': reviewed_count,
    }

    return render(request, 'account/dashboard.html', context)


@login_required()
def report_detail(request, pk):
    report = get_object_or_404(Complaint, pk=pk)
    return render(request, 'account/report_detail.html', {'report': report})


@login_required()
@require_POST
def mark_as_reviewed(request, pk):
    report = get_object_or_404(Complaint, pk=pk)

    if report.status != report.STATUS_REVIEWED:
        report.status = report.STATUS_REVIEWED
        report.save()
        messages.success(request, "Report marked as reviewed successfully.")
    else:
        messages.info(request, "This report is already reviewed.")
    return redirect('account:report_detail', pk=pk)
