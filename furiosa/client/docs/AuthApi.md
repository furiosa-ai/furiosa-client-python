# furiosa.client.AuthApi

All URIs are relative to *https://api.furiosa.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /auth/login | Login


# **login**
> LoginResponse login()

Login

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import furiosa.client
from furiosa.client.api import auth_api
from furiosa.client.model.login_request import LoginRequest
from furiosa.client.model.login_response import LoginResponse
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
    api_instance = auth_api.AuthApi(api_client)
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
        print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional]

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ss |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

