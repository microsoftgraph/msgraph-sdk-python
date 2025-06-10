from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.service_principal import ServicePrincipal
    from .add_key.add_key_request_builder import AddKeyRequestBuilder
    from .add_password.add_password_request_builder import AddPasswordRequestBuilder
    from .add_token_signing_certificate.add_token_signing_certificate_request_builder import AddTokenSigningCertificateRequestBuilder
    from .app_management_policies.app_management_policies_request_builder import AppManagementPoliciesRequestBuilder
    from .app_role_assigned_to.app_role_assigned_to_request_builder import AppRoleAssignedToRequestBuilder
    from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder
    from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder
    from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder
    from .claims_mapping_policies.claims_mapping_policies_request_builder import ClaimsMappingPoliciesRequestBuilder
    from .created_objects.created_objects_request_builder import CreatedObjectsRequestBuilder
    from .delegated_permission_classifications.delegated_permission_classifications_request_builder import DelegatedPermissionClassificationsRequestBuilder
    from .endpoints.endpoints_request_builder import EndpointsRequestBuilder
    from .federated_identity_credentials.federated_identity_credentials_request_builder import FederatedIdentityCredentialsRequestBuilder
    from .federated_identity_credentials_with_name.federated_identity_credentials_with_name_request_builder import FederatedIdentityCredentialsWithNameRequestBuilder
    from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder
    from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder
    from .home_realm_discovery_policies.home_realm_discovery_policies_request_builder import HomeRealmDiscoveryPoliciesRequestBuilder
    from .member_of.member_of_request_builder import MemberOfRequestBuilder
    from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder
    from .owned_objects.owned_objects_request_builder import OwnedObjectsRequestBuilder
    from .owners.owners_request_builder import OwnersRequestBuilder
    from .remote_desktop_security_configuration.remote_desktop_security_configuration_request_builder import RemoteDesktopSecurityConfigurationRequestBuilder
    from .remove_key.remove_key_request_builder import RemoveKeyRequestBuilder
    from .remove_password.remove_password_request_builder import RemovePasswordRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .synchronization.synchronization_request_builder import SynchronizationRequestBuilder
    from .token_issuance_policies.token_issuance_policies_request_builder import TokenIssuancePoliciesRequestBuilder
    from .token_lifetime_policies.token_lifetime_policies_request_builder import TokenLifetimePoliciesRequestBuilder
    from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder

class ServicePrincipalItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of servicePrincipal entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ServicePrincipalItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a servicePrincipal object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def federated_identity_credentials_with_name(self,name: str) -> FederatedIdentityCredentialsWithNameRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.servicePrincipal entity.
        param name: Alternate key of federatedIdentityCredential
        Returns: FederatedIdentityCredentialsWithNameRequestBuilder
        """
        if name is None:
            raise TypeError("name cannot be null.")
        from .federated_identity_credentials_with_name.federated_identity_credentials_with_name_request_builder import FederatedIdentityCredentialsWithNameRequestBuilder

        return FederatedIdentityCredentialsWithNameRequestBuilder(self.request_adapter, self.path_parameters, name)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ServicePrincipalItemRequestBuilderGetQueryParameters]] = None) -> Optional[ServicePrincipal]:
        """
        Retrieve the properties and relationships of a servicePrincipal object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicePrincipal]
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_principal import ServicePrincipal

        return await self.request_adapter.send_async(request_info, ServicePrincipal, error_mapping)
    
    async def patch(self,body: ServicePrincipal, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicePrincipal]:
        """
        Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicePrincipal]
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-upsert?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_principal import ServicePrincipal

        return await self.request_adapter.send_async(request_info, ServicePrincipal, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a servicePrincipal object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ServicePrincipalItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a servicePrincipal object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ServicePrincipal, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ServicePrincipalItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServicePrincipalItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServicePrincipalItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_key(self) -> AddKeyRequestBuilder:
        """
        Provides operations to call the addKey method.
        """
        from .add_key.add_key_request_builder import AddKeyRequestBuilder

        return AddKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_password(self) -> AddPasswordRequestBuilder:
        """
        Provides operations to call the addPassword method.
        """
        from .add_password.add_password_request_builder import AddPasswordRequestBuilder

        return AddPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_token_signing_certificate(self) -> AddTokenSigningCertificateRequestBuilder:
        """
        Provides operations to call the addTokenSigningCertificate method.
        """
        from .add_token_signing_certificate.add_token_signing_certificate_request_builder import AddTokenSigningCertificateRequestBuilder

        return AddTokenSigningCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_management_policies(self) -> AppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_management_policies.app_management_policies_request_builder import AppManagementPoliciesRequestBuilder

        return AppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assigned_to(self) -> AppRoleAssignedToRequestBuilder:
        """
        Provides operations to manage the appRoleAssignedTo property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_role_assigned_to.app_role_assigned_to_request_builder import AppRoleAssignedToRequestBuilder

        return AppRoleAssignedToRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder

        return AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def claims_mapping_policies(self) -> ClaimsMappingPoliciesRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .claims_mapping_policies.claims_mapping_policies_request_builder import ClaimsMappingPoliciesRequestBuilder

        return ClaimsMappingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_objects(self) -> CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.servicePrincipal entity.
        """
        from .created_objects.created_objects_request_builder import CreatedObjectsRequestBuilder

        return CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delegated_permission_classifications(self) -> DelegatedPermissionClassificationsRequestBuilder:
        """
        Provides operations to manage the delegatedPermissionClassifications property of the microsoft.graph.servicePrincipal entity.
        """
        from .delegated_permission_classifications.delegated_permission_classifications_request_builder import DelegatedPermissionClassificationsRequestBuilder

        return DelegatedPermissionClassificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def endpoints(self) -> EndpointsRequestBuilder:
        """
        Provides operations to manage the endpoints property of the microsoft.graph.servicePrincipal entity.
        """
        from .endpoints.endpoints_request_builder import EndpointsRequestBuilder

        return EndpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federated_identity_credentials(self) -> FederatedIdentityCredentialsRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.servicePrincipal entity.
        """
        from .federated_identity_credentials.federated_identity_credentials_request_builder import FederatedIdentityCredentialsRequestBuilder

        return FederatedIdentityCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def home_realm_discovery_policies(self) -> HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .home_realm_discovery_policies.home_realm_discovery_policies_request_builder import HomeRealmDiscoveryPoliciesRequestBuilder

        return HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.servicePrincipal entity.
        """
        from .member_of.member_of_request_builder import MemberOfRequestBuilder

        return MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.servicePrincipal entity.
        """
        from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder

        return Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_objects(self) -> OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.servicePrincipal entity.
        """
        from .owned_objects.owned_objects_request_builder import OwnedObjectsRequestBuilder

        return OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.servicePrincipal entity.
        """
        from .owners.owners_request_builder import OwnersRequestBuilder

        return OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_desktop_security_configuration(self) -> RemoteDesktopSecurityConfigurationRequestBuilder:
        """
        Provides operations to manage the remoteDesktopSecurityConfiguration property of the microsoft.graph.servicePrincipal entity.
        """
        from .remote_desktop_security_configuration.remote_desktop_security_configuration_request_builder import RemoteDesktopSecurityConfigurationRequestBuilder

        return RemoteDesktopSecurityConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_key(self) -> RemoveKeyRequestBuilder:
        """
        Provides operations to call the removeKey method.
        """
        from .remove_key.remove_key_request_builder import RemoveKeyRequestBuilder

        return RemoveKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_password(self) -> RemovePasswordRequestBuilder:
        """
        Provides operations to call the removePassword method.
        """
        from .remove_password.remove_password_request_builder import RemovePasswordRequestBuilder

        return RemovePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def synchronization(self) -> SynchronizationRequestBuilder:
        """
        Provides operations to manage the synchronization property of the microsoft.graph.servicePrincipal entity.
        """
        from .synchronization.synchronization_request_builder import SynchronizationRequestBuilder

        return SynchronizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_issuance_policies(self) -> TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .token_issuance_policies.token_issuance_policies_request_builder import TokenIssuancePoliciesRequestBuilder

        return TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_lifetime_policies(self) -> TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .token_lifetime_policies.token_lifetime_policies_request_builder import TokenLifetimePoliciesRequestBuilder

        return TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.servicePrincipal entity.
        """
        from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder

        return TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ServicePrincipalItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServicePrincipalItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a servicePrincipal object.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class ServicePrincipalItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ServicePrincipalItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServicePrincipalItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

