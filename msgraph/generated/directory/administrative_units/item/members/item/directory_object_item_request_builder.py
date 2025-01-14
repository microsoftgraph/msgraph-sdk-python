from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .graph_application.graph_application_request_builder import GraphApplicationRequestBuilder
    from .graph_device.graph_device_request_builder import GraphDeviceRequestBuilder
    from .graph_group.graph_group_request_builder import GraphGroupRequestBuilder
    from .graph_org_contact.graph_org_contact_request_builder import GraphOrgContactRequestBuilder
    from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder
    from .graph_user.graph_user_request_builder import GraphUserRequestBuilder
    from .ref.ref_request_builder import RefRequestBuilder

class DirectoryObjectItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /directory/administrativeUnits/{administrativeUnit-id}/members/{directoryObject-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/administrativeUnits/{administrativeUnit%2Did}/members/{directoryObject%2Did}", path_parameters)
    
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
    
    @property
    def ref(self) -> RefRequestBuilder:
        """
        Provides operations to manage the collection of directory entities.
        """
        from .ref.ref_request_builder import RefRequestBuilder

        return RefRequestBuilder(self.request_adapter, self.path_parameters)
    

