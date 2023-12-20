import logging
import os

import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=YOUR-Storage_Account-Name;AccountKey=YOUR-Storage_Account-KEY;EndpointSuffix=core.windows.net"
container_name = "input"
destination_container_name = "output"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

def get_metadata_and_copy(blob_file):
# Loop through each blob in the container
    #for blob in container_client.list_blobs():
        # Get a BlobClient for each blob
        blob_client = blob_service_client.get_blob_client(container_name, blob_file)    
        blob_metadata = blob_client.get_blob_properties().metadata
        
        # Set metadata on the blob
        #more_blob_metadata = {'id': '1628178.1', 'title': 'ar1feve', 'product': 'Genbbussiness', 'pilot': 'Y', 'source': 'adobedam'}
        #blob_metadata.update(more_blob_metadata)
        #blob_client.set_blob_metadata(metadata=blob_metadata)

        # Get file with metadata pilot == Y
        if blob_metadata.get('pilot') == 'Y':
        
            # print the metadata for each file
            print(f"Metadata for file {blob_file}: {blob_metadata}")
            
            # copy file with metadata pilot == Y to output folder
            destination_blob_client = blob_service_client.get_blob_client(destination_container_name, blob_file)
            copy_source_url = blob_client.url
            print(f"Source file URL: {copy_source_url}")
            destination_blob_client.start_copy_from_url(copy_source_url)
            return f"file: {blob_file} with {blob_metadata} copied"
        else:
            return f"file: {blob_file} with {blob_metadata} not copied"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #print(get_metadata)

    file_name = req.params.get('file_name')
    if not file_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            file_name = req_body.get('file_name')
    
    file_metadata = get_metadata_and_copy(file_name)

    if file_name:
        return func.HttpResponse(f"MetaData : {file_metadata}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )