from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.application.application_request_builder')
device_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.device.device_request_builder')
group_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.group.group_request_builder')
org_contact_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.org_contact.org_contact_request_builder')
ref_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.ref.ref_request_builder')
service_principal_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.service_principal.service_principal_request_builder')
user_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.members.item.user.user_request_builder')

class DirectoryObjectItemRequestBuilder():
    """
    Builds and executes requests for operations under /directory/administrativeUnits/{administrativeUnit-id}/members/{directoryObject-id}
    """
    @property
    def application(self) -> application_request_builder.ApplicationRequestBuilder:
        """
        Casts the previous resource to application.
        """
        return application_request_builder.ApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device(self) -> device_request_builder.DeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        return device_request_builder.DeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> group_request_builder.GroupRequestBuilder:
        """
        Casts the previous resource to group.
        """
        return group_request_builder.GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def org_contact(self) -> org_contact_request_builder.OrgContactRequestBuilder:
        """
        Casts the previous resource to orgContact.
        """
        return org_contact_request_builder.OrgContactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of directory entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal(self) -> service_principal_request_builder.ServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        return service_principal_request_builder.ServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user(self) -> user_request_builder.UserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        return user_request_builder.UserRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

