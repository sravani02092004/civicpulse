from accounts.models import NGOProfile

# Keyword map to detect category from title and description
CATEGORY_KEYWORDS = {
    'ROADS': ['road', 'pothole', 'street', 'asphalt', 'traffic', 'bridge', 'pavement', 'tar'],
    'SANITATION': ['garbage', 'waste', 'trash', 'clean', 'dump', 'drain', 'sewer', 'overflow', 'smell'],
    'WATER': ['water', 'pipe', 'leak', 'supply', 'tap', 'contamination', 'drinking'],
    'ELECTRICITY': ['light', 'power', 'wire', 'electricity', 'outage', 'pole', 'transformer', 'dark'],
}

def categorize_and_assign_issue(issue):
    """
    Analyzes the issue title and description to detect a category,
    then automatically assigns the issue to a matching NGO.
    """
    text_content = f"{issue.title} {issue.description}".lower()
    detected_category = 'OTHER'

    # Check text against keywords
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text_content for keyword in keywords):
            detected_category = category
            break

    issue.detected_category = detected_category

    # Attempt to assign an NGO based on matching focus area
    matching_ngo = NGOProfile.objects.filter(category_focus__icontains=detected_category).first()

    # Fallback to the first available NGO if no direct match is found
    if not matching_ngo:
        matching_ngo = NGOProfile.objects.first()

    if matching_ngo:
        issue.assigned_ngo = matching_ngo

    issue.save()
    return issue