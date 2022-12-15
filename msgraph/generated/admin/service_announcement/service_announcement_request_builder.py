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

health_overviews_request_builder = lazy_import('msgraph.generated.admin.service_announcement.health_overviews.health_overviews_request_builder')
service_health_item_request_builder = lazy_import('msgraph.generated.admin.service_announcement.health_overviews.item.service_health_item_request_builder')
issues_request_builder = lazy_import('msgraph.generated.admin.service_announcement.issues.issues_request_builder')
service_health_issue_item_request_builder = lazy_import('msgraph.generated.admin.service_announcement.issues.item.service_health_issue_item_request_builder')
messages_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.messages_request_builder')
service_update_message_item_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.item.service_update_message_item_request_builder')
service_announcement = lazy_import('msgraph.generated.models.service_announcement')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ServiceAnnouncementRequestBuilder():
    """
    Provides operations to manage the serviceAnnouncement property of the microsoft.graph.admin entity.
    """
    @property
    def health_overviews(self) -> health_overviews_request_builder.HealthOverviewsRequestBuilder:
        """
        Provides operations to manage the healthOverviews property of the microsoft.graph.serviceAnnouncement entity.
        """
        return health_overviews_request_builder.HealthOverviewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def issues(self) -> issues_request_builder.IssuesRequestBuilder:
        """
        Provides operations to manage the issues property of the microsoft.graph.serviceAnnouncement entity.
        """
        return issues_request_builder.IssuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.serviceAnnouncement entity.
        """
        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ServiceAnnouncementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/serviceAnnouncement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ServiceAnnouncementRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property serviceAnnouncement for admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[ServiceAnnouncementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A container for service communications resources. Read-only.
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
    
    def create_patch_request_information(self,body: Optional[service_announcement.ServiceAnnouncement] = None, request_configuration: Optional[ServiceAnnouncementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property serviceAnnouncement in admin
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
    
    async def delete(self,request_configuration: Optional[ServiceAnnouncementRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property serviceAnnouncement for admin
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[ServiceAnnouncementRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[service_announcement.ServiceAnnouncement]:
        """
        A container for service communications resources. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[service_announcement.ServiceAnnouncement]
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
        return await self.request_adapter.send_async(request_info, service_announcement.ServiceAnnouncement, response_handler, error_mapping)
    
    def health_overviews_by_id(self,id: str) -> service_health_item_request_builder.ServiceHealthItemRequestBuilder:
        """
        Provides operations to manage the healthOverviews property of the microsoft.graph.serviceAnnouncement entity.
        Args:
            id: Unique identifier of the item
        Returns: service_health_item_request_builder.ServiceHealthItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["serviceHealth%2Did"] = id
        return service_health_item_request_builder.ServiceHealthItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def issues_by_id(self,id: str) -> service_health_issue_item_request_builder.ServiceHealthIssueItemRequestBuilder:
        """
        Provides operations to manage the issues property of the microsoft.graph.serviceAnnouncement entity.
        Args:
            id: Unique identifier of the item
        Returns: service_health_issue_item_request_builder.ServiceHealthIssueItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["serviceHealthIssue%2Did"] = id
        return service_health_issue_item_request_builder.ServiceHealthIssueItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def messages_by_id(self,id: str) -> service_update_message_item_request_builder.ServiceUpdateMessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.serviceAnnouncement entity.
        Args:
            id: Unique identifier of the item
        Returns: service_update_message_item_request_builder.ServiceUpdateMessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["serviceUpdateMessage%2Did"] = id
        return service_update_message_item_request_builder.ServiceUpdateMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[service_announcement.ServiceAnnouncement] = None, request_configuration: Optional[ServiceAnnouncementRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[service_announcement.ServiceAnnouncement]:
        """
        Update the navigation property serviceAnnouncement in admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[service_announcement.ServiceAnnouncement]
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
        return await self.request_adapter.send_async(request_info, service_announcement.ServiceAnnouncement, response_handler, error_mapping)
    
    @dataclass
    class ServiceAnnouncementRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ServiceAnnouncementRequestBuilderGetQueryParameters():
        """
        A container for service communications resources. Read-only.
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
    class ServiceAnnouncementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ServiceAnnouncementRequestBuilder.ServiceAnnouncementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ServiceAnnouncementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

