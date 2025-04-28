import boto3

sm = boto3.client('sagemaker')

response = sm.create_model(
    ModelName='gpt2-inference-model',
    PrimaryContainer={
        'Image': '<your_ecr_image_url>',
        'Mode': 'SingleModel',
        'Environment': {
            'SAGEMAKER_PROGRAM': 'inference-server.py',
            'SAGEMAKER_SUBMIT_DIRECTORY': '/app'
        }
    },
    ExecutionRoleArn='<your_sagemaker_execution_role>'
)

response = sm.create_endpoint_config(
    EndpointConfigName='gpt2-endpoint-config',
    ProductionVariants=[
        {
            'InstanceType': 'ml.m5.large',
            'InitialInstanceCount': 1,
            'ModelName': 'gpt2-inference-model',
            'VariantName': 'AllTraffic'
        }
    ]
)

response = sm.create_endpoint(
    EndpointName='gpt2-inference-endpoint',
    EndpointConfigName='gpt2-endpoint-config'
)
