import os
import google_photos_api

API_NAME = 'GooglePhotosAnalysisPython'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = r'./credentials/client_secret_python_workflow.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

service = google_photos_api.create_service(CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)