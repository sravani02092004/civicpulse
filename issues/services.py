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
    Detect the issue category and automatically assign it
    to an NGO matching both category and location.
    """

    text_content = f"{issue.title} {issue.description}".lower()
    detected_category = 'OTHER'

    # Detect category from title and description
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword.lower() in text_content for keyword in keywords):
            detected_category = category
            break

    issue.detected_category = detected_category

    # Match NGO by both category and operating location
    matching_ngo = NGOProfile.objects.filter(
        category_focus__icontains=detected_category,
        operating_location__icontains=issue.location
    ).first()

    # If no exact category + location match,
    # try category-only match
    if not matching_ngo:
        matching_ngo = NGOProfile.objects.filter(
            category_focus__icontains=detected_category
        ).first()

    # If still no match, use the first available NGO
    if not matching_ngo:
        matching_ngo = NGOProfile.objects.first()

    if matching_ngo:
        issue.assigned_ngo = matching_ngo

    issue.save()

    return issue