# Data Transformation Pipeline

A Python project that uses AI to generate and execute data transformations on a pandas DataFrame. This pipeline combines pre-defined operations with an AI-powered command generator.

## Features
- **AI-driven transformations**: Uses a language model to convert natural language commands into structured data operations.
- **Pre-defined commands**: Supports filtering, selecting columns, and sorting.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the following command:
```bash
python main.py <model_name> <command> <path_to_csv> <api_token>
```
- `model_name`: Name of the Hugging Face model.
- `command`: Description of the transformation (e.g., "Filter rows where year > 2010 and select columns 'name'").
- `path_to_csv`: Path to the input CSV file.
- `api_token`: Your Hugging Face API token for accessing the model.

### Example
```bash
python main.py "mistralai/Mistral-7B-v0.3" "Filter rows where age > 25 and select column 'name'" "data/test.csv" "hf_your_api_token_here"
```