from __future__ import annotations
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
    from ..models.cloud_communications import CloudCommunications
    from ..models.o_data_errors.o_data_error import ODataError
    from .calls.calls_request_builder import CallsRequestBuilder
    from .call_records.call_records_request_builder import CallRecordsRequestBuilder
    from .get_presences_by_user_id.get_presences_by_user_id_request_builder import GetPresencesByUserIdRequestBuilder
    from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder
    from .presences.presences_request_builder import PresencesRequestBuilder

class CommunicationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CommunicationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudCommunications]:
        """
        Get communications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudCommunications]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.cloud_communications import CloudCommunications

        return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)
    
    async def patch(self,body: Optional[CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None) -> Optional[CloudCommunications]:
        """
        Update communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudCommunications]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.cloud_communications import CloudCommunications

        return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get communications
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
    
    def to_patch_request_information(self,body: Optional[CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update communications
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CommunicationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CommunicationsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CommunicationsRequestBuilder(self.request_adapter, raw_url)
    
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
    def get_presences_by_user_id(self) -> GetPresencesByUserIdRequestBuilder:
        """
        Provides operations to call the getPresencesByUserId method.
        """
        from .get_presences_by_user_id.get_presences_by_user_id_request_builder import GetPresencesByUserIdRequestBuilder

        return GetPresencesByUserIdRequestBuilder(self.request_adapter, self.path_parameters)
    
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
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CommunicationsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CommunicationsRequestBuilder.CommunicationsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CommunicationsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

