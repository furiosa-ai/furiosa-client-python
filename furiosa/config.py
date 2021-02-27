import os
from pathlib import Path

import dotenv

from furiosa.client.configuration import Configuration
from furiosa.client.model.api_key import ApiKey

DEFAULT_API_ENDPOINT='https://api.furiosa.ai/api/v1'
FURIOSA_API_ENDPOINT_ENV='FURIOSA_API_ENDPOINT'
FURIOSA_ACCESS_KEY_ID_ENV='FURIOSA_ACCESS_KEY_ID'
SECRET_ACCESS_KEY_ENV='FURIOSA_SECRET_ACCESS_KEY'


class ConfigLoader(object):
    def __init__(self):
        home = str(Path.home())
        dotenv.load_dotenv('{}/.furiosa/config'.format(home), verbose=False, override=False)
        dotenv.load_dotenv('{}/.furiosa/credential'.format(home), verbose=False, override=False)

        self.api_endpoint = os.environ.get(FURIOSA_API_ENDPOINT_ENV)
        self.access_key_id = os.environ.get(FURIOSA_ACCESS_KEY_ID_ENV)
        self.secret_key_access = os.environ.get(SECRET_ACCESS_KEY_ENV)

        if self.api_endpoint is None:
            self.api_endpoint = DEFAULT_API_ENDPOINT

        if self.access_key_id is None or self.secret_key_access is None:
            raise Exception('FURIOSA_ACCESS_KEY_ID, FURIOSA_SECRET_ACCESS_KEY must be set', 1)

    def apply(self, client_configuration: Configuration):
        client_configuration.api_key['accessKeyIdAuth'] = self.access_key_id
        client_configuration.api_key['secretAccessKeyAuth'] = self.secret_key_access
        client_configuration.host = self.api_endpoint
        client_configuration.discard_unknown_keys = True


def load_furiosa_config(client_configuration=None):
    loader = ConfigLoader()

    if client_configuration is None:
        config = type.__call__(Configuration)
        loader.apply(config)
        Configuration.set_default(config)
    else:
        loader.apply(client_configuration)


def set_apikey(client_configuration, apikey: ApiKey):
    client_configuration.api_key['AccessKeyIdAuth'] = apikey.access_key_id
    client_configuration.api_key['SecretAccessKeyAuth'] = apikey.secret_access_key