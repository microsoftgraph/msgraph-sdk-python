from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

add_in = lazy_import('msgraph.generated.models.add_in')
app_role = lazy_import('msgraph.generated.models.app_role')
app_role_assignment = lazy_import('msgraph.generated.models.app_role_assignment')
claims_mapping_policy = lazy_import('msgraph.generated.models.claims_mapping_policy')
delegated_permission_classification = lazy_import('msgraph.generated.models.delegated_permission_classification')
directory_object = lazy_import('msgraph.generated.models.directory_object')
endpoint = lazy_import('msgraph.generated.models.endpoint')
federated_identity_credential = lazy_import('msgraph.generated.models.federated_identity_credential')
home_realm_discovery_policy = lazy_import('msgraph.generated.models.home_realm_discovery_policy')
informational_url = lazy_import('msgraph.generated.models.informational_url')
key_credential = lazy_import('msgraph.generated.models.key_credential')
o_auth2_permission_grant = lazy_import('msgraph.generated.models.o_auth2_permission_grant')
password_credential = lazy_import('msgraph.generated.models.password_credential')
permission_scope = lazy_import('msgraph.generated.models.permission_scope')
resource_specific_permission = lazy_import('msgraph.generated.models.resource_specific_permission')
saml_single_sign_on_settings = lazy_import('msgraph.generated.models.saml_single_sign_on_settings')
token_issuance_policy = lazy_import('msgraph.generated.models.token_issuance_policy')
token_lifetime_policy = lazy_import('msgraph.generated.models.token_lifetime_policy')
verified_publisher = lazy_import('msgraph.generated.models.verified_publisher')

class ServicePrincipal(directory_object.DirectoryObject):
    @property
    def account_enabled(self,) -> Optional[bool]:
        """
        Gets the accountEnabled property value. true if the service principal account is enabled; otherwise, false. If set to false, then no users will be able to sign in to this app, even if they are assigned to it. Supports $filter (eq, ne, not, in).
        Returns: Optional[bool]
        """
        return self._account_enabled
    
    @account_enabled.setter
    def account_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountEnabled property value. true if the service principal account is enabled; otherwise, false. If set to false, then no users will be able to sign in to this app, even if they are assigned to it. Supports $filter (eq, ne, not, in).
        Args:
            value: Value to set for the accountEnabled property.
        """
        self._account_enabled = value
    
    @property
    def add_ins(self,) -> Optional[List[add_in.AddIn]]:
        """
        Gets the addIns property value. Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.
        Returns: Optional[List[add_in.AddIn]]
        """
        return self._add_ins
    
    @add_ins.setter
    def add_ins(self,value: Optional[List[add_in.AddIn]] = None) -> None:
        """
        Sets the addIns property value. Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.
        Args:
            value: Value to set for the addIns property.
        """
        self._add_ins = value
    
    @property
    def alternative_names(self,) -> Optional[List[str]]:
        """
        Gets the alternativeNames property value. Used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._alternative_names
    
    @alternative_names.setter
    def alternative_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the alternativeNames property value. Used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the alternativeNames property.
        """
        self._alternative_names = value
    
    @property
    def app_description(self,) -> Optional[str]:
        """
        Gets the appDescription property value. The description exposed by the associated application.
        Returns: Optional[str]
        """
        return self._app_description
    
    @app_description.setter
    def app_description(self,value: Optional[str] = None) -> None:
        """
        Sets the appDescription property value. The description exposed by the associated application.
        Args:
            value: Value to set for the appDescription property.
        """
        self._app_description = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The display name exposed by the associated application.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The display name exposed by the associated application.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The unique identifier for the associated application (its appId property). Supports $filter (eq, ne, not, in, startsWith).
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The unique identifier for the associated application (its appId property). Supports $filter (eq, ne, not, in, startsWith).
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def application_template_id(self,) -> Optional[str]:
        """
        Gets the applicationTemplateId property value. Unique identifier of the applicationTemplate that the servicePrincipal was created from. Read-only. Supports $filter (eq, ne, NOT, startsWith).
        Returns: Optional[str]
        """
        return self._application_template_id
    
    @application_template_id.setter
    def application_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationTemplateId property value. Unique identifier of the applicationTemplate that the servicePrincipal was created from. Read-only. Supports $filter (eq, ne, NOT, startsWith).
        Args:
            value: Value to set for the applicationTemplateId property.
        """
        self._application_template_id = value
    
    @property
    def app_owner_organization_id(self,) -> Optional[str]:
        """
        Gets the appOwnerOrganizationId property value. Contains the tenant id where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
        Returns: Optional[str]
        """
        return self._app_owner_organization_id
    
    @app_owner_organization_id.setter
    def app_owner_organization_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appOwnerOrganizationId property value. Contains the tenant id where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
        Args:
            value: Value to set for the appOwnerOrganizationId property.
        """
        self._app_owner_organization_id = value
    
    @property
    def app_role_assigned_to(self,) -> Optional[List[app_role_assignment.AppRoleAssignment]]:
        """
        Gets the appRoleAssignedTo property value. App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.
        Returns: Optional[List[app_role_assignment.AppRoleAssignment]]
        """
        return self._app_role_assigned_to
    
    @app_role_assigned_to.setter
    def app_role_assigned_to(self,value: Optional[List[app_role_assignment.AppRoleAssignment]] = None) -> None:
        """
        Sets the appRoleAssignedTo property value. App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.
        Args:
            value: Value to set for the appRoleAssignedTo property.
        """
        self._app_role_assigned_to = value
    
    @property
    def app_role_assignment_required(self,) -> Optional[bool]:
        """
        Gets the appRoleAssignmentRequired property value. Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
        Returns: Optional[bool]
        """
        return self._app_role_assignment_required
    
    @app_role_assignment_required.setter
    def app_role_assignment_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the appRoleAssignmentRequired property value. Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
        Args:
            value: Value to set for the appRoleAssignmentRequired property.
        """
        self._app_role_assignment_required = value
    
    @property
    def app_role_assignments(self,) -> Optional[List[app_role_assignment.AppRoleAssignment]]:
        """
        Gets the appRoleAssignments property value. App role assignment for another app or service, granted to this service principal. Supports $expand.
        Returns: Optional[List[app_role_assignment.AppRoleAssignment]]
        """
        return self._app_role_assignments
    
    @app_role_assignments.setter
    def app_role_assignments(self,value: Optional[List[app_role_assignment.AppRoleAssignment]] = None) -> None:
        """
        Sets the appRoleAssignments property value. App role assignment for another app or service, granted to this service principal. Supports $expand.
        Args:
            value: Value to set for the appRoleAssignments property.
        """
        self._app_role_assignments = value
    
    @property
    def app_roles(self,) -> Optional[List[app_role.AppRole]]:
        """
        Gets the appRoles property value. The roles exposed by the application which this service principal represents. For more information see the appRoles property definition on the application entity. Not nullable.
        Returns: Optional[List[app_role.AppRole]]
        """
        return self._app_roles
    
    @app_roles.setter
    def app_roles(self,value: Optional[List[app_role.AppRole]] = None) -> None:
        """
        Sets the appRoles property value. The roles exposed by the application which this service principal represents. For more information see the appRoles property definition on the application entity. Not nullable.
        Args:
            value: Value to set for the appRoles property.
        """
        self._app_roles = value
    
    @property
    def claims_mapping_policies(self,) -> Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]:
        """
        Gets the claimsMappingPolicies property value. The claimsMappingPolicies assigned to this service principal. Supports $expand.
        Returns: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]
        """
        return self._claims_mapping_policies
    
    @claims_mapping_policies.setter
    def claims_mapping_policies(self,value: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None) -> None:
        """
        Sets the claimsMappingPolicies property value. The claimsMappingPolicies assigned to this service principal. Supports $expand.
        Args:
            value: Value to set for the claimsMappingPolicies property.
        """
        self._claims_mapping_policies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new servicePrincipal and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.servicePrincipal"
        # true if the service principal account is enabled; otherwise, false. If set to false, then no users will be able to sign in to this app, even if they are assigned to it. Supports $filter (eq, ne, not, in).
        self._account_enabled: Optional[bool] = None
        # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.
        self._add_ins: Optional[List[add_in.AddIn]] = None
        # Used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities. Supports $filter (eq, not, ge, le, startsWith).
        self._alternative_names: Optional[List[str]] = None
        # The description exposed by the associated application.
        self._app_description: Optional[str] = None
        # The display name exposed by the associated application.
        self._app_display_name: Optional[str] = None
        # The unique identifier for the associated application (its appId property). Supports $filter (eq, ne, not, in, startsWith).
        self._app_id: Optional[str] = None
        # Unique identifier of the applicationTemplate that the servicePrincipal was created from. Read-only. Supports $filter (eq, ne, NOT, startsWith).
        self._application_template_id: Optional[str] = None
        # Contains the tenant id where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
        self._app_owner_organization_id: Optional[str] = None
        # App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.
        self._app_role_assigned_to: Optional[List[app_role_assignment.AppRoleAssignment]] = None
        # Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
        self._app_role_assignment_required: Optional[bool] = None
        # App role assignment for another app or service, granted to this service principal. Supports $expand.
        self._app_role_assignments: Optional[List[app_role_assignment.AppRoleAssignment]] = None
        # The roles exposed by the application which this service principal represents. For more information see the appRoles property definition on the application entity. Not nullable.
        self._app_roles: Optional[List[app_role.AppRole]] = None
        # The claimsMappingPolicies assigned to this service principal. Supports $expand.
        self._claims_mapping_policies: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None
        # Directory objects created by this service principal. Read-only. Nullable.
        self._created_objects: Optional[List[directory_object.DirectoryObject]] = None
        # The delegatedPermissionClassifications property
        self._delegated_permission_classifications: Optional[List[delegated_permission_classification.DelegatedPermissionClassification]] = None
        # Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps will display the application description in this field. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        self._description: Optional[str] = None
        # Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        self._disabled_by_microsoft_status: Optional[str] = None
        # The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # The endpoints property
        self._endpoints: Optional[List[endpoint.Endpoint]] = None
        # Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        self._federated_identity_credentials: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None
        # Home page or landing page of the application.
        self._homepage: Optional[str] = None
        # The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
        self._home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
        # Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        self._info: Optional[informational_url.InformationalUrl] = None
        # The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
        self._key_credentials: Optional[List[key_credential.KeyCredential]] = None
        # Specifies the URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Azure AD My Apps, or the Azure AD SSO URL.
        self._login_url: Optional[str] = None
        # Specifies the URL that will be used by Microsoft's authorization service to logout an user using OpenId Connect front-channel, back-channel or SAML logout protocols.
        self._logout_url: Optional[str] = None
        # Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1024 characters.
        self._notes: Optional[str] = None
        # Specifies the list of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications.
        self._notification_email_addresses: Optional[List[str]] = None
        # Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
        self._oauth2_permission_grants: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]] = None
        # The delegated permissions exposed by the application. For more information see the oauth2PermissionScopes property on the application entity's api property. Not nullable.
        self._oauth2_permission_scopes: Optional[List[permission_scope.PermissionScope]] = None
        # Directory objects that are owned by this service principal. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        self._owned_objects: Optional[List[directory_object.DirectoryObject]] = None
        # Directory objects that are owners of this servicePrincipal. The owners are a set of non-admin users or servicePrincipals who are allowed to modify this object. Read-only. Nullable.  Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        self._owners: Optional[List[directory_object.DirectoryObject]] = None
        # The collection of password credentials associated with the application. Not nullable.
        self._password_credentials: Optional[List[password_credential.PasswordCredential]] = None
        # Specifies the single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps. The supported values are password, saml, notSupported, and oidc.
        self._preferred_single_sign_on_mode: Optional[str] = None
        # Reserved for internal use only. Do not write or otherwise rely on this property. May be removed in future versions.
        self._preferred_token_signing_key_thumbprint: Optional[str] = None
        # The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
        self._reply_urls: Optional[List[str]] = None
        # The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.
        self._resource_specific_application_permissions: Optional[List[resource_specific_permission.ResourceSpecificPermission]] = None
        # The collection for settings related to saml single sign-on.
        self._saml_single_sign_on_settings: Optional[saml_single_sign_on_settings.SamlSingleSignOnSettings] = None
        # Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Azure AD. For example,Client apps can specify a resource URI which is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
        self._service_principal_names: Optional[List[str]] = None
        # Identifies whether the service principal represents an application, a managed identity, or a legacy application. This is set by Azure AD internally. The servicePrincipalType property can be set to three different values: __Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens are not issued for the service principal.__ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but cannot be updated or modified directly.__Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. Legacy service principal can have credentials, service principal names, reply URLs, and other properties which are editable by an authorized user, but does not have an associated app registration. The appId value does not associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.__SocialIdp - For internal use.
        self._service_principal_type: Optional[str] = None
        # Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization’s Azure AD tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization’s Azure AD tenant (multi-tenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization’s Azure AD tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
        self._sign_in_audience: Optional[str] = None
        # Custom strings that can be used to categorize and identify the service principal. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        self._tags: Optional[List[str]] = None
        # Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        self._token_encryption_key_id: Optional[str] = None
        # The tokenIssuancePolicies assigned to this service principal.
        self._token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
        # The tokenLifetimePolicies assigned to this service principal.
        self._token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
        # The transitiveMemberOf property
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Specifies the verified publisher of the application which this service principal represents.
        self._verified_publisher: Optional[verified_publisher.VerifiedPublisher] = None
    
    @property
    def created_objects(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the createdObjects property value. Directory objects created by this service principal. Read-only. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._created_objects
    
    @created_objects.setter
    def created_objects(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the createdObjects property value. Directory objects created by this service principal. Read-only. Nullable.
        Args:
            value: Value to set for the createdObjects property.
        """
        self._created_objects = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipal()
    
    @property
    def delegated_permission_classifications(self,) -> Optional[List[delegated_permission_classification.DelegatedPermissionClassification]]:
        """
        Gets the delegatedPermissionClassifications property value. The delegatedPermissionClassifications property
        Returns: Optional[List[delegated_permission_classification.DelegatedPermissionClassification]]
        """
        return self._delegated_permission_classifications
    
    @delegated_permission_classifications.setter
    def delegated_permission_classifications(self,value: Optional[List[delegated_permission_classification.DelegatedPermissionClassification]] = None) -> None:
        """
        Sets the delegatedPermissionClassifications property value. The delegatedPermissionClassifications property
        Args:
            value: Value to set for the delegatedPermissionClassifications property.
        """
        self._delegated_permission_classifications = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps will display the application description in this field. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps will display the application description in this field. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def disabled_by_microsoft_status(self,) -> Optional[str]:
        """
        Gets the disabledByMicrosoftStatus property value. Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        Returns: Optional[str]
        """
        return self._disabled_by_microsoft_status
    
    @disabled_by_microsoft_status.setter
    def disabled_by_microsoft_status(self,value: Optional[str] = None) -> None:
        """
        Sets the disabledByMicrosoftStatus property value. Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the disabledByMicrosoftStatus property.
        """
        self._disabled_by_microsoft_status = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def endpoints(self,) -> Optional[List[endpoint.Endpoint]]:
        """
        Gets the endpoints property value. The endpoints property
        Returns: Optional[List[endpoint.Endpoint]]
        """
        return self._endpoints
    
    @endpoints.setter
    def endpoints(self,value: Optional[List[endpoint.Endpoint]] = None) -> None:
        """
        Sets the endpoints property value. The endpoints property
        Args:
            value: Value to set for the endpoints property.
        """
        self._endpoints = value
    
    @property
    def federated_identity_credentials(self,) -> Optional[List[federated_identity_credential.FederatedIdentityCredential]]:
        """
        Gets the federatedIdentityCredentials property value. Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Returns: Optional[List[federated_identity_credential.FederatedIdentityCredential]]
        """
        return self._federated_identity_credentials
    
    @federated_identity_credentials.setter
    def federated_identity_credentials(self,value: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None) -> None:
        """
        Sets the federatedIdentityCredentials property value. Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the federatedIdentityCredentials property.
        """
        self._federated_identity_credentials = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_enabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "add_ins": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(add_in.AddIn)),
            "alternative_names": lambda n : setattr(self, 'alternative_names', n.get_collection_of_primitive_values(str)),
            "app_description": lambda n : setattr(self, 'app_description', n.get_str_value()),
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "application_template_id": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "app_owner_organization_id": lambda n : setattr(self, 'app_owner_organization_id', n.get_str_value()),
            "app_role_assigned_to": lambda n : setattr(self, 'app_role_assigned_to', n.get_collection_of_object_values(app_role_assignment.AppRoleAssignment)),
            "app_role_assignment_required": lambda n : setattr(self, 'app_role_assignment_required', n.get_bool_value()),
            "app_role_assignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(app_role_assignment.AppRoleAssignment)),
            "app_roles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(app_role.AppRole)),
            "claims_mapping_policies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(claims_mapping_policy.ClaimsMappingPolicy)),
            "created_objects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "delegated_permission_classifications": lambda n : setattr(self, 'delegated_permission_classifications', n.get_collection_of_object_values(delegated_permission_classification.DelegatedPermissionClassification)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabled_by_microsoft_status": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(endpoint.Endpoint)),
            "federated_identity_credentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(federated_identity_credential.FederatedIdentityCredential)),
            "homepage": lambda n : setattr(self, 'homepage', n.get_str_value()),
            "home_realm_discovery_policies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "info": lambda n : setattr(self, 'info', n.get_object_value(informational_url.InformationalUrl)),
            "key_credentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(key_credential.KeyCredential)),
            "login_url": lambda n : setattr(self, 'login_url', n.get_str_value()),
            "logout_url": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "notification_email_addresses": lambda n : setattr(self, 'notification_email_addresses', n.get_collection_of_primitive_values(str)),
            "oauth2_permission_grants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(o_auth2_permission_grant.OAuth2PermissionGrant)),
            "oauth2_permission_scopes": lambda n : setattr(self, 'oauth2_permission_scopes', n.get_collection_of_object_values(permission_scope.PermissionScope)),
            "owned_objects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "password_credentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(password_credential.PasswordCredential)),
            "preferred_single_sign_on_mode": lambda n : setattr(self, 'preferred_single_sign_on_mode', n.get_str_value()),
            "preferred_token_signing_key_thumbprint": lambda n : setattr(self, 'preferred_token_signing_key_thumbprint', n.get_str_value()),
            "reply_urls": lambda n : setattr(self, 'reply_urls', n.get_collection_of_primitive_values(str)),
            "resource_specific_application_permissions": lambda n : setattr(self, 'resource_specific_application_permissions', n.get_collection_of_object_values(resource_specific_permission.ResourceSpecificPermission)),
            "saml_single_sign_on_settings": lambda n : setattr(self, 'saml_single_sign_on_settings', n.get_object_value(saml_single_sign_on_settings.SamlSingleSignOnSettings)),
            "service_principal_names": lambda n : setattr(self, 'service_principal_names', n.get_collection_of_primitive_values(str)),
            "service_principal_type": lambda n : setattr(self, 'service_principal_type', n.get_str_value()),
            "sign_in_audience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "token_encryption_key_id": lambda n : setattr(self, 'token_encryption_key_id', n.get_str_value()),
            "token_issuance_policies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "token_lifetime_policies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
            "transitive_member_of": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "verified_publisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(verified_publisher.VerifiedPublisher)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def homepage(self,) -> Optional[str]:
        """
        Gets the homepage property value. Home page or landing page of the application.
        Returns: Optional[str]
        """
        return self._homepage
    
    @homepage.setter
    def homepage(self,value: Optional[str] = None) -> None:
        """
        Sets the homepage property value. Home page or landing page of the application.
        Args:
            value: Value to set for the homepage property.
        """
        self._homepage = value
    
    @property
    def home_realm_discovery_policies(self,) -> Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]:
        """
        Gets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
        Returns: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]
        """
        return self._home_realm_discovery_policies
    
    @home_realm_discovery_policies.setter
    def home_realm_discovery_policies(self,value: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None) -> None:
        """
        Sets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
        Args:
            value: Value to set for the homeRealmDiscoveryPolicies property.
        """
        self._home_realm_discovery_policies = value
    
    @property
    def info(self,) -> Optional[informational_url.InformationalUrl]:
        """
        Gets the info property value. Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Returns: Optional[informational_url.InformationalUrl]
        """
        return self._info
    
    @info.setter
    def info(self,value: Optional[informational_url.InformationalUrl] = None) -> None:
        """
        Sets the info property value. Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Args:
            value: Value to set for the info property.
        """
        self._info = value
    
    @property
    def key_credentials(self,) -> Optional[List[key_credential.KeyCredential]]:
        """
        Gets the keyCredentials property value. The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[key_credential.KeyCredential]]
        """
        return self._key_credentials
    
    @key_credentials.setter
    def key_credentials(self,value: Optional[List[key_credential.KeyCredential]] = None) -> None:
        """
        Sets the keyCredentials property value. The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the keyCredentials property.
        """
        self._key_credentials = value
    
    @property
    def login_url(self,) -> Optional[str]:
        """
        Gets the loginUrl property value. Specifies the URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Azure AD My Apps, or the Azure AD SSO URL.
        Returns: Optional[str]
        """
        return self._login_url
    
    @login_url.setter
    def login_url(self,value: Optional[str] = None) -> None:
        """
        Sets the loginUrl property value. Specifies the URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Azure AD My Apps, or the Azure AD SSO URL.
        Args:
            value: Value to set for the loginUrl property.
        """
        self._login_url = value
    
    @property
    def logout_url(self,) -> Optional[str]:
        """
        Gets the logoutUrl property value. Specifies the URL that will be used by Microsoft's authorization service to logout an user using OpenId Connect front-channel, back-channel or SAML logout protocols.
        Returns: Optional[str]
        """
        return self._logout_url
    
    @logout_url.setter
    def logout_url(self,value: Optional[str] = None) -> None:
        """
        Sets the logoutUrl property value. Specifies the URL that will be used by Microsoft's authorization service to logout an user using OpenId Connect front-channel, back-channel or SAML logout protocols.
        Args:
            value: Value to set for the logoutUrl property.
        """
        self._logout_url = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the memberOf property.
        """
        self._member_of = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1024 characters.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1024 characters.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def notification_email_addresses(self,) -> Optional[List[str]]:
        """
        Gets the notificationEmailAddresses property value. Specifies the list of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications.
        Returns: Optional[List[str]]
        """
        return self._notification_email_addresses
    
    @notification_email_addresses.setter
    def notification_email_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notificationEmailAddresses property value. Specifies the list of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications.
        Args:
            value: Value to set for the notificationEmailAddresses property.
        """
        self._notification_email_addresses = value
    
    @property
    def oauth2_permission_grants(self,) -> Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]]:
        """
        Gets the oauth2PermissionGrants property value. Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
        Returns: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]]
        """
        return self._oauth2_permission_grants
    
    @oauth2_permission_grants.setter
    def oauth2_permission_grants(self,value: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]] = None) -> None:
        """
        Sets the oauth2PermissionGrants property value. Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
        Args:
            value: Value to set for the oauth2PermissionGrants property.
        """
        self._oauth2_permission_grants = value
    
    @property
    def oauth2_permission_scopes(self,) -> Optional[List[permission_scope.PermissionScope]]:
        """
        Gets the oauth2PermissionScopes property value. The delegated permissions exposed by the application. For more information see the oauth2PermissionScopes property on the application entity's api property. Not nullable.
        Returns: Optional[List[permission_scope.PermissionScope]]
        """
        return self._oauth2_permission_scopes
    
    @oauth2_permission_scopes.setter
    def oauth2_permission_scopes(self,value: Optional[List[permission_scope.PermissionScope]] = None) -> None:
        """
        Sets the oauth2PermissionScopes property value. The delegated permissions exposed by the application. For more information see the oauth2PermissionScopes property on the application entity's api property. Not nullable.
        Args:
            value: Value to set for the oauth2PermissionScopes property.
        """
        self._oauth2_permission_scopes = value
    
    @property
    def owned_objects(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the ownedObjects property value. Directory objects that are owned by this service principal. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owned_objects
    
    @owned_objects.setter
    def owned_objects(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the ownedObjects property value. Directory objects that are owned by this service principal. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            value: Value to set for the ownedObjects property.
        """
        self._owned_objects = value
    
    @property
    def owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the owners property value. Directory objects that are owners of this servicePrincipal. The owners are a set of non-admin users or servicePrincipals who are allowed to modify this object. Read-only. Nullable.  Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the owners property value. Directory objects that are owners of this servicePrincipal. The owners are a set of non-admin users or servicePrincipals who are allowed to modify this object. Read-only. Nullable.  Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    @property
    def password_credentials(self,) -> Optional[List[password_credential.PasswordCredential]]:
        """
        Gets the passwordCredentials property value. The collection of password credentials associated with the application. Not nullable.
        Returns: Optional[List[password_credential.PasswordCredential]]
        """
        return self._password_credentials
    
    @password_credentials.setter
    def password_credentials(self,value: Optional[List[password_credential.PasswordCredential]] = None) -> None:
        """
        Sets the passwordCredentials property value. The collection of password credentials associated with the application. Not nullable.
        Args:
            value: Value to set for the passwordCredentials property.
        """
        self._password_credentials = value
    
    @property
    def preferred_single_sign_on_mode(self,) -> Optional[str]:
        """
        Gets the preferredSingleSignOnMode property value. Specifies the single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps. The supported values are password, saml, notSupported, and oidc.
        Returns: Optional[str]
        """
        return self._preferred_single_sign_on_mode
    
    @preferred_single_sign_on_mode.setter
    def preferred_single_sign_on_mode(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredSingleSignOnMode property value. Specifies the single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps. The supported values are password, saml, notSupported, and oidc.
        Args:
            value: Value to set for the preferredSingleSignOnMode property.
        """
        self._preferred_single_sign_on_mode = value
    
    @property
    def preferred_token_signing_key_thumbprint(self,) -> Optional[str]:
        """
        Gets the preferredTokenSigningKeyThumbprint property value. Reserved for internal use only. Do not write or otherwise rely on this property. May be removed in future versions.
        Returns: Optional[str]
        """
        return self._preferred_token_signing_key_thumbprint
    
    @preferred_token_signing_key_thumbprint.setter
    def preferred_token_signing_key_thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredTokenSigningKeyThumbprint property value. Reserved for internal use only. Do not write or otherwise rely on this property. May be removed in future versions.
        Args:
            value: Value to set for the preferredTokenSigningKeyThumbprint property.
        """
        self._preferred_token_signing_key_thumbprint = value
    
    @property
    def reply_urls(self,) -> Optional[List[str]]:
        """
        Gets the replyUrls property value. The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
        Returns: Optional[List[str]]
        """
        return self._reply_urls
    
    @reply_urls.setter
    def reply_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the replyUrls property value. The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
        Args:
            value: Value to set for the replyUrls property.
        """
        self._reply_urls = value
    
    @property
    def resource_specific_application_permissions(self,) -> Optional[List[resource_specific_permission.ResourceSpecificPermission]]:
        """
        Gets the resourceSpecificApplicationPermissions property value. The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.
        Returns: Optional[List[resource_specific_permission.ResourceSpecificPermission]]
        """
        return self._resource_specific_application_permissions
    
    @resource_specific_application_permissions.setter
    def resource_specific_application_permissions(self,value: Optional[List[resource_specific_permission.ResourceSpecificPermission]] = None) -> None:
        """
        Sets the resourceSpecificApplicationPermissions property value. The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.
        Args:
            value: Value to set for the resourceSpecificApplicationPermissions property.
        """
        self._resource_specific_application_permissions = value
    
    @property
    def saml_single_sign_on_settings(self,) -> Optional[saml_single_sign_on_settings.SamlSingleSignOnSettings]:
        """
        Gets the samlSingleSignOnSettings property value. The collection for settings related to saml single sign-on.
        Returns: Optional[saml_single_sign_on_settings.SamlSingleSignOnSettings]
        """
        return self._saml_single_sign_on_settings
    
    @saml_single_sign_on_settings.setter
    def saml_single_sign_on_settings(self,value: Optional[saml_single_sign_on_settings.SamlSingleSignOnSettings] = None) -> None:
        """
        Sets the samlSingleSignOnSettings property value. The collection for settings related to saml single sign-on.
        Args:
            value: Value to set for the samlSingleSignOnSettings property.
        """
        self._saml_single_sign_on_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_collection_of_primitive_values("alternativeNames", self.alternative_names)
        writer.write_str_value("appDescription", self.app_description)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
        writer.write_str_value("appOwnerOrganizationId", self.app_owner_organization_id)
        writer.write_collection_of_object_values("appRoleAssignedTo", self.app_role_assigned_to)
        writer.write_bool_value("appRoleAssignmentRequired", self.app_role_assignment_required)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("createdObjects", self.created_objects)
        writer.write_collection_of_object_values("delegatedPermissionClassifications", self.delegated_permission_classifications)
        writer.write_str_value("description", self.description)
        writer.write_str_value("disabledByMicrosoftStatus", self.disabled_by_microsoft_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("endpoints", self.endpoints)
        writer.write_collection_of_object_values("federatedIdentityCredentials", self.federated_identity_credentials)
        writer.write_str_value("homepage", self.homepage)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("info", self.info)
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_str_value("loginUrl", self.login_url)
        writer.write_str_value("logoutUrl", self.logout_url)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_str_value("notes", self.notes)
        writer.write_collection_of_primitive_values("notificationEmailAddresses", self.notification_email_addresses)
        writer.write_collection_of_object_values("oauth2PermissionGrants", self.oauth2_permission_grants)
        writer.write_collection_of_object_values("oauth2PermissionScopes", self.oauth2_permission_scopes)
        writer.write_collection_of_object_values("ownedObjects", self.owned_objects)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_str_value("preferredSingleSignOnMode", self.preferred_single_sign_on_mode)
        writer.write_str_value("preferredTokenSigningKeyThumbprint", self.preferred_token_signing_key_thumbprint)
        writer.write_collection_of_primitive_values("replyUrls", self.reply_urls)
        writer.write_collection_of_object_values("resourceSpecificApplicationPermissions", self.resource_specific_application_permissions)
        writer.write_object_value("samlSingleSignOnSettings", self.saml_single_sign_on_settings)
        writer.write_collection_of_primitive_values("servicePrincipalNames", self.service_principal_names)
        writer.write_str_value("servicePrincipalType", self.service_principal_type)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
    
    @property
    def service_principal_names(self,) -> Optional[List[str]]:
        """
        Gets the servicePrincipalNames property value. Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Azure AD. For example,Client apps can specify a resource URI which is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._service_principal_names
    
    @service_principal_names.setter
    def service_principal_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the servicePrincipalNames property value. Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Azure AD. For example,Client apps can specify a resource URI which is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the servicePrincipalNames property.
        """
        self._service_principal_names = value
    
    @property
    def service_principal_type(self,) -> Optional[str]:
        """
        Gets the servicePrincipalType property value. Identifies whether the service principal represents an application, a managed identity, or a legacy application. This is set by Azure AD internally. The servicePrincipalType property can be set to three different values: __Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens are not issued for the service principal.__ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but cannot be updated or modified directly.__Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. Legacy service principal can have credentials, service principal names, reply URLs, and other properties which are editable by an authorized user, but does not have an associated app registration. The appId value does not associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.__SocialIdp - For internal use.
        Returns: Optional[str]
        """
        return self._service_principal_type
    
    @service_principal_type.setter
    def service_principal_type(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalType property value. Identifies whether the service principal represents an application, a managed identity, or a legacy application. This is set by Azure AD internally. The servicePrincipalType property can be set to three different values: __Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens are not issued for the service principal.__ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but cannot be updated or modified directly.__Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. Legacy service principal can have credentials, service principal names, reply URLs, and other properties which are editable by an authorized user, but does not have an associated app registration. The appId value does not associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.__SocialIdp - For internal use.
        Args:
            value: Value to set for the servicePrincipalType property.
        """
        self._service_principal_type = value
    
    @property
    def sign_in_audience(self,) -> Optional[str]:
        """
        Gets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization’s Azure AD tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization’s Azure AD tenant (multi-tenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization’s Azure AD tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
        Returns: Optional[str]
        """
        return self._sign_in_audience
    
    @sign_in_audience.setter
    def sign_in_audience(self,value: Optional[str] = None) -> None:
        """
        Sets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization’s Azure AD tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization’s Azure AD tenant (multi-tenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization’s Azure AD tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
        Args:
            value: Value to set for the signInAudience property.
        """
        self._sign_in_audience = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Custom strings that can be used to categorize and identify the service principal. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Custom strings that can be used to categorize and identify the service principal. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def token_encryption_key_id(self,) -> Optional[str]:
        """
        Gets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Returns: Optional[str]
        """
        return self._token_encryption_key_id
    
    @token_encryption_key_id.setter
    def token_encryption_key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Args:
            value: Value to set for the tokenEncryptionKeyId property.
        """
        self._token_encryption_key_id = value
    
    @property
    def token_issuance_policies(self,) -> Optional[List[token_issuance_policy.TokenIssuancePolicy]]:
        """
        Gets the tokenIssuancePolicies property value. The tokenIssuancePolicies assigned to this service principal.
        Returns: Optional[List[token_issuance_policy.TokenIssuancePolicy]]
        """
        return self._token_issuance_policies
    
    @token_issuance_policies.setter
    def token_issuance_policies(self,value: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None) -> None:
        """
        Sets the tokenIssuancePolicies property value. The tokenIssuancePolicies assigned to this service principal.
        Args:
            value: Value to set for the tokenIssuancePolicies property.
        """
        self._token_issuance_policies = value
    
    @property
    def token_lifetime_policies(self,) -> Optional[List[token_lifetime_policy.TokenLifetimePolicy]]:
        """
        Gets the tokenLifetimePolicies property value. The tokenLifetimePolicies assigned to this service principal.
        Returns: Optional[List[token_lifetime_policy.TokenLifetimePolicy]]
        """
        return self._token_lifetime_policies
    
    @token_lifetime_policies.setter
    def token_lifetime_policies(self,value: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None) -> None:
        """
        Sets the tokenLifetimePolicies property value. The tokenLifetimePolicies assigned to this service principal.
        Args:
            value: Value to set for the tokenLifetimePolicies property.
        """
        self._token_lifetime_policies = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. The transitiveMemberOf property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. The transitiveMemberOf property
        Args:
            value: Value to set for the transitiveMemberOf property.
        """
        self._transitive_member_of = value
    
    @property
    def verified_publisher(self,) -> Optional[verified_publisher.VerifiedPublisher]:
        """
        Gets the verifiedPublisher property value. Specifies the verified publisher of the application which this service principal represents.
        Returns: Optional[verified_publisher.VerifiedPublisher]
        """
        return self._verified_publisher
    
    @verified_publisher.setter
    def verified_publisher(self,value: Optional[verified_publisher.VerifiedPublisher] = None) -> None:
        """
        Sets the verifiedPublisher property value. Specifies the verified publisher of the application which this service principal represents.
        Args:
            value: Value to set for the verifiedPublisher property.
        """
        self._verified_publisher = value
    

