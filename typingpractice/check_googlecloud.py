from google.cloud import storage
from django.conf import settings
print(settings.GS_CREDENTIALS)
# Create a client using the GS_CREDENTIALS path
client = storage.Client.from_service_account_json(settings.GS_CREDENTIALS)

# Define the name of your storage bucket
bucket_name = 'guyrawit-movies'

# Define the name of the file you want to upload
file_name = 'helloworld.txt'

# Define the destination blob name in the bucket
blob_name = 'file.txt'

# Get the bucket reference
bucket = client.bucket(bucket_name)

# Create a blob from the file and upload it to the bucket
blob = bucket.blob(blob_name)
blob.upload_from_filename(file_name)

# Print a success message
print(f'Successfully uploaded file "{file_name}" to bucket "{bucket_name}" with blob name "{blob_name}"')
