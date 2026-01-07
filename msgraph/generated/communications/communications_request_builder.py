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
    from ..models.cloud_communications import CloudCommunications
    from ..models.o_data_errors.o_data_error import ODataError
    from .adhoc_calls.adhoc_calls_request_builder import AdhocCallsRequestBuilder
    from .calls.calls_request_builder import CallsRequestBuilder
    from .call_records.call_records_request_builder import CallRecordsRequestBuilder
    from .get_all_online_meeting_messages.get_all_online_meeting_messages_request_builder import GetAllOnlineMeetingMessagesRequestBuilder
    from .get_presences_by_user_id.get_presences_by_user_id_request_builder import GetPresencesByUserIdRequestBuilder
    from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder
    from .online_meeting_conversations.online_meeting_conversations_request_builder import OnlineMeetingConversationsRequestBuilder
    from .presences.presences_request_builder import PresencesRequestBuilder

class CommunicationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CommunicationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CommunicationsRequestBuilderGetQueryParameters]] = None) -> Optional[CloudCommunications]:
        """
        Get communications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudCommunications]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.cloud_communications import CloudCommunications

        return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)
    
    async def patch(self,body: CloudCommunications, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CloudCommunications]:
        """
        Update communications
        param body: Represents a container that exposes navigation properties for cloud communications resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudCommunications]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.cloud_communications import CloudCommunications

        return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CommunicationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get communications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CloudCommunications, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update communications
        param body: Represents a container that exposes navigation properties for cloud communications resources.
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
    
    def with_url(self,raw_url: str) -> CommunicationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CommunicationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CommunicationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def adhoc_calls(self) -> AdhocCallsRequestBuilder:
        """
        Provides operations to manage the adhocCalls property of the microsoft.graph.cloudCommunications entity.
        """
        from .adhoc_calls.adhoc_calls_request_builder import AdhocCallsRequestBuilder

        return AdhocCallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def call_records(self) -> CallRecordsRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        """
        from .call_records.call_records_request_builder import CallRecordsRequestBuilder

        return CallRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calls(self) -> CallsRequestBuilder:
        """
        Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
        """
        from .calls.calls_request_builder import CallsRequestBuilder

        return CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_all_online_meeting_messages(self) -> GetAllOnlineMeetingMessagesRequestBuilder:
        """
        Provides operations to call the getAllOnlineMeetingMessages method.
        """
        from .get_all_online_meeting_messages.get_all_online_meeting_messages_request_builder import GetAllOnlineMeetingMessagesRequestBuilder

        return GetAllOnlineMeetingMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_presences_by_user_id(self) -> GetPresencesByUserIdRequestBuilder:
        """
        Provides operations to call the getPresencesByUserId method.
        """
        from .get_presences_by_user_id.get_presences_by_user_id_request_builder import GetPresencesByUserIdRequestBuilder

        return GetPresencesByUserIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meeting_conversations(self) -> OnlineMeetingConversationsRequestBuilder:
        """
        Provides operations to manage the onlineMeetingConversations property of the microsoft.graph.cloudCommunications entity.
        """
        from .online_meeting_conversations.online_meeting_conversations_request_builder import OnlineMeetingConversationsRequestBuilder

        return OnlineMeetingConversationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.cloudCommunications entity.
        """
        from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder

        return OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presences(self) -> PresencesRequestBuilder:
        """
        Provides operations to manage the presences property of the microsoft.graph.cloudCommunications entity.
        """
        from .presences.presences_request_builder import PresencesRequestBuilder

        return PresencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CommunicationsRequestBuilderGetQueryParameters():
        """
        Get communications
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
    class CommunicationsRequestBuilderGetRequestConfiguration(RequestConfiguration[CommunicationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CommunicationsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

