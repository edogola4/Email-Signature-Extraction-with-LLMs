# main.py
from functions import evaluate_prompt, analyze_results, document_results

# Define initial prompt
initial_prompt = """
Extract the email signature from the following email and structure it into a JSON format with the following fields: Name, Title, Company, Email, Phone. If a field is not present, return an empty string for that field.

Email:
"{email_content}"

JSON format:
{{
  "Name": "",
  "Title": "",
  "Company": "",
  "Email": "",
  "Phone": ""
}}
"""

# Define test cases
test_cases = [
    # Test case 1
    """
    Hi John,
    Thanks for reaching out. I would be happy to schedule a meeting with you next week.
    Best regards,
    Jane Doe
    Senior Developer
    Tech Corp
    jane.doe@techcorp.com
    (555) 123-4567
    """,
    # Test case 2
    """
    Hello Team,
    Please find the attached report for your review.
    Regards,
    Mike
    mike@example.com
    """,
    # Test case 3
    """
    Hi everyone,
    Looking forward to our meeting tomorrow.
    Best,
    Chris
    """,
    # Test case 4
    """
    Hi Sarah,
    Sure, let's discuss this in our meeting.
    Thanks,
    Alex
    On Mon, Jul 10, 2024 at 3:30 PM Sarah wrote:
    > Hi Alex,
    > Can we discuss the project updates tomorrow?
    > Best,
    > Sarah Johnson
    > Project Manager
    > Innovate Inc.
    > sarah.johnson@innovateinc.com
    > (555) 987-6543
    """
]

# Evaluate initial prompt
results = evaluate_prompt(test_cases, initial_prompt, "gpt2")  # or another Hugging Face model

# Analyze results
analyze_results(results)

# Document initial results
document_results(results, initial_prompt)

# Here you can add logic for prompt iteration based on analysis
# For now, we'll assume no changes were made

# Re-evaluate and document updated results if necessary
# updated_prompt = "your_updated_prompt_here"
# updated_results = evaluate_prompt(test_cases, updated_prompt)
# document_results(updated_results, initial_prompt, updated_prompt)
