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

add_key_request_builder = lazy_import('msgraph.generated.applications.item.add_key.add_key_request_builder')
add_password_request_builder = lazy_import('msgraph.generated.applications.item.add_password.add_password_request_builder')
check_member_groups_request_builder = lazy_import('msgraph.generated.applications.item.check_member_groups.check_member_groups_request_builder')
check_member_objects_request_builder = lazy_import('msgraph.generated.applications.item.check_member_objects.check_member_objects_request_builder')
created_on_behalf_of_request_builder = lazy_import('msgraph.generated.applications.item.created_on_behalf_of.created_on_behalf_of_request_builder')
extension_properties_request_builder = lazy_import('msgraph.generated.applications.item.extension_properties.extension_properties_request_builder')
extension_property_item_request_builder = lazy_import('msgraph.generated.applications.item.extension_properties.item.extension_property_item_request_builder')
federated_identity_credentials_request_builder = lazy_import('msgraph.generated.applications.item.federated_identity_credentials.federated_identity_credentials_request_builder')
federated_identity_credential_item_request_builder = lazy_import('msgraph.generated.applications.item.federated_identity_credentials.item.federated_identity_credential_item_request_builder')
get_member_groups_request_builder = lazy_import('msgraph.generated.applications.item.get_member_groups.get_member_groups_request_builder')
get_member_objects_request_builder = lazy_import('msgraph.generated.applications.item.get_member_objects.get_member_objects_request_builder')
home_realm_discovery_policies_request_builder = lazy_import('msgraph.generated.applications.item.home_realm_discovery_policies.home_realm_discovery_policies_request_builder')
home_realm_discovery_policy_item_request_builder = lazy_import('msgraph.generated.applications.item.home_realm_discovery_policies.item.home_realm_discovery_policy_item_request_builder')
logo_request_builder = lazy_import('msgraph.generated.applications.item.logo.logo_request_builder')
owners_request_builder = lazy_import('msgraph.generated.applications.item.owners.owners_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.applications.item.owners.item.directory_object_item_request_builder')
remove_key_request_builder = lazy_import('msgraph.generated.applications.item.remove_key.remove_key_request_builder')
remove_password_request_builder = lazy_import('msgraph.generated.applications.item.remove_password.remove_password_request_builder')
restore_request_builder = lazy_import('msgraph.generated.applications.item.restore.restore_request_builder')
set_verified_publisher_request_builder = lazy_import('msgraph.generated.applications.item.set_verified_publisher.set_verified_publisher_request_builder')
token_issuance_policies_request_builder = lazy_import('msgraph.generated.applications.item.token_issuance_policies.token_issuance_policies_request_builder')
token_issuance_policy_item_request_builder = lazy_import('msgraph.generated.applications.item.token_issuance_policies.item.token_issuance_policy_item_request_builder')
token_lifetime_policies_request_builder = lazy_import('msgraph.generated.applications.item.token_lifetime_policies.token_lifetime_policies_request_builder')
token_lifetime_policy_item_request_builder = lazy_import('msgraph.generated.applications.item.token_lifetime_policies.item.token_lifetime_policy_item_request_builder')
unset_verified_publisher_request_builder = lazy_import('msgraph.generated.applications.item.unset_verified_publisher.unset_verified_publisher_request_builder')
application = lazy_import('msgraph.generated.models.application')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ApplicationItemRequestBuilder():
    """
    Provides operations to manage the collection of application entities.
    """
    def add_key(self) -> add_key_request_builder.AddKeyRequestBuilder:
        """
        Provides operations to call the addKey method.
        """
        return add_key_request_builder.AddKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def add_password(self) -> add_password_request_builder.AddPasswordRequestBuilder:
        """
        Provides operations to call the addPassword method.
        """
        return add_password_request_builder.AddPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def created_on_behalf_of(self) -> created_on_behalf_of_request_builder.CreatedOnBehalfOfRequestBuilder:
        """
        Provides operations to manage the createdOnBehalfOf property of the microsoft.graph.application entity.
        """
        return created_on_behalf_of_request_builder.CreatedOnBehalfOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    def extension_properties(self) -> extension_properties_request_builder.ExtensionPropertiesRequestBuilder:
        """
        Provides operations to manage the extensionProperties property of the microsoft.graph.application entity.
        """
        return extension_properties_request_builder.ExtensionPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def federated_identity_credentials(self) -> federated_identity_credentials_request_builder.FederatedIdentityCredentialsRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.application entity.
        """
        return federated_identity_credentials_request_builder.FederatedIdentityCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def home_realm_discovery_policies(self) -> home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.application entity.
        """
        return home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def logo(self) -> logo_request_builder.LogoRequestBuilder:
        """
        Provides operations to manage the media for the application entity.
        """
        return logo_request_builder.LogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    def owners(self) -> owners_request_builder.OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.application entity.
        """
        return owners_request_builder.OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def remove_key(self) -> remove_key_request_builder.RemoveKeyRequestBuilder:
        """
        Provides operations to call the removeKey method.
        """
        return remove_key_request_builder.RemoveKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def remove_password(self) -> remove_password_request_builder.RemovePasswordRequestBuilder:
        """
        Provides operations to call the removePassword method.
        """
        return remove_password_request_builder.RemovePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    def set_verified_publisher(self) -> set_verified_publisher_request_builder.SetVerifiedPublisherRequestBuilder:
        """
        Provides operations to call the setVerifiedPublisher method.
        """
        return set_verified_publisher_request_builder.SetVerifiedPublisherRequestBuilder(self.request_adapter, self.path_parameters)
    
    def token_issuance_policies(self) -> token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.application entity.
        """
        return token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def token_lifetime_policies(self) -> token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.application entity.
        """
        return token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def unset_verified_publisher(self) -> unset_verified_publisher_request_builder.UnsetVerifiedPublisherRequestBuilder:
        """
        Provides operations to call the unsetVerifiedPublisher method.
        """
        return unset_verified_publisher_request_builder.UnsetVerifiedPublisherRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ApplicationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ApplicationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted.
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
    
    def create_get_request_information(self,request_configuration: Optional[ApplicationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of an application object.
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
    
    def create_patch_request_information(self,body: Optional[application.Application] = None, request_configuration: Optional[ApplicationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an application object.
        Args:
            body: 
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
    
    async def delete(self,request_configuration: Optional[ApplicationItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted.
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
    
    def extension_properties_by_id(self,id: str) -> extension_property_item_request_builder.ExtensionPropertyItemRequestBuilder:
        """
        Provides operations to manage the extensionProperties property of the microsoft.graph.application entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_property_item_request_builder.ExtensionPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extensionProperty%2Did"] = id
        return extension_property_item_request_builder.ExtensionPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def federated_identity_credentials_by_id(self,id: str) -> federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.application entity.
        Args:
            id: Unique identifier of the item
        Returns: federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["federatedIdentityCredential%2Did"] = id
        return federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ApplicationItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[application.Application]:
        """
        Get the properties and relationships of an application object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[application.Application]
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
        return await self.request_adapter.send_async(request_info, application.Application, response_handler, error_mapping)
    
    def home_realm_discovery_policies_by_id(self,id: str) -> home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.application entity.
        Args:
            id: Unique identifier of the item
        Returns: home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["homeRealmDiscoveryPolicy%2Did"] = id
        return home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owners_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.applications.item.owners.item collection
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[application.Application] = None, request_configuration: Optional[ApplicationItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[application.Application]:
        """
        Update the properties of an application object.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[application.Application]
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
        return await self.request_adapter.send_async(request_info, application.Application, response_handler, error_mapping)
    
    def token_issuance_policies_by_id(self,id: str) -> token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.applications.item.tokenIssuancePolicies.item collection
        Args:
            id: Unique identifier of the item
        Returns: token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenIssuancePolicy%2Did"] = id
        return token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def token_lifetime_policies_by_id(self,id: str) -> token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.applications.item.tokenLifetimePolicies.item collection
        Args:
            id: Unique identifier of the item
        Returns: token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenLifetimePolicy%2Did"] = id
        return token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ApplicationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ApplicationItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of an application object.
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
    class ApplicationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ApplicationItemRequestBuilder.ApplicationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ApplicationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

