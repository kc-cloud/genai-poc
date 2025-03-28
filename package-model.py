from transformers.convert_graph_to_onnx import convert
import os

onnx_model_path = "model.onnx"
convert(framework="pt", model=model_name, output=onnx_model_path, opset=12)

import boto3

s3 = boto3.client("s3")
bucket_name = "your-s3-bucket"
s3.upload_file("model.onnx", bucket_name, "model.onnx")
