# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field, StrictBool, conlist, constr, validator

from typing import Optional

from lusid.models.allocation_service_run_response import AllocationServiceRunResponse
from lusid.models.book_transactions_response import BookTransactionsResponse
from lusid.models.resource_id import ResourceId

from lusid.api_client import ApiClient
from lusid.api_response import ApiResponse
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OrderManagementApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def book_transactions(self, resource_id : Annotated[conlist(ResourceId, max_items=5000), Field(..., description="The allocations to create transactions for")], apply_fees_and_commission : Annotated[Optional[StrictBool], Field(description="Whether to apply fees and commissions to transactions (default: true)")] = None, **kwargs) -> BookTransactionsResponse:  # noqa: E501
        ...

    @overload
    def book_transactions(self, resource_id : Annotated[conlist(ResourceId, max_items=5000), Field(..., description="The allocations to create transactions for")], apply_fees_and_commission : Annotated[Optional[StrictBool], Field(description="Whether to apply fees and commissions to transactions (default: true)")] = None, async_req: Optional[bool]=True, **kwargs) -> BookTransactionsResponse:  # noqa: E501
        ...

    @validate_arguments
    def book_transactions(self, resource_id : Annotated[conlist(ResourceId, max_items=5000), Field(..., description="The allocations to create transactions for")], apply_fees_and_commission : Annotated[Optional[StrictBool], Field(description="Whether to apply fees and commissions to transactions (default: true)")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[BookTransactionsResponse, Awaitable[BookTransactionsResponse]]:  # noqa: E501
        """[EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.  # noqa: E501

        Takes a collection of allocation IDs, and maps fields from those allocations and related orders onto new transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.book_transactions(resource_id, apply_fees_and_commission, async_req=True)
        >>> result = thread.get()

        :param resource_id: The allocations to create transactions for (required)
        :type resource_id: List[ResourceId]
        :param apply_fees_and_commission: Whether to apply fees and commissions to transactions (default: true)
        :type apply_fees_and_commission: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BookTransactionsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the book_transactions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.book_transactions_with_http_info(resource_id, apply_fees_and_commission, **kwargs)  # noqa: E501

    @validate_arguments
    def book_transactions_with_http_info(self, resource_id : Annotated[conlist(ResourceId, max_items=5000), Field(..., description="The allocations to create transactions for")], apply_fees_and_commission : Annotated[Optional[StrictBool], Field(description="Whether to apply fees and commissions to transactions (default: true)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.  # noqa: E501

        Takes a collection of allocation IDs, and maps fields from those allocations and related orders onto new transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.book_transactions_with_http_info(resource_id, apply_fees_and_commission, async_req=True)
        >>> result = thread.get()

        :param resource_id: The allocations to create transactions for (required)
        :type resource_id: List[ResourceId]
        :param apply_fees_and_commission: Whether to apply fees and commissions to transactions (default: true)
        :type apply_fees_and_commission: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BookTransactionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'apply_fees_and_commission'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method book_transactions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('apply_fees_and_commission') is not None:  # noqa: E501
            _query_params.append(('applyFeesAndCommission', _params['apply_fees_and_commission']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['resource_id'] is not None:
            _body_params = _params['resource_id']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "BookTransactionsResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/ordermanagement/booktransactions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def run_allocation_service(self, resource_id : Annotated[conlist(ResourceId, max_items=100), Field(..., description="The List of Placement IDs for which you wish to allocate executions.")], allocation_algorithm : Annotated[Optional[constr(strict=True, max_length=64, min_length=1)], Field(description="A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".")] = None, **kwargs) -> AllocationServiceRunResponse:  # noqa: E501
        ...

    @overload
    def run_allocation_service(self, resource_id : Annotated[conlist(ResourceId, max_items=100), Field(..., description="The List of Placement IDs for which you wish to allocate executions.")], allocation_algorithm : Annotated[Optional[constr(strict=True, max_length=64, min_length=1)], Field(description="A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".")] = None, async_req: Optional[bool]=True, **kwargs) -> AllocationServiceRunResponse:  # noqa: E501
        ...

    @validate_arguments
    def run_allocation_service(self, resource_id : Annotated[conlist(ResourceId, max_items=100), Field(..., description="The List of Placement IDs for which you wish to allocate executions.")], allocation_algorithm : Annotated[Optional[constr(strict=True, max_length=64, min_length=1)], Field(description="A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[AllocationServiceRunResponse, Awaitable[AllocationServiceRunResponse]]:  # noqa: E501
        """[EXPERIMENTAL] RunAllocationService: Runs the Allocation Service  # noqa: E501

        This will allocate executions for a given list of placements back to their originating orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.run_allocation_service(resource_id, allocation_algorithm, async_req=True)
        >>> result = thread.get()

        :param resource_id: The List of Placement IDs for which you wish to allocate executions. (required)
        :type resource_id: List[ResourceId]
        :param allocation_algorithm: A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".
        :type allocation_algorithm: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AllocationServiceRunResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the run_allocation_service_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.run_allocation_service_with_http_info(resource_id, allocation_algorithm, **kwargs)  # noqa: E501

    @validate_arguments
    def run_allocation_service_with_http_info(self, resource_id : Annotated[conlist(ResourceId, max_items=100), Field(..., description="The List of Placement IDs for which you wish to allocate executions.")], allocation_algorithm : Annotated[Optional[constr(strict=True, max_length=64, min_length=1)], Field(description="A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] RunAllocationService: Runs the Allocation Service  # noqa: E501

        This will allocate executions for a given list of placements back to their originating orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.run_allocation_service_with_http_info(resource_id, allocation_algorithm, async_req=True)
        >>> result = thread.get()

        :param resource_id: The List of Placement IDs for which you wish to allocate executions. (required)
        :type resource_id: List[ResourceId]
        :param allocation_algorithm: A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\".
        :type allocation_algorithm: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AllocationServiceRunResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'allocation_algorithm'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_allocation_service" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('allocation_algorithm') is not None:  # noqa: E501
            _query_params.append(('allocationAlgorithm', _params['allocation_algorithm']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['resource_id'] is not None:
            _body_params = _params['resource_id']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "AllocationServiceRunResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/ordermanagement/allocate', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
