## Google Photos API

1. Enable Google Photos API Service
   1. Create credentials and save .json in \credentials
2. Create virtual environment venv 
``python -m venv venv``
3. Install python packages https://developers.google.com/people/quickstart/python <br>
``pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
``
4. Create Google API Service ([Source](https://stackoverflow.com/questions/65184355/error-403-access-denied-from-google-authentication-web-api-despite-google-acc))
   1. Define Scope (https://developers.google.com/photos/library/guides/authorization)
   2. Go to https://console.developers.google.com/
   3. On the top left beside the words "Google APIs" click the project dropdown on the right 
   4. Ensure that your correct project is selected 
   5. Click "OAuth consent screen" on the left side of the screen (below "Credentials")
   6. If you have not created a consent screen, do that first 
   7. Under "Test users" there is a button called "+ ADD USERS"
   8. Type the email of the account you will be testing with, press enter, then click save.

If you now try to run the script for the first time, you will be asked if you trust the app and
need to give the app the required permissions to the defined scopes.

Once you done this, you will see a "token_......pickle" file created, which will be used for future authentification.

**Helpful links:**

* https://www.youtube.com/watch?v=dkxcd2Q3Qwo
* https://developers.google.com/people/quickstart/python
* https://console.developers.google.com/
* https://learndataanalysis.org/getting-started-with-google-photos-api-and-python-part-1/