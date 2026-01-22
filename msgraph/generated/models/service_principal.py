from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .add_in import AddIn
    from .app_management_policy import AppManagementPolicy
    from .app_role import AppRole
    from .app_role_assignment import AppRoleAssignment
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .custom_security_attribute_value import CustomSecurityAttributeValue
    from .delegated_permission_classification import DelegatedPermissionClassification
    from .directory_object import DirectoryObject
    from .endpoint import Endpoint
    from .federated_identity_credential import FederatedIdentityCredential
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .informational_url import InformationalUrl
    from .key_credential import KeyCredential
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .password_credential import PasswordCredential
    from .permission_scope import PermissionScope
    from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
    from .resource_specific_permission import ResourceSpecificPermission
    from .saml_single_sign_on_settings import SamlSingleSignOnSettings
    from .synchronization import Synchronization
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .verified_publisher import VerifiedPublisher

from .directory_object import DirectoryObject

@dataclass
class ServicePrincipal(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.servicePrincipal"
    # true if the service principal account is enabled; otherwise, false. If set to false, then no users are able to sign in to this app, even if they're assigned to it. Supports $filter (eq, ne, not, in).
    account_enabled: Optional[bool] = None
    # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.
    add_ins: Optional[list[AddIn]] = None
    # Used to retrieve service principals by subscription, identify resource group and full resource IDs for managed identities. Supports $filter (eq, not, ge, le, startsWith).
    alternative_names: Optional[list[str]] = None
    # The description exposed by the associated application.
    app_description: Optional[str] = None
    # The display name exposed by the associated application. Maximum length is 256 characters.
    app_display_name: Optional[str] = None
    # The unique identifier for the associated application (its appId property). Alternate key. Supports $filter (eq, ne, not, in, startsWith).
    app_id: Optional[str] = None
    # The appManagementPolicy applied to this application.
    app_management_policies: Optional[list[AppManagementPolicy]] = None
    # Contains the tenant ID where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
    app_owner_organization_id: Optional[UUID] = None
    # App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.
    app_role_assigned_to: Optional[list[AppRoleAssignment]] = None
    # Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
    app_role_assignment_required: Optional[bool] = None
    # App role assignment for another app or service, granted to this service principal. Supports $expand.
    app_role_assignments: Optional[list[AppRoleAssignment]] = None
    # The roles exposed by the application that's linked to this service principal. For more information, see the appRoles property definition on the application entity. Not nullable.
    app_roles: Optional[list[AppRole]] = None
    # Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the service principal wasn't created from an application template.
    application_template_id: Optional[str] = None
    # The claimsMappingPolicies assigned to this service principal. Supports $expand.
    claims_mapping_policies: Optional[list[ClaimsMappingPolicy]] = None
    # Directory objects created by this service principal. Read-only. Nullable.
    created_objects: Optional[list[DirectoryObject]] = None
    # An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.
    custom_security_attributes: Optional[CustomSecurityAttributeValue] = None
    # The delegatedPermissionClassifications property
    delegated_permission_classifications: Optional[list[DelegatedPermissionClassification]] = None
    # Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps displays the application description in this field. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    description: Optional[str] = None
    # Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    disabled_by_microsoft_status: Optional[str] = None
    # The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # The endpoints property
    endpoints: Optional[list[Endpoint]] = None
    # Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
    federated_identity_credentials: Optional[list[FederatedIdentityCredential]] = None
    # The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
    home_realm_discovery_policies: Optional[list[HomeRealmDiscoveryPolicy]] = None
    # Home page or landing page of the application.
    homepage: Optional[str] = None
    # Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    info: Optional[InformationalUrl] = None
    # The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
    key_credentials: Optional[list[KeyCredential]] = None
    # Specifies the URL where the service provider redirects the user to Microsoft Entra ID to authenticate. Microsoft Entra ID uses the URL to launch the application from Microsoft 365 or the Microsoft Entra My Apps. When blank, Microsoft Entra ID performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Microsoft Entra My Apps, or the Microsoft Entra SSO URL.
    login_url: Optional[str] = None
    # Specifies the URL that the Microsoft's authorization service uses to sign out a user using OpenID Connect front-channel, back-channel, or SAML sign out protocols.
    logout_url: Optional[str] = None
    # Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1,024 characters.
    notes: Optional[str] = None
    # Specifies the list of email addresses where Microsoft Entra ID sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Microsoft Entra Gallery applications.
    notification_email_addresses: Optional[list[str]] = None
    # Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
    oauth2_permission_grants: Optional[list[OAuth2PermissionGrant]] = None
    # The delegated permissions exposed by the application. For more information, see the oauth2PermissionScopes property on the application entity's api property. Not nullable.
    oauth2_permission_scopes: Optional[list[PermissionScope]] = None
    # Directory objects that this service principal owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_objects: Optional[list[DirectoryObject]] = None
    # Directory objects that are owners of this servicePrincipal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.
    owners: Optional[list[DirectoryObject]] = None
    # The collection of password credentials associated with the application. Not nullable.
    password_credentials: Optional[list[PasswordCredential]] = None
    # Specifies the single sign-on mode configured for this application. Microsoft Entra ID uses the preferred single sign-on mode to launch the application from Microsoft 365 or the My Apps portal. The supported values are password, saml, notSupported, and oidc. Note: This field might be null for older SAML apps and for OIDC applications where it isn't set automatically.
    preferred_single_sign_on_mode: Optional[str] = None
    # This property can be used on SAML applications (apps that have preferredSingleSignOnMode set to saml) to control which certificate is used to sign the SAML responses. For applications that aren't SAML, don't write or otherwise rely on this property.
    preferred_token_signing_key_thumbprint: Optional[str] = None
    # The remoteDesktopSecurityConfiguration object applied to this service principal. Supports $filter (eq) for isRemoteDesktopProtocolEnabled property.
    remote_desktop_security_configuration: Optional[RemoteDesktopSecurityConfiguration] = None
    # The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
    reply_urls: Optional[list[str]] = None
    # The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.
    resource_specific_application_permissions: Optional[list[ResourceSpecificPermission]] = None
    # The collection for settings related to saml single sign-on.
    saml_single_sign_on_settings: Optional[SamlSingleSignOnSettings] = None
    # Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. For example,Client apps can specify a resource URI that is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
    service_principal_names: Optional[list[str]] = None
    # Identifies whether the service principal represents an application, a managed identity, or a legacy application. This property is set by Microsoft Entra ID internally. The servicePrincipalType property can be set to three different values: Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens aren't issued for the service principal.ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but can't be updated or modified directly.Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. A legacy service principal can have credentials, service principal names, reply URLs, and other properties that are editable by an authorized user, but doesn't have an associated app registration. The appId value doesn't associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.ServiceIdentity - A service principal that represents an agent identity.SocialIdp - For internal use.
    service_principal_type: Optional[str] = None
    # Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
    sign_in_audience: Optional[str] = None
    # Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
    synchronization: Optional[Synchronization] = None
    # Custom strings that can be used to categorize and identify the service principal. Not nullable. The value is the union of strings set here and on the associated application entity's tags property.Supports $filter (eq, not, ge, le, startsWith).
    tags: Optional[list[str]] = None
    # Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    token_encryption_key_id: Optional[UUID] = None
    # The tokenIssuancePolicies assigned to this service principal.
    token_issuance_policies: Optional[list[TokenIssuancePolicy]] = None
    # The tokenLifetimePolicies assigned to this service principal.
    token_lifetime_policies: Optional[list[TokenLifetimePolicy]] = None
    # The transitiveMemberOf property
    transitive_member_of: Optional[list[DirectoryObject]] = None
    # Specifies the verified publisher of the application that's linked to this service principal.
    verified_publisher: Optional[VerifiedPublisher] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .add_in import AddIn
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .app_role_assignment import AppRoleAssignment
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .directory_object import DirectoryObject
        from .endpoint import Endpoint
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_credential import PasswordCredential
        from .permission_scope import PermissionScope
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .resource_specific_permission import ResourceSpecificPermission
        from .saml_single_sign_on_settings import SamlSingleSignOnSettings
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher

        from .add_in import AddIn
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .app_role_assignment import AppRoleAssignment
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .directory_object import DirectoryObject
        from .endpoint import Endpoint
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_credential import PasswordCredential
        from .permission_scope import PermissionScope
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .resource_specific_permission import ResourceSpecificPermission
        from .saml_single_sign_on_settings import SamlSingleSignOnSettings
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher

        fields: dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "addIns": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(AddIn)),
            "alternativeNames": lambda n : setattr(self, 'alternative_names', n.get_collection_of_primitive_values(str)),
            "appDescription": lambda n : setattr(self, 'app_description', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "appOwnerOrganizationId": lambda n : setattr(self, 'app_owner_organization_id', n.get_uuid_value()),
            "appRoleAssignedTo": lambda n : setattr(self, 'app_role_assigned_to', n.get_collection_of_object_values(AppRoleAssignment)),
            "appRoleAssignmentRequired": lambda n : setattr(self, 'app_role_assignment_required', n.get_bool_value()),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "appRoles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(AppRole)),
            "applicationTemplateId": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "claimsMappingPolicies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(ClaimsMappingPolicy)),
            "createdObjects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(DirectoryObject)),
            "customSecurityAttributes": lambda n : setattr(self, 'custom_security_attributes', n.get_object_value(CustomSecurityAttributeValue)),
            "delegatedPermissionClassifications": lambda n : setattr(self, 'delegated_permission_classifications', n.get_collection_of_object_values(DelegatedPermissionClassification)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabledByMicrosoftStatus": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(Endpoint)),
            "federatedIdentityCredentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(FederatedIdentityCredential)),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "homepage": lambda n : setattr(self, 'homepage', n.get_str_value()),
            "info": lambda n : setattr(self, 'info', n.get_object_value(InformationalUrl)),
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(KeyCredential)),
            "loginUrl": lambda n : setattr(self, 'login_url', n.get_str_value()),
            "logoutUrl": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "notificationEmailAddresses": lambda n : setattr(self, 'notification_email_addresses', n.get_collection_of_primitive_values(str)),
            "oauth2PermissionGrants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(OAuth2PermissionGrant)),
            "oauth2PermissionScopes": lambda n : setattr(self, 'oauth2_permission_scopes', n.get_collection_of_object_values(PermissionScope)),
            "ownedObjects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(DirectoryObject)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(DirectoryObject)),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(PasswordCredential)),
            "preferredSingleSignOnMode": lambda n : setattr(self, 'preferred_single_sign_on_mode', n.get_str_value()),
            "preferredTokenSigningKeyThumbprint": lambda n : setattr(self, 'preferred_token_signing_key_thumbprint', n.get_str_value()),
            "remoteDesktopSecurityConfiguration": lambda n : setattr(self, 'remote_desktop_security_configuration', n.get_object_value(RemoteDesktopSecurityConfiguration)),
            "replyUrls": lambda n : setattr(self, 'reply_urls', n.get_collection_of_primitive_values(str)),
            "resourceSpecificApplicationPermissions": lambda n : setattr(self, 'resource_specific_application_permissions', n.get_collection_of_object_values(ResourceSpecificPermission)),
            "samlSingleSignOnSettings": lambda n : setattr(self, 'saml_single_sign_on_settings', n.get_object_value(SamlSingleSignOnSettings)),
            "servicePrincipalNames": lambda n : setattr(self, 'service_principal_names', n.get_collection_of_primitive_values(str)),
            "servicePrincipalType": lambda n : setattr(self, 'service_principal_type', n.get_str_value()),
            "signInAudience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "synchronization": lambda n : setattr(self, 'synchronization', n.get_object_value(Synchronization)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_uuid_value()),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "verifiedPublisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(VerifiedPublisher)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_collection_of_primitive_values("alternativeNames", self.alternative_names)
        writer.write_str_value("appDescription", self.app_description)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_uuid_value("appOwnerOrganizationId", self.app_owner_organization_id)
        writer.write_collection_of_object_values("appRoleAssignedTo", self.app_role_assigned_to)
        writer.write_bool_value("appRoleAssignmentRequired", self.app_role_assignment_required)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("createdObjects", self.created_objects)
        writer.write_object_value("customSecurityAttributes", self.custom_security_attributes)
        writer.write_collection_of_object_values("delegatedPermissionClassifications", self.delegated_permission_classifications)
        writer.write_str_value("description", self.description)
        writer.write_str_value("disabledByMicrosoftStatus", self.disabled_by_microsoft_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("endpoints", self.endpoints)
        writer.write_collection_of_object_values("federatedIdentityCredentials", self.federated_identity_credentials)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_str_value("homepage", self.homepage)
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
        writer.write_object_value("remoteDesktopSecurityConfiguration", self.remote_desktop_security_configuration)
        writer.write_collection_of_primitive_values("replyUrls", self.reply_urls)
        writer.write_collection_of_object_values("resourceSpecificApplicationPermissions", self.resource_specific_application_permissions)
        writer.write_object_value("samlSingleSignOnSettings", self.saml_single_sign_on_settings)
        writer.write_collection_of_primitive_values("servicePrincipalNames", self.service_principal_names)
        writer.write_str_value("servicePrincipalType", self.service_principal_type)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("synchronization", self.synchronization)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_uuid_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
    

