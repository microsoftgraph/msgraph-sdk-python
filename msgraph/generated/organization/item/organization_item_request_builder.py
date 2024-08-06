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
    from ...models.organization import Organization
    from ...models.o_data_errors.o_data_error import ODataError
    from .branding.branding_request_builder import BrandingRequestBuilder
    from .certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder import CertificateBasedAuthConfigurationRequestBuilder
    from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder
    from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder
    from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .set_mobile_device_management_authority.set_mobile_device_management_authority_request_builder import SetMobileDeviceManagementAuthorityRequestBuilder

class OrganizationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of organization entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete entity from organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OrganizationItemRequestBuilderGetQueryParameters]] = None) -> Optional[Organization]:
        """
        Read properties and relationships of the organization object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Organization]
        Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-organization-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.organization import Organization

        return await self.request_adapter.send_async(request_info, Organization, error_mapping)
    
    async def patch(self,body: Organization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Organization]:
        """
        Update the properties of the currently authenticated organization. In this case, organization is defined as a collection of exactly one record, and so its ID must be specified in the request.  The ID is also known as the tenantId of the organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Organization]
        Find more info here: https://learn.microsoft.com/graph/api/organization-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.organization import Organization

        return await self.request_adapter.send_async(request_info, Organization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete entity from organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OrganizationItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read properties and relationships of the organization object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Organization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of the currently authenticated organization. In this case, organization is defined as a collection of exactly one record, and so its ID must be specified in the request.  The ID is also known as the tenantId of the organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> OrganizationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrganizationItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OrganizationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def branding(self) -> BrandingRequestBuilder:
        """
        Provides operations to manage the branding property of the microsoft.graph.organization entity.
        """
        from .branding.branding_request_builder import BrandingRequestBuilder

        return BrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_based_auth_configuration(self) -> CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the certificateBasedAuthConfiguration property of the microsoft.graph.organization entity.
        """
        from .certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder import CertificateBasedAuthConfigurationRequestBuilder

        return CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder

        return CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder

        return CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.organization entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder

        return GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder

        return GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_mobile_device_management_authority(self) -> SetMobileDeviceManagementAuthorityRequestBuilder:
        """
        Provides operations to call the setMobileDeviceManagementAuthority method.
        """
        from .set_mobile_device_management_authority.set_mobile_device_management_authority_request_builder import SetMobileDeviceManagementAuthorityRequestBuilder

        return SetMobileDeviceManagementAuthorityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OrganizationItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrganizationItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the organization object.
        """
        def get_query_parameter(self,original_name: str) -> str:
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

    
    @dataclass
    class OrganizationItemRequestBuilderGetRequestConfiguration(RequestConfiguration[OrganizationItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrganizationItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

