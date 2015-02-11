from __future__ import print_function

import httplib2
import os

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


# Redirect URI for installed (out-of-band) apps
OOB_REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

credentials_storage = Storage('.credentials')

# Check https://developers.google.com/admin-sdk/directory/v1/guides/authorizing
# for all available scopes
def get_authenticated_http(oauth_scope):
    credentials = credentials_storage.get()

    if not credentials:
        flow = OAuth2WebServerFlow(
            os.environ['GOOGLE_CLIENT_ID'],
            os.environ['GOOGLE_CLIENT_SECRET'],
            oauth_scope,
            OOB_REDIRECT_URI)

        print('Go to the following link in your browser:',
              flow.step1_get_authorize_url())
        code = raw_input('Enter verification code: ').strip()

        credentials = flow.step2_exchange(code)
        credentials_storage.put(credentials)

    return credentials.authorize(httplib2.Http())
