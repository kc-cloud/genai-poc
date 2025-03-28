import sagemaker

sm_client = boto3.client("sagemaker")

model_name = "GenAIONNXModel"

container = {
    "Image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.9.1-cpu-py38",
    "ModelDataUrl": f"s3://{bucket_name}/model.onnx",
    "Environment": {"SAGEMAKER_MODEL_SERVER_WORKERS": "1"},
}

response = sm_client.create_model(
    ModelName=model_name,
    ExecutionRoleArn="arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole",
    PrimaryContainer=container,
)

endpoint_config_name = "GenAIONNXEndpointConfig"

sm_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[
        {
            "InstanceType": "ml.m5.large",
            "InitialInstanceCount": 1,
            "ModelName": model_name,
            "VariantName": "AllTraffic",
        }
    ],
)

sm_client.create_endpoint(
    EndpointName="GenAIONNXEndpoint",
    EndpointConfigName=endpoint_config_name,
)
