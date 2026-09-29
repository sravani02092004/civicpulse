# CivicPulse

CivicPulse is a civic issue reporting and coordination platform that helps citizens report local problems, understand issues using AI, connect complaints with relevant NGOs, and use organizational memory to support future issue resolution.

## Problem

Civic complaints such as road damage, garbage problems, and water-related issues can be reported repeatedly without an effective way to learn from previous cases.

CivicPulse combines issue reporting, AI-based categorization, NGO coordination, and persistent organizational memory to make previous civic issue experiences useful for future cases.

## Key Features

* Citizen registration and login
* NGO registration and organization profiles
* Civic issue reporting with image upload
* AI-based issue categorization
* Public civic issue feed
* Search and filtering of reported issues
* NGO dashboard for assigned complaints
* Issue status management
* Resolution details
* Persistent organizational memory using Hindsight
* Recall of similar previous civic issues
* Reflection on previous experiences to support NGO decision-making

## How CivicPulse Works

1. A citizen reports a civic issue with a description, location, and image.
2. CivicPulse analyzes the issue and assigns an AI-detected category.
3. The issue can be assigned to a relevant NGO.
4. NGO representatives review assigned complaints.
5. When an issue is resolved, the resolution experience is stored as organizational memory.
6. For future similar issues, CivicPulse recalls relevant previous experiences.
7. Hindsight Reflection can analyze those experiences and provide practical context for the NGO.

## CivicRecall Agent

CivicPulse uses Hindsight as its persistent organizational memory layer.

The memory workflow follows three stages:

### RETAIN

When a civic issue is resolved, CivicPulse stores information such as:

* Issue ID
* Title
* Description
* Location
* Detected category
* Status
* Resolution details
* Report and update timestamps

This creates a persistent record of past civic issue experiences.

### RECALL

When an NGO views an assigned issue, CivicPulse can query Hindsight for similar previously stored experiences.

The recall process considers information such as:

* Issue category
* Location
* Title
* Description
* Previous actions
* Previous resolutions

This allows relevant historical experiences to be retrieved for the current issue.

### REFLECT

CivicPulse can use Hindsight Reflection to analyze relevant past experiences and provide:

* Relevant patterns
* A summary of similar cases
* Practical actions for the NGO
* Uncertainty when stored experiences are insufficient

The system is designed to distinguish stored historical information from suggestions or inferences.

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* SQLite

### Frontend

* HTML
* CSS
* JavaScript
* Django Templates

### AI and Memory

* YOLO-based image analysis for issue categorization
* Hindsight for persistent organizational memory
* RETAIN
* RECALL
* REFLECT

### Development Tools

* Git
* GitHub
* VS Code
* Postman

## Project Structure

```text
civicpulse/
├── accounts/
├── ai/
├── api/
├── civicpulse_project/
├── dashboard/
├── issues/
├── memory/
├── templates/
├── .gitignore
├── manage.py
└── README.md
```

## Example Memory Workflow

A previous civic issue can be stored after resolution:

```text
Issue:
Road damage in Gokavaram

Cause:
Heavy rains

Resolution:
The issue was reported to the local municipality.

Stored by:
CivicRecall Agent using Hindsight
```

Later, when another similar road issue is reported, CivicPulse can recall related historical experiences instead of treating the new complaint as completely isolated.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/sravani02092004/civicpulse.git
cd civicpulse
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install django djangorestframework pillow python-dotenv hindsight-client
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
HINDSIGHT_API_KEY=your_hindsight_api_key
```

Do not commit the `.env` file to GitHub.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Important Security Note

API keys and other secrets are stored in environment variables and should not be committed to the repository.

The `.gitignore` file excludes:

```text
.env
venv/
__pycache__/
*.pyc
db.sqlite3
issue_images/
media/
```

## Current Scope and Limitations

CivicPulse is an MVP demonstrating civic issue reporting, AI categorization, NGO coordination, and persistent organizational memory.

AI categorization and memory recommendations depend on the available model output and stored historical experiences. When sufficient historical information is not available, the system should treat recommendations as uncertain rather than presenting them as established facts.

## Hindsight

Hindsight provides the persistent memory layer used by CivicPulse.

Resources:

* Hindsight GitHub: https://github.com/vectorize-io/hindsight
* Hindsight Documentation: https://hindsight.vectorize.io/

## Project

CivicPulse — turning civic issue reports into actionable, reusable organizational knowledge.
