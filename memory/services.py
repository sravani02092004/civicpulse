# import os

# from dotenv import load_dotenv
# from hindsight_client import Hindsight

# load_dotenv()

# HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

# client = Hindsight(
# base_url="https://api.hindsight.vectorize.io",
# api_key=HINDSIGHT_API_KEY
# )

# BANK_ID = "civicpulse"
# def retain_issue_resolution(issue):
#     content = f"""
# CivicPulse civic issue resolution record.

# Issue ID: {issue.id}
# Title: {issue.title}
# Description: {issue.description}
# Location: {issue.location}
# Detected Category: {issue.detected_category}
# Status: {issue.status}
# Resolution Details: {issue.resolution_details}
# Reported At: {issue.created_at}
# Resolved/Updated At: {issue.updated_at}
# """

#     return client.retain(
#         bank_id=BANK_ID,
#         content=content
#     )
# def recall_similar_issues(query):
#     return client.recall(
#         bank_id=BANK_ID,
#         query=query
#     )
# def get_similar_issue_memories(issue):
#     query = f"""
#     Find previous civic issues similar to this issue.

#     Category: {issue.detected_category}
#     Location: {issue.location}
#     Title: {issue.title}
#     Description: {issue.description}

#     Focus on previous issues, actions taken, and successful resolutions.
#     """

#     return recall_similar_issues(query)
# def reflect_on_issue(issue):
#     query = f"""
#     Analyze the past experience related to this civic issue.

#     Current issue:
#     Category: {issue.detected_category}
#     Location: {issue.location}
#     Title: {issue.title}
#     Description: {issue.description}

#     Based on previous stored civic issue experiences:

#     1. Identify relevant patterns.
#     2. Summarize what happened in similar cases.
#     3. Suggest practical actions for the NGO.
#     4. Mention uncertainty if the stored memories are insufficient.

#     IMPORTANT:
#     - Write the response as clean plain text.
#     - Do not use Markdown symbols such as #, *, **, backslashes, or bullet symbols.
#     - Do not claim that CivicPulse generally resolves issues within minutes.
#     - If a stored record was resolved quickly, describe it only as a historical example.
#     - Clearly distinguish stored facts from suggestions or inferences.
#     - Keep the recommendation concise and practical.
#     """

#     return client.reflect(
#         bank_id=BANK_ID,
#         query=query
#     )
import os
import asyncio

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

BANK_ID = "civicpulse"


def retain_issue_resolution(issue):
    content = f"""
CivicPulse civic issue resolution record.

Issue ID: {issue.id}
Title: {issue.title}
Description: {issue.description}
Location: {issue.location}
Detected Category: {issue.detected_category}
Status: {issue.status}
Resolution Details: {issue.resolution_details}
Reported At: {issue.created_at}
Resolved/Updated At: {issue.updated_at}
"""

    return asyncio.run(
        client.aretain(
            bank_id=BANK_ID,
            content=content
        )
    )


def recall_similar_issues(query):
    result = asyncio.run(
        client.arecall(
            bank_id=BANK_ID,
            query=query
        )
    )

    print("\n========== HINDSIGHT RECALL RESULT ==========")
    print(result)
    print("=============================================\n")

    return result


def get_similar_issue_memories(issue):
    query = f"""
Find previous civic issues similar to this issue.

Category: {issue.detected_category}
Location: {issue.location}
Title: {issue.title}
Description: {issue.description}

Focus on previous issues, actions taken, and successful resolutions.
"""

    return recall_similar_issues(query)


def reflect_on_issue(issue):
    query = f"""
Analyze the past experience related to this civic issue.

Current issue:
Category: {issue.detected_category}
Location: {issue.location}
Title: {issue.title}
Description: {issue.description}

Based on previous stored civic issue experiences:

1. Identify relevant patterns.
2. Summarize what happened in similar cases.
3. Suggest practical actions for the NGO.
4. Mention uncertainty if the stored memories are insufficient.

IMPORTANT:
- Write the response as clean plain text.
- Do not use Markdown symbols such as #, *, **, backslashes, or bullet symbols.
- Do not claim that CivicPulse generally resolves issues within minutes.
- If a stored record was resolved quickly, describe it only as a historical example.
- Clearly distinguish stored facts from suggestions or inferences.
- Keep the recommendation concise and practical.
"""

    return asyncio.run(
        client.areflect(
            bank_id=BANK_ID,
            query=query
        )
    )

