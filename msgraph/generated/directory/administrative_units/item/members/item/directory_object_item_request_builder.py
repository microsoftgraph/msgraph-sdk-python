from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

microsoft_graph_application_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_application.microsoft_graph_application_request_builder')
microsoft_graph_device_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_device.microsoft_graph_device_request_builder')
microsoft_graph_group_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_group.microsoft_graph_group_request_builder')
microsoft_graph_org_contact_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_org_contact.microsoft_graph_org_contact_request_builder')
microsoft_graph_service_principal_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_service_principal.microsoft_graph_service_principal_request_builder')
microsoft_graph_user_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.microsoft_graph_user.microsoft_graph_user_request_builder')
ref_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.ref.ref_request_builder')

class DirectoryObjectItemRequestBuilder():
    """
    Builds and executes requests for operations under /directory/administrativeUnits/{administrativeUnit-id}/members/{directoryObject-id}
    """
    @property
    def microsoft_graph_application(self) -> microsoft_graph_application_request_builder.MicrosoftGraphApplicationRequestBuilder:
        """
        Casts the previous resource to application.
        """
        return microsoft_graph_application_request_builder.MicrosoftGraphApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_device(self) -> microsoft_graph_device_request_builder.MicrosoftGraphDeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        return microsoft_graph_device_request_builder.MicrosoftGraphDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_group(self) -> microsoft_graph_group_request_builder.MicrosoftGraphGroupRequestBuilder:
        """
        Casts the previous resource to group.
        """
        return microsoft_graph_group_request_builder.MicrosoftGraphGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_org_contact(self) -> microsoft_graph_org_contact_request_builder.MicrosoftGraphOrgContactRequestBuilder:
        """
        Casts the previous resource to orgContact.
        """
        return microsoft_graph_org_contact_request_builder.MicrosoftGraphOrgContactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_service_principal(self) -> microsoft_graph_service_principal_request_builder.MicrosoftGraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        return microsoft_graph_service_principal_request_builder.MicrosoftGraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_user(self) -> microsoft_graph_user_request_builder.MicrosoftGraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        return microsoft_graph_user_request_builder.MicrosoftGraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of directory entities.
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
        self.url_template: str = "{+baseurl}/directory/administrativeUnits/{administrativeUnit%2Did}/members/{directoryObject%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    

