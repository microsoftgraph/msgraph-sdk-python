from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

call_records_request_builder = lazy_import('msgraph.generated.communications.call_records.call_records_request_builder')
call_record_item_request_builder = lazy_import('msgraph.generated.communications.call_records.item.call_record_item_request_builder')
calls_request_builder = lazy_import('msgraph.generated.communications.calls.calls_request_builder')
call_item_request_builder = lazy_import('msgraph.generated.communications.calls.item.call_item_request_builder')
get_presences_by_user_id_request_builder = lazy_import('msgraph.generated.communications.get_presences_by_user_id.get_presences_by_user_id_request_builder')
online_meetings_request_builder = lazy_import('msgraph.generated.communications.online_meetings.online_meetings_request_builder')
online_meeting_item_request_builder = lazy_import('msgraph.generated.communications.online_meetings.item.online_meeting_item_request_builder')
presences_request_builder = lazy_import('msgraph.generated.communications.presences.presences_request_builder')
presence_item_request_builder = lazy_import('msgraph.generated.communications.presences.item.presence_item_request_builder')
cloud_communications = lazy_import('msgraph.generated.models.cloud_communications')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CommunicationsRequestBuilder():
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    @property
    def call_records(self) -> call_records_request_builder.CallRecordsRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        """
        return call_records_request_builder.CallRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calls(self) -> calls_request_builder.CallsRequestBuilder:
        """
        Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
        """
        return calls_request_builder.CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_presences_by_user_id(self) -> get_presences_by_user_id_request_builder.GetPresencesByUserIdRequestBuilder:
        """
        Provides operations to call the getPresencesByUserId method.
        """
        return get_presences_by_user_id_request_builder.GetPresencesByUserIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> online_meetings_request_builder.OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.cloudCommunications entity.
        """
        return online_meetings_request_builder.OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presences(self) -> presences_request_builder.PresencesRequestBuilder:
        """
        Provides operations to manage the presences property of the microsoft.graph.cloudCommunications entity.
        """
        return presences_request_builder.PresencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def call_records_by_id(self,id: str) -> call_record_item_request_builder.CallRecordItemRequestBuilder:
        """
        Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
        Args:
            id: Unique identifier of the item
        Returns: call_record_item_request_builder.CallRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callRecord%2Did"] = id
        return call_record_item_request_builder.CallRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calls_by_id(self,id: str) -> call_item_request_builder.CallItemRequestBuilder:
        """
        Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
        Args:
            id: Unique identifier of the item
        Returns: call_item_request_builder.CallItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["call%2Did"] = id
        return call_item_request_builder.CallItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
    
    def create_get_request_information(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[cloud_communications.CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[CommunicationsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[cloud_communications.CloudCommunications]:
        """
        Get communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[cloud_communications.CloudCommunications]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, cloud_communications.CloudCommunications, response_handler, error_mapping)
    
    def online_meetings_by_id(self,id: str) -> online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.cloudCommunications entity.
        Args:
            id: Unique identifier of the item
        Returns: online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onlineMeeting%2Did"] = id
        return online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[cloud_communications.CloudCommunications] = None, request_configuration: Optional[CommunicationsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[cloud_communications.CloudCommunications]:
        """
        Update communications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[cloud_communications.CloudCommunications]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, cloud_communications.CloudCommunications, response_handler, error_mapping)
    
    def presences_by_id(self,id: str) -> presence_item_request_builder.PresenceItemRequestBuilder:
        """
        Provides operations to manage the presences property of the microsoft.graph.cloudCommunications entity.
        Args:
            id: Unique identifier of the item
        Returns: presence_item_request_builder.PresenceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["presence%2Did"] = id
        return presence_item_request_builder.PresenceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class CommunicationsRequestBuilderGetQueryParameters():
        """
        Get communications
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class CommunicationsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

