from azure.storage import CloudStorageAccount

class AzureUploader():
    def __init__(self):
        account_name = 'jianalphazerostorage'
        account_key = #''
        account = CloudStorageAccount(account_name, account_key)
        self.blockblob_service = account.create_block_blob_service()
        self.container_name = 'alphamodel'
        
    def upload(self, modelPath, modelName):
        self.blockblob_service.create_blob_from_path(self.container_name, modelName, modelPath)
        generator = self.blockblob_service.list_blobs(self.container_name)
        for blob in generator:
            print('\tBlob Name: ' + blob.name)