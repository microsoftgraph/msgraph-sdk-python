from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.call_records.call_record import CallRecord
    from ...models.call_records.call_record_collection_response import CallRecordCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.call_record_item_request_builder import CallRecordItemRequestBuilder
    from .microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder
    from .microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder

class CallRecordsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CallRecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/callRecords{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_call_record_id(self,call_record_id: str) -> CallRecordItemRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        param call_record_id: The unique identifier of callRecord
        Returns: CallRecordItemRequestBuilder
        """
        if call_record_id is None:
            raise TypeError("call_record_id cannot be null.")
        from .item.call_record_item_request_builder import CallRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callRecord%2Did"] = call_record_id
        return CallRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CallRecordsRequestBuilderGetQueryParameters]] = None) -> Optional[CallRecordCollectionResponse]:
        """
        Get the list of callRecord objects and their properties. The results can be optionally filtered using the $filter query parameter on the startDateTime and participant id properties. Note that the listed call records don't include expandable relationships such as sessions and participants_v2. You can expand these relationships using Get callRecord for a specific record.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecordCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/callrecords-cloudcommunications-list-callrecords?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.call_records.call_record_collection_response import CallRecordCollectionResponse

        return await self.request_adapter.send_async(request_info, CallRecordCollectionResponse, error_mapping)
    
    def microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time(self,from_date_time: datetime.datetime, to_date_time: datetime.datetime) -> MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getDirectRoutingCalls method.
        param from_date_time: Usage: fromDateTime={fromDateTime}
        param to_date_time: Usage: toDateTime={toDateTime}
        Returns: MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if from_date_time is None:
            raise TypeError("from_date_time cannot be null.")
        if to_date_time is None:
            raise TypeError("to_date_time cannot be null.")
        from .microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder

        return MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, from_date_time, to_date_time)
    
    def microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time(self,from_date_time: datetime.datetime, to_date_time: datetime.datetime) -> MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getPstnCalls method.
        param from_date_time: Usage: fromDateTime={fromDateTime}
        param to_date_time: Usage: toDateTime={toDateTime}
        Returns: MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if from_date_time is None:
            raise TypeError("from_date_time cannot be null.")
        if to_date_time is None:
            raise TypeError("to_date_time cannot be null.")
        from .microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder

        return MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, from_date_time, to_date_time)
    
    async def post(self,body: CallRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CallRecord]:
        """
        Create new navigation property to callRecords for communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecord]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.call_records.call_record import CallRecord

        return await self.request_adapter.send_async(request_info, CallRecord, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CallRecordsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the list of callRecord objects and their properties. The results can be optionally filtered using the $filter query parameter on the startDateTime and participant id properties. Note that the listed call records don't include expandable relationships such as sessions and participants_v2. You can expand these relationships using Get callRecord for a specific record.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CallRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to callRecords for communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CallRecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallRecordsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CallRecordsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CallRecordsRequestBuilderGetQueryParameters():
        """
        Get the list of callRecord objects and their properties. The results can be optionally filtered using the $filter query parameter on the startDateTime and participant id properties. Note that the listed call records don't include expandable relationships such as sessions and participants_v2. You can expand these relationships using Get callRecord for a specific record.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class CallRecordsRequestBuilderGetRequestConfiguration(RequestConfiguration[CallRecordsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CallRecordsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

