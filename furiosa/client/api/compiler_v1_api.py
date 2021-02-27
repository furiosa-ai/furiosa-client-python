"""
    Furiosa AI Web Service API

    Furiosa AI Web Service API for Compiler and Model Tools  # noqa: E501

    The version of the OpenAPI document: v1alpha
    Contact: contact@furisa.ai
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from furiosa.client.api_client import ApiClient, Endpoint as _Endpoint
from furiosa.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from furiosa.client.model.api_response import ApiResponse
from furiosa.client.model.compile_output import CompileOutput
from furiosa.client.model.compile_status import CompileStatus
from furiosa.client.model.compile_status_list import CompileStatusList


class CompilerV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_task(
            self,
            x_request_id,
            source,
            **kwargs
        ):
            """Compile  # noqa: E501

            Create a task to compile a model binary (e.g., tflite, onnx)  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_task(x_request_id, source, async_req=True)
            >>> result = thread.get()

            Args:
                x_request_id (str): Unique request Id to identify the user request
                source (file_type): a byte array of a source image

            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                target_npu_spec (str): [optional]
                compiler_config (str): [optional]
                target_ir (str): one of followings: dfg, ldfg, cdfg, gir, lir, enf. [optional]
                compiler_report (bool): include the compiler report if true. [optional]
                mem_alloc_report (bool): include the memory allocation report. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CompileStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_request_id'] = \
                x_request_id
            kwargs['source'] = \
                source
            return self.call_with_http_info(**kwargs)

        self.create_task = _Endpoint(
            settings={
                'response_type': (CompileStatus,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/tasks',
                'operation_id': 'create_task',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'source',
                    'x_furiosa_ai_api_version',
                    'target_npu_spec',
                    'compiler_config',
                    'target_ir',
                    'compiler_report',
                    'mem_alloc_report',
                ],
                'required': [
                    'x_request_id',
                    'source',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'source':
                        (file_type,),
                    'x_furiosa_ai_api_version':
                        (int,),
                    'target_npu_spec':
                        (str,),
                    'compiler_config':
                        (str,),
                    'target_ir':
                        (str,),
                    'compiler_report':
                        (bool,),
                    'mem_alloc_report':
                        (bool,),
                },
                'attribute_map': {
                    'x_request_id': 'X-Request-ID',
                    'source': 'source',
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                    'target_npu_spec': 'target_npu_spec',
                    'compiler_config': 'compiler_config',
                    'target_ir': 'target_ir',
                    'compiler_report': 'compiler_report',
                    'mem_alloc_report': 'mem_alloc_report',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'source': 'form',
                    'x_furiosa_ai_api_version': 'header',
                    'target_npu_spec': 'form',
                    'compiler_config': 'form',
                    'target_ir': 'form',
                    'compiler_report': 'form',
                    'mem_alloc_report': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__create_task
        )

        def __get_artifacts(
            self,
            task_id,
            **kwargs
        ):
            """Get compilation task status  # noqa: E501

            Get a compilation task status  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_artifacts(task_id, async_req=True)
            >>> result = thread.get()

            Args:
                task_id (str): API key to be patched

            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CompileStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['task_id'] = \
                task_id
            return self.call_with_http_info(**kwargs)

        self.get_artifacts = _Endpoint(
            settings={
                'response_type': (CompileStatus,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/tasks/{task_id}/artifacts',
                'operation_id': 'get_artifacts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'x_furiosa_ai_api_version',
                ],
                'required': [
                    'task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'task_id':
                        (str,),
                    'x_furiosa_ai_api_version':
                        (int,),
                },
                'attribute_map': {
                    'task_id': 'task_id',
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                },
                'location_map': {
                    'task_id': 'path',
                    'x_furiosa_ai_api_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_artifacts
        )

        def __get_task(
            self,
            task_id,
            **kwargs
        ):
            """Get compilation task status  # noqa: E501

            Get a compilation task status  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_task(task_id, async_req=True)
            >>> result = thread.get()

            Args:
                task_id (str): API key to be patched

            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CompileStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['task_id'] = \
                task_id
            return self.call_with_http_info(**kwargs)

        self.get_task = _Endpoint(
            settings={
                'response_type': (CompileStatus,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/tasks/{task_id}',
                'operation_id': 'get_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'x_furiosa_ai_api_version',
                ],
                'required': [
                    'task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'task_id':
                        (str,),
                    'x_furiosa_ai_api_version':
                        (int,),
                },
                'attribute_map': {
                    'task_id': 'task_id',
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                },
                'location_map': {
                    'task_id': 'path',
                    'x_furiosa_ai_api_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_task
        )

        def __get_toolchains(
            self,
            **kwargs
        ):
            """Get compiler toolchains  # noqa: E501

            Get compiler toolchain information  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_toolchains(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CompileOutput
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_toolchains = _Endpoint(
            settings={
                'response_type': (CompileOutput,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/toolchains',
                'operation_id': 'get_toolchains',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_furiosa_ai_api_version',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_furiosa_ai_api_version':
                        (int,),
                },
                'attribute_map': {
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                },
                'location_map': {
                    'x_furiosa_ai_api_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_toolchains
        )

        def __kill_task(
            self,
            task_id,
            **kwargs
        ):
            """Kill the compilation task  # noqa: E501

            Kill the compilation task  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.kill_task(task_id, async_req=True)
            >>> result = thread.get()

            Args:
                task_id (str): API key to be patched

            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['task_id'] = \
                task_id
            return self.call_with_http_info(**kwargs)

        self.kill_task = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/tasks/{task_id}',
                'operation_id': 'kill_task',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'x_furiosa_ai_api_version',
                ],
                'required': [
                    'task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'task_id':
                        (str,),
                    'x_furiosa_ai_api_version':
                        (int,),
                },
                'attribute_map': {
                    'task_id': 'task_id',
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                },
                'location_map': {
                    'task_id': 'path',
                    'x_furiosa_ai_api_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__kill_task
        )

        def __list_tasks(
            self,
            **kwargs
        ):
            """List compilation tasks  # noqa: E501

            List all running compilation tasks  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_tasks(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_furiosa_ai_api_version (int): API Version. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CompileStatusList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_tasks = _Endpoint(
            settings={
                'response_type': (CompileStatusList,),
                'auth': [
                    'AccessKeyIdAuth',
                    'SecretAccessKeyAuth'
                ],
                'endpoint_path': '/api/compiler/v1alpha1/tasks',
                'operation_id': 'list_tasks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_furiosa_ai_api_version',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_furiosa_ai_api_version':
                        (int,),
                },
                'attribute_map': {
                    'x_furiosa_ai_api_version': 'X-FuriosaAI-API-Version',
                },
                'location_map': {
                    'x_furiosa_ai_api_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_tasks
        )
