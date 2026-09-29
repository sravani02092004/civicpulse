from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Issue
from memory.services import (
    retain_issue_resolution,
    get_similar_issue_memories,
    reflect_on_issue
)
from .forms import IssueReportForm
from .services import categorize_and_assign_issue


@login_required
def report_issue(request):

    if request.method == 'POST':
        form = IssueReportForm(request.POST, request.FILES)

        if form.is_valid():
            issue = form.save(commit=False)

            issue.reported_by = request.user
            issue.status = 'OPEN'

            issue.save()

            # Phase 5: Auto-categorize and assign NGO
            categorize_and_assign_issue(issue)

            messages.success(
                request,
                "Issue reported successfully!"
            )

            return redirect('my_issues')

    else:
        form = IssueReportForm()

    return render(
        request,
        'issues/report_issue.html',
        {'form': form}
    )


@login_required
def my_issues(request):

    issues = Issue.objects.filter(
        reported_by=request.user
    ).order_by('-created_at')

    return render(
        request,
        'issues/my_issues.html',
        {'issues': issues}
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

    assigned_issues = Issue.objects.filter(
        assigned_ngo=ngo_profile
    ).order_by('-created_at')
    for issue in assigned_issues:
       try:
          issue.similar_memories = get_similar_issue_memories(issue)
       except Exception:
           issue.similar_memories = None
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


@login_required
def update_issue_status(request, issue_id):

    # Only NGO users can update issues
    if not hasattr(request.user, 'ngo_profile'):
        messages.error(
            request,
            "Access restricted to NGO accounts."
        )
        return redirect('dashboard_home')

    ngo_profile = request.user.ngo_profile

    issue = get_object_or_404(
        Issue,
        id=issue_id,
        assigned_ngo=ngo_profile
    )

    # Show resolution form
    if request.method == 'GET':
        return render(
            request,
            'dashboard/resolve_issue.html',
            {'issue': issue}
        )

    # Process submitted resolution
    if request.method == 'POST':

        new_status = request.POST.get('status', 'RESOLVED')

        resolution_details = request.POST.get(
            'resolution_details',
            ''
        )

        issue.status = new_status
        issue.resolution_details = resolution_details
        issue.save()

# Store the resolved issue in Hindsight memory
        if new_status == 'RESOLVED':
           retain_issue_resolution(issue)

        messages.success(
          request,
          f"Issue #{issue.id} marked as {new_status}."
)

        return redirect('ngo_dashboard')

    return redirect('ngo_dashboard')
def public_feed(request):
    issues = Issue.objects.all().order_by('-created_at')

    # Get search and filter params from GET query parameters
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    status = request.GET.get('status', '').strip()

    # Apply keyword filter across title, description, and location
    if query:
        issues = issues.filter(
            title__icontains=query
        ) | issues.filter(
            description__icontains=query
        ) | issues.filter(
            location__icontains=query
        )

    # Apply category filter
    if category:
        issues = issues.filter(detected_category=category)

    # Apply status filter
    if status:
        issues = issues.filter(status=status)

    return render(
        request,
        'issues/public_feed.html',
        {
            'issues': issues,
            'query': query,
            'category': category,
            'status': status,
        }
    )