
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
DESCRIPTION:
    Given an AIProjectClient, this sample demonstrates how to get an authenticated 
    AsyncAzureOpenAI client from the azure.ai.inference package.

USAGE:
    python sample_get_azure_openai_client.py

    Before running the sample:

    pip install azure-ai-projects openai

    Set these environment variables with your own values:
    * PROJECT_CONNECTION_STRING - the Azure AI Project connection string, as found in your AI Studio Project.
    * MODEL_DEPLOYMENT_NAME - The model deployment name, as found in your AI Studio Project.

    Update the Azure OpenAI api-version as needed (see `api_version=` below). Values can be found here:
    https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#api-specs
"""
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from dotenv import load_dotenv
load_dotenv()

PROJECT_CONNECTION_STRING ="francecentral.api.azureml.ms;f93b65a5-0bac-4e59-b286-140e2dae416d;rg-contosodev;jturuk-3055"
MODEL_DEPLOYMENT_NAME ="gpt-4o-mini"
project_connection_string = PROJECT_CONNECTION_STRING
model_deployment_name = MODEL_DEPLOYMENT_NAME
#project_connection_string = os.environ["PROJECT_CONNECTION_STRING"]
#model_deployment_name = os.environ["MODEL_DEPLOYMENT_NAME"]

with AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=project_connection_string,
) as project_client:

    with project_client.inference.get_azure_openai_client(api_version="2024-06-01") as client:

        response = client.chat.completions.create(
            model=model_deployment_name,
            messages=[
                {
                    "role": "user",
                    "content": "How many feet are in a mile?",
                },
            ],
        )

        print(response.choices[0].message.content)