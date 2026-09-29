from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from accounts.models import NGOProfile

class Issue(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Detection'),
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='issue_images/')
    location = models.CharField(max_length=150)
    
    # Auto-detected or assigned category
    detected_category = models.CharField(max_length=100, blank=True, null=True)
    detection_confidence = models.FloatField(default=0.0)
    
    # AI generated summary
    ai_summary = models.TextField(blank=True, null=True)
    
    # Workflow
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_issues')
    assigned_ngo = models.ForeignKey(NGOProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues')
    
    resolution_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"