import boto3
import json

runtime = boto3.client("sagemaker-runtime")

def query_model(prompt):
    payload = json.dumps({"inputs": prompt})
    
    response = runtime.invoke_endpoint(
        EndpointName="GenAIONNXEndpoint",
        ContentType="application/json",
        Body=payload
    )

    return json.loads(response["Body"].read().decode())

print(query_model("What is the capital of France?"))
