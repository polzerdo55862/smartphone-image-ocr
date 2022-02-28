import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

class GooglePhotosApi:
    def __init__(self,
                 api_name = 'photoslibrary',
                 client_secret_file=os.path.dirname(__file__) + r'/credentials/client_secret_python_workflow.json',
                 api_version = 'v1',
                 scopes = ['https://www.googleapis.com/auth/photoslibrary']):
        '''
        Args:
            client_secret_file: string, location where the requested credentials are saved
            api_version: string, the version of the service
            api_name: string, name of the api e.g."docs","photoslibrary",...
            api_version: version of the api

        Return:
            service:
        '''

        self.api_name = api_name
        self.client_secret_file = client_secret_file
        self.api_version = api_version
        self.scopes = scopes
        self.cred_picke_file = f'token_{self.api_name}_{self.api_version}.pickle'

        cred = None

    def create_service(self):
        # is checking if there is already a pickle file with relevant credentials
        if os.path.exists(self.cred_picke_file):
            with open(self.cred_picke_file, 'rb') as token:
                cred = pickle.load(token)

        # if there is no pickle file with stored credentials, create one using google_auth_oauthlib.flow
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
                cred = flow.run_local_server()

            with open(self.cred_picke_file, 'wb') as token:
                pickle.dump(cred, token)

        # try to set up the service to the google photos API
        try:
            # example: service = build('docs', 'v1', credentials=creds)
            service = build(self.api_name, self.api_version, credentials=cred, static_discovery=False)
            print(self.api_name, 'service created successfully')
            return service
        except Exception as e:
            print(e)
        return None