# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2623
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DataTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_data_type(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get data type definition  # noqa: E501

        Get the definition of a specified data type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_type(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the data type (required)
        :param str code: The code of the data type (required)
        :param datetime as_at: The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DataType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_data_type_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_data_type_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get data type definition  # noqa: E501

        Get the definition of a specified data type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_type_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the data type (required)
        :param str code: The code of the data type (required)
        :param datetime as_at: The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DataType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_data_type`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_data_type`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_data_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_data_type`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_data_type`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_data_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2623'

        return self.api_client.call_api(
            '/api/datatypes/{scope}/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_units_from_data_type(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get units from data type  # noqa: E501

        Get the definitions of the specified units associated bound to a specific data type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_units_from_data_type(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the data type (required)
        :param str code: The code of the data type (required)
        :param list[str] units: One or more unit identifiers for which the definition is being requested
        :param str filter: Optional. Expression to filter the result set.               For example, to filter on the Schema, use \"schema eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param datetime as_at: Optional. The as at of the requested data type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfIUnitDefinitionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_units_from_data_type_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_units_from_data_type_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get units from data type  # noqa: E501

        Get the definitions of the specified units associated bound to a specific data type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_units_from_data_type_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the data type (required)
        :param str code: The code of the data type (required)
        :param list[str] units: One or more unit identifiers for which the definition is being requested
        :param str filter: Optional. Expression to filter the result set.               For example, to filter on the Schema, use \"schema eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param datetime as_at: Optional. The as at of the requested data type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfIUnitDefinitionDto, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'units', 'filter', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_units_from_data_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_units_from_data_type`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_units_from_data_type`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_units_from_data_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_units_from_data_type`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_units_from_data_type`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_units_from_data_type`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('filter' in local_var_params and
                len(local_var_params['filter']) > 2147483647):
            raise ApiValueError("Invalid value for parameter `filter` when calling `get_units_from_data_type`, length must be less than or equal to `2147483647`")  # noqa: E501
        if ('filter' in local_var_params and
                len(local_var_params['filter']) < 0):
            raise ApiValueError("Invalid value for parameter `filter` when calling `get_units_from_data_type`, length must be greater than or equal to `0`")  # noqa: E501
        if 'filter' in local_var_params and not re.search(r'(?s).*', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `get_units_from_data_type`, must conform to the pattern `/(?s).*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'units' in local_var_params:
            query_params.append(('units', local_var_params['units']))  # noqa: E501
            collection_formats['units'] = 'multi'  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2623'

        return self.api_client.call_api(
            '/api/datatypes/{scope}/{code}/units', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfIUnitDefinitionDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_data_types(self, scope, **kwargs):  # noqa: E501
        """[EARLY ACCESS] List data types  # noqa: E501

        List all data types in a specified scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_data_types(scope, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The requested scope of the data types (required)
        :param datetime as_at: The as at of the requested data types
        :param bool include_system: Whether to additionally include those data types in the \"system\" scope
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfDataType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_data_types_with_http_info(scope, **kwargs)  # noqa: E501

    def list_data_types_with_http_info(self, scope, **kwargs):  # noqa: E501
        """[EARLY ACCESS] List data types  # noqa: E501

        List all data types in a specified scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_data_types_with_http_info(scope, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The requested scope of the data types (required)
        :param datetime as_at: The as at of the requested data types
        :param bool include_system: Whether to additionally include those data types in the \"system\" scope
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfDataType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'as_at', 'include_system', 'sort_by', 'start', 'limit', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_data_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_data_types`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_data_types`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_data_types`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('filter' in local_var_params and
                len(local_var_params['filter']) > 2147483647):
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_data_types`, length must be less than or equal to `2147483647`")  # noqa: E501
        if ('filter' in local_var_params and
                len(local_var_params['filter']) < 0):
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_data_types`, length must be greater than or equal to `0`")  # noqa: E501
        if 'filter' in local_var_params and not re.search(r'(?s).*', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_data_types`, must conform to the pattern `/(?s).*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'include_system' in local_var_params:
            query_params.append(('includeSystem', local_var_params['include_system']))  # noqa: E501
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2623'

        return self.api_client.call_api(
            '/api/datatypes/{scope}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfDataType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
