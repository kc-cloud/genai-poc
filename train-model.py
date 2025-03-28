import mlflow
import torch
from transformers import TrainingArguments, Trainer
from datasets import load_dataset

# Load dataset
dataset = load_dataset("samsum")  # Replace with your dataset

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    logging_dir="./logs",
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"]
)

# Start MLflow tracking
mlflow.set_experiment("gen-ai-finetuning")

with mlflow.start_run():
    trainer.train()
    mlflow.log_params(training_args.to_dict())

    # Save model to MLflow
    model_path = "mlflow_model"
    trainer.save_model(model_path)
    mlflow.pytorch.log_model(model, "model")
