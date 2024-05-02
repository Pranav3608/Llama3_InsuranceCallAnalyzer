from .model import llama3_generate
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# nltk setup
nltk.download('punkt')
nltk.download('stopwords')

def verify_schema(text, schema):
    stop_words = set(stopwords.words('english'))
    text_tokens = word_tokenize(text.lower())
    text_tokens_filtered = [word for word in text_tokens if word not in stop_words]

    chunk_size = 1000  
    text_chunks = [' '.join(text_tokens_filtered[i:i + chunk_size]) for i in range(0, len(text_tokens_filtered), chunk_size)]
    text_input = ' '.join(text_chunks)

    results = []
    for key, description in schema.items():
        schema_tokens = word_tokenize(description.lower())
        schema_tokens_filtered = [word for word in schema_tokens if word not in stop_words]
        schema_input = ' '.join(schema_tokens_filtered)
        prompt = f"Check if the text: {text_input}, matches the schema point or not. Just reply matched or unmatched: {schema_input}"  # Prompt to interacct with the Llama-3 model for compliance or schema verification
        response = llama3_generate(prompt)
        status = "Verified" if "matched" in response.lower() else "Unverified"
        score = 1 if status == "Verified" else 0
        results.append([key, status, score])

    return results

def extract_metadata_from_transcript(transcript):
    # Prompts to extract entities from the Insurance Call transcript
    prompts = {
        "DATE": "What is the date of the call in the transcript? Answer in just one word",
        "CALL_ID": "What is the call ID in the transcript? Answer in just one word",
        "TIME": "What is the time of the call in the transcript? Answer in just one word",
        "AGENT_ID": "What is the ID of the Life Insurance Agent in the transcript? Answer in just one word",
        "LIFE_INSURANCE_AGENT_NAME": "What is the name of Life Insurance Agent in the transcript? Answer in just one word",
        "PROSPECTIVE_CLIENT_NAME": "What is the name of Client in the transcript? Answer in just one word",
    }

    extracted_data = {}
    for metadata, prompt in prompts.items():
        full_prompt = f"Extract the {metadata} from the following text: {transcript}"
        response = llama3_generate(full_prompt)
        # Extract the last part after "is" which is expected to be the answer
        extracted_value = response.split(":")[-1].strip()
        extracted_data[metadata] = extracted_value

    return extracted_data

def process_transcript(transcript, schema):
    schema_results = verify_schema(transcript, schema)
    metadata_results = extract_metadata_from_transcript(transcript)

    # DataFrame for displaying results
    df_schema = pd.DataFrame(schema_results, columns=['Schema point', 'Verification status', 'Verification score'])
    df_metadata = pd.DataFrame(list(metadata_results.items()), columns=['Metadata', 'Value'])

    return df_schema, df_metadata

