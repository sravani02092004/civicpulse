


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from issues.models import Issue
from memory.services import (
    get_similar_issue_memories,
    reflect_on_issue
)
def landing_page(request):
    return render(request, 'dashboard/landing.html')

@login_required
def dashboard_home(request):

    user_role = (
        getattr(request.user.profile, 'role', 'CITIZEN')
        if hasattr(request.user, 'profile')
        else 'ADMIN'
    )

    return render(
        request,
        'dashboard/home.html',
        {'role': user_role}
    )


@login_required
def ngo_dashboard(request):

    # Only NGO users can access this page
    if not hasattr(request.user, 'ngo_profile'):
        messages.error(
            request,
            "Access restricted to NGO accounts."
        )
        return redirect('dashboard_home')

    ngo_profile = request.user.ngo_profile

    # Get issues assigned to this NGO
    assigned_issues = Issue.objects.filter(
        assigned_ngo=ngo_profile
    ).order_by('-created_at')

    # Hindsight RECALL
    for issue in assigned_issues:
        try:
            issue.similar_memories = get_similar_issue_memories(issue)
        except Exception:
            issue.similar_memories = None

    # Hindsight REFLECT
    for issue in assigned_issues:
        try:
            issue.reflection = reflect_on_issue(issue)
        except Exception:
            issue.reflection = None

    return render(
        request,
        'dashboard/ngo_dashboard.html',
        {
            'ngo': ngo_profile,
            'assigned_issues': assigned_issues,
        }
    )