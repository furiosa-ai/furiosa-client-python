# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from furiosa.client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from furiosa.client.model.api_key import ApiKey
from furiosa.client.model.api_key_patch import ApiKeyPatch
from furiosa.client.model.api_key_request import ApiKeyRequest
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_output import CompileOutput
from furiosa.client.model.compile_status import CompileStatus
from furiosa.client.model.compile_status_list import CompileStatusList
from furiosa.client.model.inline_object import InlineObject
from furiosa.client.model.inline_object1 import InlineObject1
from furiosa.client.model.inline_response200 import InlineResponse200
from furiosa.client.model.login_output import LoginOutput
from furiosa.client.model.login_request import LoginRequest
from furiosa.client.model.version_info import VersionInfo
