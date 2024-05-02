import boto3
import json

def llama3_generate(prompt):
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")
    model_id = "meta.llama3-70b-instruct-v1:0"
    payload = {
        "prompt": "[INST]" + prompt + "[/INST]",
        "max_gen_len": 2048,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response['body'].read().decode('utf-8'))
    return response_body['generation']
