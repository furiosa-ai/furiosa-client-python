# furiosa.client.AccountApi

All URIs are relative to *https://api.furiosa.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](AccountApi.md#create_api_key) | **POST** /account/me/apikeys | Generate new API key
[**delete_api_key**](AccountApi.md#delete_api_key) | **DELETE** /account/me/apikeys/{access_key_id} | Delete a API key
[**get_account_info**](AccountApi.md#get_account_info) | **GET** /account/me | Get my account information
[**get_api_key**](AccountApi.md#get_api_key) | **GET** /account/me/apikeys/{access_key_id} | Get a API key
[**list_api_keys**](AccountApi.md#list_api_keys) | **GET** /account/me/apikeys | List generated API keys
[**login**](AccountApi.md#login) | **POST** /account/login | Login
[**update_account_info**](AccountApi.md#update_account_info) | **PUT** /account/me | Update my account information
[**update_account_password**](AccountApi.md#update_account_password) | **PUT** /account/me/password | Change my account password
[**update_api_key**](AccountApi.md#update_api_key) | **PUT** /account/me/apikeys/{access_key_id} | Update a API key


# **create_api_key**
> ApiKey create_api_key()

Generate new API key

Generate a new API key

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_key import ApiKey
from furiosa.client.model.api_key_request import ApiKeyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_key_request = ApiKeyRequest(
        name="name_example",
        description="description_example",
    ) # ApiKeyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate new API key
        api_response = api_instance.create_api_key(api_key_request=api_key_request)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**ApiKeyRequest**](ApiKeyRequest.md)|  | [optional]

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully new API key has been generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> ApiResponse delete_api_key(access_key_id)

Delete a API key

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_response import ApiResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    access_key_id = "access_key_id_example" # str | API key ID to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete a API key
        api_response = api_instance.delete_api_key(access_key_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **str**| API key ID to be deleted |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key has been deleted successfully |  -  |
**404** | API key is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_info**
> InlineResponse200 get_account_info()

Get my account information

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get my account information
        api_response = api_instance.get_account_info()
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->get_account_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKey get_api_key(access_key_id)

Get a API key

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.api_key import ApiKey
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    access_key_id = "access_key_id_example" # str | API key ID to get

    # example passing only required values which don't have defaults set
    try:
        # Get a API key
        api_response = api_instance.get_api_key(access_key_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **str**| API key ID to get |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a API key |  -  |
**404** | API key is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> [ApiKey] list_api_keys()

List generated API keys

List all generated API keys

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_key import ApiKey
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List generated API keys
        api_response = api_instance.list_api_keys()
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->list_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ApiKey]**](ApiKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all API keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginResponse login()

Login

### Example

```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.login_request import LoginRequest
from furiosa.client.model.login_response import LoginResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)


# Enter a context with an instance of the API client
with furiosa.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    login_request = LoginRequest(
        email="email_example",
        password="password_example",
        remember_me=True,
    ) # LoginRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Login
        api_response = api_instance.login(login_request=login_request)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional]

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logged in successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_info**
> ApiResponse update_account_info()

Update my account information

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    inline_object = InlineObject(
        surname="surname_example",
        given_name="given_name_example",
        email="email_example",
        password="password_example",
        company="company_example",
        phone="phone_example",
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update my account information
        api_response = api_instance.update_account_info(inline_object=inline_object)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->update_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | My account has been updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_password**
> ApiResponse update_account_password()

Change my account password

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.inline_object1 import InlineObject1
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    inline_object1 = InlineObject1(
        old_password="old_password_example",
        new_password="new_password_example",
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change my account password
        api_response = api_instance.update_account_password(inline_object1=inline_object1)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->update_account_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | My account password has been updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiResponse update_api_key(access_key_id)

Update a API key

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import account_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.inline_object2 import InlineObject2
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = furiosa.client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    access_key_id = "access_key_id_example" # str | API key to be updated
    inline_object2 = InlineObject2(
        active=True,
    ) # InlineObject2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a API key
        api_response = api_instance.update_api_key(access_key_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->update_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a API key
        api_response = api_instance.update_api_key(access_key_id, inline_object2=inline_object2)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling AccountApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **str**| API key to be updated |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the API key has been updated successfully |  -  |
**404** | API key is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

