# functions.py
import openai
from transformers import pipeline
from config import OPENAI_API_KEY

# Set API key
openai.api_key = OPENAI_API_KEY

def call_openai(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def call_huggingface(model_name, prompt):
    generator = pipeline('text-generation', model=model_name)
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text'].strip()

def evaluate_prompt(test_cases, initial_prompt, model_name):
    results = []
    for email in test_cases:
        prompt = initial_prompt.format(email_content=email)
        openai_result = call_openai(prompt)
        hf_result = call_huggingface(model_name, prompt)
        results.append({
            "email": email,
            "openai_result": openai_result,
            "hf_result": hf_result
        })
    return results

def analyze_results(results):
    for result in results:
        print("Email:\n", result['email'])
        print("OpenAI Result:\n", result['openai_result'])
        print("Hugging Face Result:\n", result['hf_result'])
        print("\n")

def document_results(results, initial_prompt, updated_prompt=None):
    with open('results.txt', 'w') as f:
        f.write("Initial Prompt:\n")
        f.write(initial_prompt + "\n\n")
        if updated_prompt:
            f.write("Updated Prompt:\n")
            f.write(updated_prompt + "\n\n")
        for result in results:
            f.write("Email:\n")
            f.write(result['email'] + "\n")
            f.write("OpenAI Result:\n")
            f.write(result['openai_result'] + "\n")
            f.write("Hugging Face Result:\n")
            f.write(result['hf_result'] + "\n")
            f.write("\n")
