from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=YOUR-Storage_Account-Name;AccountKey=YOUR-Storage_Account-KEY;EndpointSuffix=core.windows.net"
container_name = "input"
destination_container_name = "output"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Loop through each blob in the container
for blob in container_client.list_blobs():
    # Get a BlobClient for each blob
    blob_client = blob_service_client.get_blob_client(container_name, blob.name)    
    blob_metadata = blob_client.get_blob_properties().metadata
    
    # Set metadata on the blob
    #more_blob_metadata = {'id': '1628178.1', 'title': 'ar1feve', 'product': 'Genbbussiness', 'pilot': 'Y', 'source': 'adobedam'}
    #blob_metadata.update(more_blob_metadata)
    #blob_client.set_blob_metadata(metadata=blob_metadata)

    # Get file with metadata pilot == Y
    if blob_metadata.get('pilot') == 'Y':
    
        # print the metadata for each file
        print(f"Metadata for file {blob.name}: {blob_metadata}")
        
        # copy file with metadata pilot == Y to output folder
        destination_blob_client = blob_service_client.get_blob_client(destination_container_name, blob.name)
        copy_source_url = blob_client.url
        print(f"Source file URL: {copy_source_url}")
        destination_blob_client.start_copy_from_url(copy_source_url)