from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.directory_object import DirectoryObject
    from .....models.o_data_errors.o_data_error import ODataError
    from .graph_application.graph_application_request_builder import GraphApplicationRequestBuilder
    from .graph_device.graph_device_request_builder import GraphDeviceRequestBuilder
    from .graph_group.graph_group_request_builder import GraphGroupRequestBuilder
    from .graph_org_contact.graph_org_contact_request_builder import GraphOrgContactRequestBuilder
    from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder
    from .graph_user.graph_user_request_builder import GraphUserRequestBuilder

class DirectoryObjectItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the membersWithLicenseErrors property of the microsoft.graph.group entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/membersWithLicenseErrors/{directoryObject%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DirectoryObjectItemRequestBuilderGetQueryParameters]] = None) -> Optional[DirectoryObject]:
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DirectoryObject]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.directory_object import DirectoryObject

        return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DirectoryObjectItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DirectoryObjectItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DirectoryObjectItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DirectoryObjectItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def graph_application(self) -> GraphApplicationRequestBuilder:
        """
        Casts the previous resource to application.
        """
        from .graph_application.graph_application_request_builder import GraphApplicationRequestBuilder

        return GraphApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_device(self) -> GraphDeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        from .graph_device.graph_device_request_builder import GraphDeviceRequestBuilder

        return GraphDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_group(self) -> GraphGroupRequestBuilder:
        """
        Casts the previous resource to group.
        """
        from .graph_group.graph_group_request_builder import GraphGroupRequestBuilder

        return GraphGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_org_contact(self) -> GraphOrgContactRequestBuilder:
        """
        Casts the previous resource to orgContact.
        """
        from .graph_org_contact.graph_org_contact_request_builder import GraphOrgContactRequestBuilder

        return GraphOrgContactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_service_principal(self) -> GraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder

        return GraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_user(self) -> GraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        from .graph_user.graph_user_request_builder import GraphUserRequestBuilder

        return GraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DirectoryObjectItemRequestBuilderGetQueryParameters():
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class DirectoryObjectItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DirectoryObjectItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

