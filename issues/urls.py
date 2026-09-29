from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('my-issues/', views.my_issues, name='my_issues'),
    path('feed/', views.public_feed, name='public_feed'),
    path('ngo/', views.ngo_dashboard, name='ngo_dashboard'),
    path(
        'ngo/update/<int:issue_id>/',
        views.update_issue_status,
        name='update_issue_status'
    ),
]