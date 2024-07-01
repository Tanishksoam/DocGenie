from azure.storage.blob import BlobServiceClient
import os

def upload_to_azure(file_path, filename):
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    container_name = os.getenv('AZURE_STORAGE_CONTAINER')

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    return blob_client.url