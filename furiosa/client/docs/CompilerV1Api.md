# furiosa.client.CompilerV1Api

All URIs are relative to *https://api.furiosa.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](CompilerV1Api.md#create_task) | **POST** /api/compiler/v1alpha1/tasks | Compile
[**get_artifacts**](CompilerV1Api.md#get_artifacts) | **GET** /api/compiler/v1alpha1/tasks/{task_id}/artifacts | Get compilation task status
[**get_task**](CompilerV1Api.md#get_task) | **GET** /api/compiler/v1alpha1/tasks/{task_id} | Get compilation task status
[**get_toolchains**](CompilerV1Api.md#get_toolchains) | **GET** /api/compiler/v1alpha1/toolchains | Get compiler toolchains
[**kill_task**](CompilerV1Api.md#kill_task) | **DELETE** /api/compiler/v1alpha1/tasks/{task_id} | Kill the compilation task
[**list_tasks**](CompilerV1Api.md#list_tasks) | **GET** /api/compiler/v1alpha1/tasks | List compilation tasks


# **create_task**
> CompileStatus create_task(x_request_id, source)

Compile

Create a task to compile a model binary (e.g., tflite, onnx)

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_status import CompileStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    x_request_id = "X-Request-ID_example" # str | Unique request Id to identify the user request
    source = open('/path/to/file', 'rb') # file_type | a byte array of a source image
    x_furiosa_ai_api_version = 1 # int | API Version (optional)
    target_npu_spec = "target_npu_spec_example" # str |  (optional)
    compiler_config = "compiler_config_example" # str |  (optional)
    target_ir = "target_ir_example" # str | one of followings: dfg, ldfg, cdfg, gir, lir, enf (optional)
    compiler_report = True # bool | include the compiler report if true (optional)
    mem_alloc_report = True # bool | include the memory allocation report (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compile
        api_response = api_instance.create_task(x_request_id, source)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->create_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compile
        api_response = api_instance.create_task(x_request_id, source, x_furiosa_ai_api_version=x_furiosa_ai_api_version, target_npu_spec=target_npu_spec, compiler_config=compiler_config, target_ir=target_ir, compiler_report=compiler_report, mem_alloc_report=mem_alloc_report)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| Unique request Id to identify the user request |
 **source** | **file_type**| a byte array of a source image |
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]
 **target_npu_spec** | **str**|  | [optional]
 **compiler_config** | **str**|  | [optional]
 **target_ir** | **str**| one of followings: dfg, ldfg, cdfg, gir, lir, enf | [optional]
 **compiler_report** | **bool**| include the compiler report if true | [optional]
 **mem_alloc_report** | **bool**| include the memory allocation report | [optional]

### Return type

[**CompileStatus**](CompileStatus.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully submitted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts**
> CompileStatus get_artifacts(task_id)

Get compilation task status

Get a compilation task status

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_status import CompileStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    task_id = "task_id_example" # str | API key to be patched
    x_furiosa_ai_api_version = 1 # int | API Version (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get compilation task status
        api_response = api_instance.get_artifacts(task_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->get_artifacts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get compilation task status
        api_response = api_instance.get_artifacts(task_id, x_furiosa_ai_api_version=x_furiosa_ai_api_version)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->get_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| API key to be patched |
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]

### Return type

[**CompileStatus**](CompileStatus.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully compiled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> CompileStatus get_task(task_id)

Get compilation task status

Get a compilation task status

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_status import CompileStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    task_id = "task_id_example" # str | API key to be patched
    x_furiosa_ai_api_version = 1 # int | API Version (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get compilation task status
        api_response = api_instance.get_task(task_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->get_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get compilation task status
        api_response = api_instance.get_task(task_id, x_furiosa_ai_api_version=x_furiosa_ai_api_version)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| API key to be patched |
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]

### Return type

[**CompileStatus**](CompileStatus.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully compiled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_toolchains**
> CompileOutput get_toolchains()

Get compiler toolchains

Get compiler toolchain information

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_output import CompileOutput
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    x_furiosa_ai_api_version = 1 # int | API Version (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get compiler toolchains
        api_response = api_instance.get_toolchains(x_furiosa_ai_api_version=x_furiosa_ai_api_version)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->get_toolchains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]

### Return type

[**CompileOutput**](CompileOutput.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully compiled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_task**
> ApiResponse kill_task(task_id)

Kill the compilation task

Kill the compilation task

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    task_id = "task_id_example" # str | API key to be patched
    x_furiosa_ai_api_version = 1 # int | API Version (optional)

    # example passing only required values which don't have defaults set
    try:
        # Kill the compilation task
        api_response = api_instance.kill_task(task_id)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->kill_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Kill the compilation task
        api_response = api_instance.kill_task(task_id, x_furiosa_ai_api_version=x_furiosa_ai_api_version)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->kill_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| API key to be patched |
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully killed |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> CompileStatusList list_tasks()

List compilation tasks

List all running compilation tasks

### Example

* Api Key Authentication (AccessKeyIdAuth):
* Api Key Authentication (SecretAccessKeyAuth):
```python
import time
import furiosa.client
from furiosa.client.api import compiler_v1_api
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_status_list import CompileStatusList
from pprint import pprint
# Defining the host is optional and defaults to https://api.furiosa.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = furiosa.client.Configuration(
    host = "https://api.furiosa.ai"
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
    api_instance = compiler_v1_api.CompilerV1Api(api_client)
    x_furiosa_ai_api_version = 1 # int | API Version (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compilation tasks
        api_response = api_instance.list_tasks(x_furiosa_ai_api_version=x_furiosa_ai_api_version)
        pprint(api_response)
    except furiosa.client.ApiException as e:
        print("Exception when calling CompilerV1Api->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_furiosa_ai_api_version** | **int**| API Version | [optional]

### Return type

[**CompileStatusList**](CompileStatusList.md)

### Authorization

[AccessKeyIdAuth](../README.md#AccessKeyIdAuth), [SecretAccessKeyAuth](../README.md#SecretAccessKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully compiled |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. It can happen when no API key is set or the given API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

