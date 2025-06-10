from __future__ import annotations
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
    from ....models.call_records.call_record import CallRecord
    from ....models.o_data_errors.o_data_error import ODataError
    from .organizer_v2.organizer_v2_request_builder import Organizer_v2RequestBuilder
    from .participants_v2.participants_v2_request_builder import Participants_v2RequestBuilder
    from .sessions.sessions_request_builder import SessionsRequestBuilder

class CallRecordItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CallRecordItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/callRecords/{callRecord%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property callRecords for communications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CallRecordItemRequestBuilderGetQueryParameters]] = None) -> Optional[CallRecord]:
        """
        Retrieve the properties and relationships of a callRecord object. You can get the id of a callRecord in two ways:* Subscribe to change notifications to the /communications/callRecords endpoint.* Use the callChainId property of a call. The call record is available only after the associated call is completed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecord]
        Find more info here: https://learn.microsoft.com/graph/api/callrecords-callrecord-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.call_records.call_record import CallRecord

        return await self.request_adapter.send_async(request_info, CallRecord, error_mapping)
    
    async def patch(self,body: CallRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CallRecord]:
        """
        Update the navigation property callRecords in communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallRecord]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.call_records.call_record import CallRecord

        return await self.request_adapter.send_async(request_info, CallRecord, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property callRecords for communications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CallRecordItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a callRecord object. You can get the id of a callRecord in two ways:* Subscribe to change notifications to the /communications/callRecords endpoint.* Use the callChainId property of a call. The call record is available only after the associated call is completed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CallRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property callRecords in communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CallRecordItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallRecordItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CallRecordItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def organizer_v2(self) -> Organizer_v2RequestBuilder:
        """
        Provides operations to manage the organizer_v2 property of the microsoft.graph.callRecords.callRecord entity.
        """
        from .organizer_v2.organizer_v2_request_builder import Organizer_v2RequestBuilder

        return Organizer_v2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def participants_v2(self) -> Participants_v2RequestBuilder:
        """
        Provides operations to manage the participants_v2 property of the microsoft.graph.callRecords.callRecord entity.
        """
        from .participants_v2.participants_v2_request_builder import Participants_v2RequestBuilder

        return Participants_v2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sessions(self) -> SessionsRequestBuilder:
        """
        Provides operations to manage the sessions property of the microsoft.graph.callRecords.callRecord entity.
        """
        from .sessions.sessions_request_builder import SessionsRequestBuilder

        return SessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CallRecordItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CallRecordItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a callRecord object. You can get the id of a callRecord in two ways:* Subscribe to change notifications to the /communications/callRecords endpoint.* Use the callChainId property of a call. The call record is available only after the associated call is completed.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class CallRecordItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CallRecordItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CallRecordItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

