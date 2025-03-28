model_uri = f"runs:/{mlflow.active_run().info.run_id}/model"
model_version = mlflow.register_model(model_uri, "GenAIModel")

