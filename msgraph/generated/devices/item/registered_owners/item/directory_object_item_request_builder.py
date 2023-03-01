from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

graph_app_role_assignment_request_builder = lazy_import('msgraph.generated.devices.item.registered_owners.item.graph_app_role_assignment.graph_app_role_assignment_request_builder')
graph_endpoint_request_builder = lazy_import('msgraph.generated.devices.item.registered_owners.item.graph_endpoint.graph_endpoint_request_builder')
graph_service_principal_request_builder = lazy_import('msgraph.generated.devices.item.registered_owners.item.graph_service_principal.graph_service_principal_request_builder')
graph_user_request_builder = lazy_import('msgraph.generated.devices.item.registered_owners.item.graph_user.graph_user_request_builder')
ref_request_builder = lazy_import('msgraph.generated.devices.item.registered_owners.item.ref.ref_request_builder')

class DirectoryObjectItemRequestBuilder():
    """
    Builds and executes requests for operations under /devices/{device-id}/registeredOwners/{directoryObject-id}
    """
    @property
    def graph_app_role_assignment(self) -> graph_app_role_assignment_request_builder.GraphAppRoleAssignmentRequestBuilder:
        """
        Casts the previous resource to appRoleAssignment.
        """
        return graph_app_role_assignment_request_builder.GraphAppRoleAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_endpoint(self) -> graph_endpoint_request_builder.GraphEndpointRequestBuilder:
        """
        Casts the previous resource to endpoint.
        """
        return graph_endpoint_request_builder.GraphEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_service_principal(self) -> graph_service_principal_request_builder.GraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        return graph_service_principal_request_builder.GraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_user(self) -> graph_user_request_builder.GraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        return graph_user_request_builder.GraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/devices/{device%2Did}/registeredOwners/{directoryObject%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    

