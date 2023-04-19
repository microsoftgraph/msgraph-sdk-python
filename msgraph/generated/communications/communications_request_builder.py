from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import cloud_communications
    from ..models.o_data_errors import o_data_error
    from .call_records import call_records_request_builder
    from .calls import calls_request_builder
    from .get_presences_by_user_id import get_presences_by_user_id_request_builder
    from .online_meetings import online_meetings_request_builder
    from .presences import presences_request_builder

class CommunicationsRequestBuilder():
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CommunicationsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None) -> Optional[cloud_communications.CloudCommunications]:
        """
        Get communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_communications.CloudCommunications]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import cloud_communications

        return await self.request_adapter.send_async(request_info, cloud_communications.CloudCommunications, error_mapping)
    
    async def patch(self,body: Optional[cloud_communications.CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None) -> Optional[cloud_communications.CloudCommunications]:
        """
        Update communications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_communications.CloudCommunications]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import cloud_communications

        return await self.request_adapter.send_async(request_info, cloud_communications.CloudCommunications, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[cloud_communications.CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update communications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def call_records(self) -> call_records_request_builder.CallRecordsRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        """
        from .call_records import call_records_request_builder

        return call_records_request_builder.CallRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calls(self) -> calls_request_builder.CallsRequestBuilder:
        """
        Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
        """
        from .calls import calls_request_builder

        return calls_request_builder.CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_presences_by_user_id(self) -> get_presences_by_user_id_request_builder.GetPresencesByUserIdRequestBuilder:
        """
        Provides operations to call the getPresencesByUserId method.
        """
        from .get_presences_by_user_id import get_presences_by_user_id_request_builder

        return get_presences_by_user_id_request_builder.GetPresencesByUserIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> online_meetings_request_builder.OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.cloudCommunications entity.
        """
        from .online_meetings import online_meetings_request_builder

        return online_meetings_request_builder.OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presences(self) -> presences_request_builder.PresencesRequestBuilder:
        """
        Provides operations to manage the presences property of the microsoft.graph.cloudCommunications entity.
        """
        from .presences import presences_request_builder

        return presences_request_builder.PresencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CommunicationsRequestBuilderGetQueryParameters():
        """
        Get communications
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class CommunicationsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CommunicationsRequestBuilder.CommunicationsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CommunicationsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

