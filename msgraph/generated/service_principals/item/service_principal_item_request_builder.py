from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import service_principal
    from ...models.o_data_errors import o_data_error
    from .add_key import add_key_request_builder
    from .add_password import add_password_request_builder
    from .add_token_signing_certificate import add_token_signing_certificate_request_builder
    from .app_management_policies import app_management_policies_request_builder
    from .app_management_policies.item import app_management_policy_item_request_builder
    from .app_role_assigned_to import app_role_assigned_to_request_builder
    from .app_role_assigned_to.item import app_role_assignment_item_request_builder
    from .app_role_assignments import app_role_assignments_request_builder
    from .app_role_assignments.item import app_role_assignment_item_request_builder
    from .check_member_groups import check_member_groups_request_builder
    from .check_member_objects import check_member_objects_request_builder
    from .claims_mapping_policies import claims_mapping_policies_request_builder
    from .claims_mapping_policies.item import claims_mapping_policy_item_request_builder
    from .created_objects import created_objects_request_builder
    from .created_objects.item import directory_object_item_request_builder
    from .delegated_permission_classifications import delegated_permission_classifications_request_builder
    from .delegated_permission_classifications.item import delegated_permission_classification_item_request_builder
    from .endpoints import endpoints_request_builder
    from .endpoints.item import endpoint_item_request_builder
    from .federated_identity_credentials import federated_identity_credentials_request_builder
    from .federated_identity_credentials.item import federated_identity_credential_item_request_builder
    from .get_member_groups import get_member_groups_request_builder
    from .get_member_objects import get_member_objects_request_builder
    from .home_realm_discovery_policies import home_realm_discovery_policies_request_builder
    from .home_realm_discovery_policies.item import home_realm_discovery_policy_item_request_builder
    from .member_of import member_of_request_builder
    from .member_of.item import directory_object_item_request_builder
    from .oauth2_permission_grants import oauth2_permission_grants_request_builder
    from .oauth2_permission_grants.item import o_auth2_permission_grant_item_request_builder
    from .owned_objects import owned_objects_request_builder
    from .owned_objects.item import directory_object_item_request_builder
    from .owners import owners_request_builder
    from .owners.item import directory_object_item_request_builder
    from .remove_key import remove_key_request_builder
    from .remove_password import remove_password_request_builder
    from .restore import restore_request_builder
    from .token_issuance_policies import token_issuance_policies_request_builder
    from .token_issuance_policies.item import token_issuance_policy_item_request_builder
    from .token_lifetime_policies import token_lifetime_policies_request_builder
    from .token_lifetime_policies.item import token_lifetime_policy_item_request_builder
    from .transitive_member_of import transitive_member_of_request_builder
    from .transitive_member_of.item import directory_object_item_request_builder

class ServicePrincipalItemRequestBuilder():
    """
    Provides operations to manage the collection of servicePrincipal entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ServicePrincipalItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def app_management_policies_by_id(self,id: str) -> app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .app_management_policies.item import app_management_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appManagementPolicy%2Did"] = id
        return app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_role_assigned_to_by_id(self,id: str) -> app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the appRoleAssignedTo property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .app_role_assigned_to.item import app_role_assignment_item_request_builder
        from .app_role_assignments.item import app_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appRoleAssignment%2Did"] = id
        return app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_role_assignments_by_id(self,id: str) -> app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .app_role_assigned_to.item import app_role_assignment_item_request_builder
        from .app_role_assignments.item import app_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appRoleAssignment%2Did"] = id
        return app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def claims_mapping_policies_by_id(self,id: str) -> claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.servicePrincipals.item.claimsMappingPolicies.item collection
        Args:
            id: Unique identifier of the item
        Returns: claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .claims_mapping_policies.item import claims_mapping_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["claimsMappingPolicy%2Did"] = id
        return claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def created_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .created_objects.item import directory_object_item_request_builder
        from .member_of.item import directory_object_item_request_builder
        from .owned_objects.item import directory_object_item_request_builder
        from .owners.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def delegated_permission_classifications_by_id(self,id: str) -> delegated_permission_classification_item_request_builder.DelegatedPermissionClassificationItemRequestBuilder:
        """
        Provides operations to manage the delegatedPermissionClassifications property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_permission_classification_item_request_builder.DelegatedPermissionClassificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .delegated_permission_classifications.item import delegated_permission_classification_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedPermissionClassification%2Did"] = id
        return delegated_permission_classification_item_request_builder.DelegatedPermissionClassificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ServicePrincipalItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete a servicePrincipal object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def endpoints_by_id(self,id: str) -> endpoint_item_request_builder.EndpointItemRequestBuilder:
        """
        Provides operations to manage the endpoints property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: endpoint_item_request_builder.EndpointItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .endpoints.item import endpoint_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["endpoint%2Did"] = id
        return endpoint_item_request_builder.EndpointItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def federated_identity_credentials_by_id(self,id: str) -> federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .federated_identity_credentials.item import federated_identity_credential_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["federatedIdentityCredential%2Did"] = id
        return federated_identity_credential_item_request_builder.FederatedIdentityCredentialItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ServicePrincipalItemRequestBuilderGetRequestConfiguration] = None) -> Optional[service_principal.ServicePrincipal]:
        """
        Retrieve the properties and relationships of a servicePrincipal object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[service_principal.ServicePrincipal]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import service_principal

        return await self.request_adapter.send_async(request_info, service_principal.ServicePrincipal, error_mapping)
    
    def home_realm_discovery_policies_by_id(self,id: str) -> home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.servicePrincipals.item.homeRealmDiscoveryPolicies.item collection
        Args:
            id: Unique identifier of the item
        Returns: home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .home_realm_discovery_policies.item import home_realm_discovery_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["homeRealmDiscoveryPolicy%2Did"] = id
        return home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .created_objects.item import directory_object_item_request_builder
        from .member_of.item import directory_object_item_request_builder
        from .owned_objects.item import directory_object_item_request_builder
        from .owners.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def oauth2_permission_grants_by_id(self,id: str) -> o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .oauth2_permission_grants.item import o_auth2_permission_grant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oAuth2PermissionGrant%2Did"] = id
        return o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owned_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .created_objects.item import directory_object_item_request_builder
        from .member_of.item import directory_object_item_request_builder
        from .owned_objects.item import directory_object_item_request_builder
        from .owners.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owners_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.servicePrincipals.item.owners.item collection
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .created_objects.item import directory_object_item_request_builder
        from .member_of.item import directory_object_item_request_builder
        from .owned_objects.item import directory_object_item_request_builder
        from .owners.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[service_principal.ServicePrincipal] = None, request_configuration: Optional[ServicePrincipalItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[service_principal.ServicePrincipal]:
        """
        Update entity in servicePrincipals
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[service_principal.ServicePrincipal]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import service_principal

        return await self.request_adapter.send_async(request_info, service_principal.ServicePrincipal, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ServicePrincipalItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a servicePrincipal object.
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
    
    def to_get_request_information(self,request_configuration: Optional[ServicePrincipalItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a servicePrincipal object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def token_issuance_policies_by_id(self,id: str) -> token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .token_issuance_policies.item import token_issuance_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenIssuancePolicy%2Did"] = id
        return token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def token_lifetime_policies_by_id(self,id: str) -> token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .token_lifetime_policies.item import token_lifetime_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenLifetimePolicy%2Did"] = id
        return token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_patch_request_information(self,body: Optional[service_principal.ServicePrincipal] = None, request_configuration: Optional[ServicePrincipalItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in servicePrincipals
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def transitive_member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.servicePrincipal entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .created_objects.item import directory_object_item_request_builder
        from .member_of.item import directory_object_item_request_builder
        from .owned_objects.item import directory_object_item_request_builder
        from .owners.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def add_key(self) -> add_key_request_builder.AddKeyRequestBuilder:
        """
        Provides operations to call the addKey method.
        """
        from .add_key import add_key_request_builder

        return add_key_request_builder.AddKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_password(self) -> add_password_request_builder.AddPasswordRequestBuilder:
        """
        Provides operations to call the addPassword method.
        """
        from .add_password import add_password_request_builder

        return add_password_request_builder.AddPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_token_signing_certificate(self) -> add_token_signing_certificate_request_builder.AddTokenSigningCertificateRequestBuilder:
        """
        Provides operations to call the addTokenSigningCertificate method.
        """
        from .add_token_signing_certificate import add_token_signing_certificate_request_builder

        return add_token_signing_certificate_request_builder.AddTokenSigningCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_management_policies(self) -> app_management_policies_request_builder.AppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_management_policies import app_management_policies_request_builder

        return app_management_policies_request_builder.AppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assigned_to(self) -> app_role_assigned_to_request_builder.AppRoleAssignedToRequestBuilder:
        """
        Provides operations to manage the appRoleAssignedTo property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_role_assigned_to import app_role_assigned_to_request_builder

        return app_role_assigned_to_request_builder.AppRoleAssignedToRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.servicePrincipal entity.
        """
        from .app_role_assignments import app_role_assignments_request_builder

        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups import check_member_groups_request_builder

        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects import check_member_objects_request_builder

        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def claims_mapping_policies(self) -> claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .claims_mapping_policies import claims_mapping_policies_request_builder

        return claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_objects(self) -> created_objects_request_builder.CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.servicePrincipal entity.
        """
        from .created_objects import created_objects_request_builder

        return created_objects_request_builder.CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delegated_permission_classifications(self) -> delegated_permission_classifications_request_builder.DelegatedPermissionClassificationsRequestBuilder:
        """
        Provides operations to manage the delegatedPermissionClassifications property of the microsoft.graph.servicePrincipal entity.
        """
        from .delegated_permission_classifications import delegated_permission_classifications_request_builder

        return delegated_permission_classifications_request_builder.DelegatedPermissionClassificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def endpoints(self) -> endpoints_request_builder.EndpointsRequestBuilder:
        """
        Provides operations to manage the endpoints property of the microsoft.graph.servicePrincipal entity.
        """
        from .endpoints import endpoints_request_builder

        return endpoints_request_builder.EndpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federated_identity_credentials(self) -> federated_identity_credentials_request_builder.FederatedIdentityCredentialsRequestBuilder:
        """
        Provides operations to manage the federatedIdentityCredentials property of the microsoft.graph.servicePrincipal entity.
        """
        from .federated_identity_credentials import federated_identity_credentials_request_builder

        return federated_identity_credentials_request_builder.FederatedIdentityCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups import get_member_groups_request_builder

        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects import get_member_objects_request_builder

        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def home_realm_discovery_policies(self) -> home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .home_realm_discovery_policies import home_realm_discovery_policies_request_builder

        return home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.servicePrincipal entity.
        """
        from .member_of import member_of_request_builder

        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.servicePrincipal entity.
        """
        from .oauth2_permission_grants import oauth2_permission_grants_request_builder

        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_objects(self) -> owned_objects_request_builder.OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.servicePrincipal entity.
        """
        from .owned_objects import owned_objects_request_builder

        return owned_objects_request_builder.OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> owners_request_builder.OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.servicePrincipal entity.
        """
        from .owners import owners_request_builder

        return owners_request_builder.OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_key(self) -> remove_key_request_builder.RemoveKeyRequestBuilder:
        """
        Provides operations to call the removeKey method.
        """
        from .remove_key import remove_key_request_builder

        return remove_key_request_builder.RemoveKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_password(self) -> remove_password_request_builder.RemovePasswordRequestBuilder:
        """
        Provides operations to call the removePassword method.
        """
        from .remove_password import remove_password_request_builder

        return remove_password_request_builder.RemovePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_issuance_policies(self) -> token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .token_issuance_policies import token_issuance_policies_request_builder

        return token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_lifetime_policies(self) -> token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.servicePrincipal entity.
        """
        from .token_lifetime_policies import token_lifetime_policies_request_builder

        return token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.servicePrincipal entity.
        """
        from .transitive_member_of import transitive_member_of_request_builder

        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ServicePrincipalItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ServicePrincipalItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a servicePrincipal object.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ServicePrincipalItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ServicePrincipalItemRequestBuilder.ServicePrincipalItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ServicePrincipalItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

