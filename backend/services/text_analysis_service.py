from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

def authenticate_client():
    key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")
    endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")

    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

def analyze_text(text):
    client = authenticate_client()

    documents = [text]

    response = client.analyze_sentiment(documents=documents)[0]
    return {
        'sentiment': response.sentiment,
        'confidence_scores': {
            'positive': response.confidence_scores.positive,
            'neutral': response.confidence_scores.neutral,
            'negative': response.confidence_scores.negative
        }
    }