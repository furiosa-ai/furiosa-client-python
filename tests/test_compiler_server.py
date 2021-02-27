import os
import unittest
import uuid

from furiosa.client import ApiClient
from furiosa.client.api.account_v1_api import ApiKey, AccountV1Api
from furiosa.client.api.compiler_v1_api import CompilerV1Api
from furiosa.client.api.version_api import VersionApi
from furiosa.client.models import VersionInfo, LoginRequest, ApiKeyRequest, ApiKeyPatch
from furiosa.config import load_furiosa_config, set_apikey
from furiosa.utils import login_account

load_furiosa_config()
client = login_account(ApiClient())
account_api = AccountV1Api(api_client=client)
version_api = VersionApi(api_client=client)


class ParserTest(unittest.TestCase):
    client = None

    def setUp(self) -> None:
        request = ApiKeyRequest(name=uuid.uuid4().__str__())
        apikey: ApiKey = account_api.create_api_key(request=request)
        self.access_key_id = apikey.access_key_id
        set_apikey(client.configuration, apikey)
        self.compiler_api = CompilerV1Api(api_client=client)

    def tearDown(self) -> None:
        account_api.patch_api_key(self.access_key_id,
                                  request=ApiKeyPatch(active=False))

    def test_version(self):
        version: VersionInfo = version_api.version()
        self.assertEqual(version.version, "0.1.10-dev")

    def test_login(self):
        request = LoginRequest(email=os.environ['FURIOSA_USERNAME'], password=os.environ['FURIOSA_PASSWORD'])
        authenticated = account_api.login(login_request=request)
        self.assertTrue(authenticated.access_token is not None)
        self.assertTrue(authenticated.expires_at is not None)
        self.assertEqual(authenticated.token_type, 'Bearer')

    def test_apikey_set(self):
        names = []
        for idx in range(0, 5):
            names.append(uuid.uuid4().__str__())

        for name in names:
            name = name.__str__()
            request = ApiKeyRequest(name=name, description=name)
            apikey: ApiKey = account_api.create_api_key(request=request)
            self.assertEqual(apikey.name, name)
            self.assertEqual(apikey.description, name)
            self.assertTrue(apikey.active)

        apikey_list: [ApiKey] = account_api.list_api_keys()
        apikey_dict = {key.name: key for key in apikey_list}

        for name in names:
            self.assertTrue(name in apikey_dict)

        for name in names:
            apikey = apikey_dict[name]
            account_api.patch_api_key(apikey.access_key_id,
                                      request=ApiKeyPatch(active=False))

    def test_compile(self):
        request_id = uuid.uuid4().__str__();
        with open('test_data/MNISTnet_uint8_quant_without_softmax.tflite', 'rb') as file:
            response = self.compiler_api.create_task(x_request_id=request_id,
                                                     source=file,
                                                     x_furiosa_ai_api_version=3)
            print(response)


if __name__ == '__main__':
    unittest.main()
