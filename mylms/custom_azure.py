from storages.backends.azure_storage import AzureStorage
from django.conf import settings

class AzureMediaStorage(AzureStorage):
    account_name = settings.lmsstorage12 # Must be replaced by your <storage_account_name>
    account_key = settings.TrA/zCzBAKt7wplnoWxU9g+sPYBXHnGEiNGFx+AR6RiHxwdx0dGEpgjLvnN0ithUaTZgaJQcoYXl+ASt3qY2hg== # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None
    # file_overwrite = False

class AzureStaticStorage(AzureStorage):
    account_name = settings.lmsstorage12 # Must be replaced by your storage_account_name
    account_key = settings.TrA/zCzBAKt7wplnoWxU9g+sPYBXHnGEiNGFx+AR6RiHxwdx0dGEpgjLvnN0ithUaTZgaJQcoYXl+ASt3qY2hg== # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
    # file_overwrite = False
