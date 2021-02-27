# furiosa.client.CompilerApi

All URIs are relative to *https://api.furiosa.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile**](CompilerApi.md#compile) | **POST** /compiler | Compile


# **compile**
> CompileResult compile(x_request_id, source)

Compile

Compile a model binary (e.g., tflite, onnx) and return a NPU binary

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_result import CompileResult
from furiosa.client.model.kv_config import KvConfig
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

# Configure API key authorization: AccessKeyIdAuth
configuration.api_key['AccessKeyIdAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyIdAuth'] = 'Bearer'

# Configure API key authorization: SecretAccessKeyAuth
configuration.api_key['SecretAccessKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecretAccessKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with furiosa.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compiler_api.CompilerApi(api_client)
    x_request_id = "X-Request-ID_example" # str | Unique request Id to identify the user request
    source = open('/path/to/file', 'rb') # file_type | a byte array of a source image
    x_furiosa_ai_api_version = 1 # int | API Version (optional)
    target_npu_spec = KvConfig(
        key={
            "key": "key_example",
        },
    ) # KvConfig |  (optional)
    compiler_config = KvConfig(
        key={
            "key": "key_example",
        },
    ) # KvConfig |  (optional)
    target_ir = "target_ir_example" # str | one of followings: dfg, ldfg, cdfg, gir, lir, enf (optional)
    compiler_report = True # bool | include the compiler report if true (optional)
    mem_alloc_report = True # bool | include the memory allocation report (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compile
        api_response = api_instance.compile(x_request_id, source)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerApi->compile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compile
        api_response = api_instance.compile(x_request_id, source, x_furiosa_ai_api_version=x_furiosa_ai_api_version, target_npu_spec=target_npu_spec, compiler_config=compiler_config, target_ir=target_ir, compiler_report=compiler_report, mem_alloc_report=mem_alloc_report)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerApi->compile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| Unique request Id to identify the user request |
 **source** | **file_type**| a byte array of a source image |
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]
 **target_npu_spec** | [**KvConfig**](KvConfig.md)|  | [optional]
 **compiler_config** | [**KvConfig**](KvConfig.md)|  | [optional]
 **target_ir** | **str**| one of followings: dfg, ldfg, cdfg, gir, lir, enf | [optional]
 **compiler_report** | **bool**| include the compiler report if true | [optional]
 **mem_alloc_report** | **bool**| include the memory allocation report | [optional]

### Return type

[**CompileResult**](CompileResult.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully compiled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

