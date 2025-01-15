from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .graph_app_role_assignment.graph_app_role_assignment_request_builder import GraphAppRoleAssignmentRequestBuilder
    from .graph_endpoint.graph_endpoint_request_builder import GraphEndpointRequestBuilder
    from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder
    from .graph_user.graph_user_request_builder import GraphUserRequestBuilder
    from .ref.ref_request_builder import RefRequestBuilder

class DirectoryObjectItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /devices/{device-id}/registeredOwners/{directoryObject-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/devices/{device%2Did}/registeredOwners/{directoryObject%2Did}", path_parameters)
    
    @property
    def graph_app_role_assignment(self) -> GraphAppRoleAssignmentRequestBuilder:
        """
        Casts the previous resource to appRoleAssignment.
        """
        from .graph_app_role_assignment.graph_app_role_assignment_request_builder import GraphAppRoleAssignmentRequestBuilder

        return GraphAppRoleAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_endpoint(self) -> GraphEndpointRequestBuilder:
        """
        Casts the previous resource to endpoint.
        """
        from .graph_endpoint.graph_endpoint_request_builder import GraphEndpointRequestBuilder

        return GraphEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @property
    def ref(self) -> RefRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        from .ref.ref_request_builder import RefRequestBuilder

        return RefRequestBuilder(self.request_adapter, self.path_parameters)
    

