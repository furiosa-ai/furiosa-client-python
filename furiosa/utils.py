import os

from furiosa.openapi import ApiClient, Configuration
from furiosa.openapi.api.account_v1_api import AccountV1Api
from furiosa.openapi.model.login_request import LoginRequest


def login_account(client: ApiClient):
    request = LoginRequest(email=os.environ['FURIOSA_USERNAME'],
                           password=os.environ['FURIOSA_PASSWORD'])
    account_api = AccountV1Api()
    auth = account_api.login(request=request)
    client.configuration.access_token = auth.access_token
    Configuration.set_default(client.configuration)
    return client
