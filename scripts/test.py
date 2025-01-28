import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def check_if_shared_drive(service, folder_id):
    try:
        folder = service.files().get(fileId=folder_id, fields='id, name, driveId').execute()
        if 'driveId' in folder:
            print(f"The folder '{folder['name']}' is in a Shared Drive with ID: {folder['driveId']}")
        else:
            print(f"The folder '{folder['name']}' is in My Drive.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the values for the connection with Google Drive's API
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_JSON = os.getenv('SERVICE_ACCOUNT_JSON')
    FOLDER_ID = os.getenv('FOLDER_ID')

    # Get the credentials from Google Drive's API
    credentials = service_account.Credentials.from_service_account_info(json.loads(SERVICE_ACCOUNT_JSON), scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # Check if the folder is under a Shared Drive
    check_if_shared_drive(service, FOLDER_ID)