import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

class GooglePhotos:
    def __init__(self,
                 api_name = 'photoslibrary',
                 client_secret_file=r'credentials/client_secret_python_workflow.json',
                 api_version = 'v1'):
        '''
        Args:
            client_secret_file: string, location where the requested credentials are saved
            api_version: string, the version of the service
            api_name: string, name of the api e.g."docs","photoslibrary",...
        '''
def create_service(client_secret_file, api_name, api_version, *scopes):
    '''
    Args:
        client_secret_file: string, location where the requested credentials are saved
        api_version: string, the version of the service
        api_name: string, name of the api e.g. docs,photoslibrary,...
    '''

    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    # is checking if there is already a pickle file with relevant credentials
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        #example: service = build('docs', 'v1', credentials=creds)
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred, static_discovery=False)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
    return None