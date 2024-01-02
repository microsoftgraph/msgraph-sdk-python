from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CallRecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/callRecords{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_call_record_id(self,call_record_id: str) -> CallRecordItemRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        param call_record_id: The unique identifier of callRecord
        Returns: CallRecordItemRequestBuilder
        """
        if not call_record_id:
            raise TypeError("call_record_id cannot be null.")
        from .item.call_record_item_request_builder import CallRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callRecord%2Did"] = call_record_id
        return CallRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[CallRecordsRequestBuilderGetRequestConfiguration] = None) -> Optional[CallRecordCollectionResponse]:
        """
        Retrieve the properties and relationships of a callRecord object. There are two ways to get the id of a callRecord: You can use the $expand query parameter to optionally include session and segment details, as shown in the Get full details example. When you expand session details, the maximum page size is 60 sessions.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecordCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.call_records.call_record_collection_response import CallRecordCollectionResponse

        return await self.request_adapter.send_async(request_info, CallRecordCollectionResponse, error_mapping)
    
    def microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time(self,from_date_time: Optional[datetime.datetime] = None, to_date_time: Optional[datetime.datetime] = None) -> MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getDirectRoutingCalls method.
        param from_date_time: Usage: fromDateTime={fromDateTime}
        param to_date_time: Usage: toDateTime={toDateTime}
        Returns: MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if not from_date_time:
            raise TypeError("from_date_time cannot be null.")
        if not to_date_time:
            raise TypeError("to_date_time cannot be null.")
        from .microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder

        return MicrosoftGraphCallRecordsGetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, from_date_time, to_date_time)
    
    def microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time(self,from_date_time: Optional[datetime.datetime] = None, to_date_time: Optional[datetime.datetime] = None) -> MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getPstnCalls method.
        param from_date_time: Usage: fromDateTime={fromDateTime}
        param to_date_time: Usage: toDateTime={toDateTime}
        Returns: MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if not from_date_time:
            raise TypeError("from_date_time cannot be null.")
        if not to_date_time:
            raise TypeError("to_date_time cannot be null.")
        from .microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time.microsoft_graph_call_records_get_pstn_calls_with_from_date_time_with_to_date_time_request_builder import MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder

        return MicrosoftGraphCallRecordsGetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, from_date_time, to_date_time)
    
    async def post(self,body: Optional[CallRecord] = None, request_configuration: Optional[CallRecordsRequestBuilderPostRequestConfiguration] = None) -> Optional[CallRecord]:
        """
        Create new navigation property to callRecords for communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecord]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.call_records.call_record import CallRecord

        return await self.request_adapter.send_async(request_info, CallRecord, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[CallRecordsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a callRecord object. There are two ways to get the id of a callRecord: You can use the $expand query parameter to optionally include session and segment details, as shown in the Get full details example. When you expand session details, the maximum page size is 60 sessions.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[CallRecord] = None, request_configuration: Optional[CallRecordsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to callRecords for communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CallRecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallRecordsRequestBuilder
        """
        if not raw_url:
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
        Retrieve the properties and relationships of a callRecord object. There are two ways to get the id of a callRecord: You can use the $expand query parameter to optionally include session and segment details, as shown in the Get full details example. When you expand session details, the maximum page size is 60 sessions.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CallRecordsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CallRecordsRequestBuilder.CallRecordsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CallRecordsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

