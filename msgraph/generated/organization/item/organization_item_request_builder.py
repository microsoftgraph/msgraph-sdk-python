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

organization = lazy_import('msgraph.generated.models.organization')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
branding_request_builder = lazy_import('msgraph.generated.organization.item.branding.branding_request_builder')
certificate_based_auth_configuration_request_builder = lazy_import('msgraph.generated.organization.item.certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder')
certificate_based_auth_configuration_item_request_builder = lazy_import('msgraph.generated.organization.item.certificate_based_auth_configuration.item.certificate_based_auth_configuration_item_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.organization.item.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.organization.item.extensions.item.extension_item_request_builder')
microsoft_graph_check_member_groups_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_check_member_groups.microsoft_graph_check_member_groups_request_builder')
microsoft_graph_check_member_objects_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_check_member_objects.microsoft_graph_check_member_objects_request_builder')
microsoft_graph_get_member_groups_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_get_member_groups.microsoft_graph_get_member_groups_request_builder')
microsoft_graph_get_member_objects_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_get_member_objects.microsoft_graph_get_member_objects_request_builder')
microsoft_graph_restore_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_restore.microsoft_graph_restore_request_builder')
microsoft_graph_set_mobile_device_management_authority_request_builder = lazy_import('msgraph.generated.organization.item.microsoft_graph_set_mobile_device_management_authority.microsoft_graph_set_mobile_device_management_authority_request_builder')

class OrganizationItemRequestBuilder():
    """
    Provides operations to manage the collection of organization entities.
    """
    @property
    def branding(self) -> branding_request_builder.BrandingRequestBuilder:
        """
        Provides operations to manage the branding property of the microsoft.graph.organization entity.
        """
        return branding_request_builder.BrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_based_auth_configuration(self) -> certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the certificateBasedAuthConfiguration property of the microsoft.graph.organization entity.
        """
        return certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.organization entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_check_member_groups(self) -> microsoft_graph_check_member_groups_request_builder.MicrosoftGraphCheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        return microsoft_graph_check_member_groups_request_builder.MicrosoftGraphCheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_check_member_objects(self) -> microsoft_graph_check_member_objects_request_builder.MicrosoftGraphCheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        return microsoft_graph_check_member_objects_request_builder.MicrosoftGraphCheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_member_groups(self) -> microsoft_graph_get_member_groups_request_builder.MicrosoftGraphGetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        return microsoft_graph_get_member_groups_request_builder.MicrosoftGraphGetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_member_objects(self) -> microsoft_graph_get_member_objects_request_builder.MicrosoftGraphGetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        return microsoft_graph_get_member_objects_request_builder.MicrosoftGraphGetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_restore(self) -> microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_set_mobile_device_management_authority(self) -> microsoft_graph_set_mobile_device_management_authority_request_builder.MicrosoftGraphSetMobileDeviceManagementAuthorityRequestBuilder:
        """
        Provides operations to call the setMobileDeviceManagementAuthority method.
        """
        return microsoft_graph_set_mobile_device_management_authority_request_builder.MicrosoftGraphSetMobileDeviceManagementAuthorityRequestBuilder(self.request_adapter, self.path_parameters)
    
    def certificate_based_auth_configuration_by_id(self,id: str) -> certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder:
        """
        Provides operations to manage the certificateBasedAuthConfiguration property of the microsoft.graph.organization entity.
        Args:
            id: Unique identifier of the item
        Returns: certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["certificateBasedAuthConfiguration%2Did"] = id
        return certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OrganizationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/organization/{organization%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[OrganizationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from organization
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.organization entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[OrganizationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[organization.Organization]:
        """
        Get the properties and relationships of the currently authenticated organization. Since the **organization** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in an **organization** instance.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organization.Organization]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, organization.Organization, error_mapping)
    
    async def patch(self,body: Optional[organization.Organization] = None, request_configuration: Optional[OrganizationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[organization.Organization]:
        """
        Update the properties of the currently authenticated organization. In this case, `organization` is defined as a collection of exactly one record, and so its **ID** must be specified in the request.  The **ID** is also known as the **tenantId** of the organization.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organization.Organization]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, organization.Organization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OrganizationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from organization
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
    
    def to_get_request_information(self,request_configuration: Optional[OrganizationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of the currently authenticated organization. Since the **organization** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in an **organization** instance.
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
    
    def to_patch_request_information(self,body: Optional[organization.Organization] = None, request_configuration: Optional[OrganizationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of the currently authenticated organization. In this case, `organization` is defined as a collection of exactly one record, and so its **ID** must be specified in the request.  The **ID** is also known as the **tenantId** of the organization.
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
    
    @dataclass
    class OrganizationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OrganizationItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of the currently authenticated organization. Since the **organization** resource supports extensions, you can also use the `GET` operation to get custom properties and extension data in an **organization** instance.
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
    class OrganizationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OrganizationItemRequestBuilder.OrganizationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OrganizationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

