# Email-Signature-Extraction-with-LLMs

# Email Signature Extractor & Evaluator

This project is designed to evaluate the performance of different Large Language Models (LLMs) in extracting email signature information and structuring it into a JSON format.

## Project Structure

- `config.py`: Contains the OpenAI API key.
- `functions.py`: Defines the functions used for prompt evaluation and result analysis.
- `main.py`: The main script that runs the evaluation.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/email_signature_extractor_evaluator.git
    cd email_signature_extractor_evaluator
    ```

2. Set up a Python virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install openai transformers
    ```

4. Set your OpenAI API key in `config.py`:
    ```python
    # config.py
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

## Usage

Run the main script to evaluate the prompt against the test cases:
```bash
python main.py


Contact

For any questions or issues, please contact [brandon14ogola@gmail.com].