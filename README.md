# azfnCopyFileBasedOnMetadata

## Prerequsites:

please replace connection_string with your storage account connection string in _init_.py , local.settings.json and BulkCopyFileBasedOnMetadata.py files before testing the fucntion or the Bulk upload.

connection_string = "DefaultEndpointsProtocol=https;AccountName=YOUR-Storage_Account-Name;AccountKey=YOUR-Storage_Account-KEY;EndpointSuffix=core.windo

## Usage - Function call 
 curl -X GET http://localhost:7071/api/fnname?file_name=figure-1-1.jpg

 or

 curl -X POST http://localhost:7071/api/fnname -d '{"file_name": "figure-1-1.jpg"}

 
