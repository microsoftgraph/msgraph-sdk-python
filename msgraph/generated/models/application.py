from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .add_in import AddIn
    from .api_application import ApiApplication
    from .app_management_policy import AppManagementPolicy
    from .app_role import AppRole
    from .authentication_behaviors import AuthenticationBehaviors
    from .certification import Certification
    from .directory_object import DirectoryObject
    from .extension_property import ExtensionProperty
    from .federated_identity_credential import FederatedIdentityCredential
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .informational_url import InformationalUrl
    from .key_credential import KeyCredential
    from .native_authentication_apis_enabled import NativeAuthenticationApisEnabled
    from .optional_claims import OptionalClaims
    from .parental_control_settings import ParentalControlSettings
    from .password_credential import PasswordCredential
    from .public_client_application import PublicClientApplication
    from .request_signature_verification import RequestSignatureVerification
    from .required_resource_access import RequiredResourceAccess
    from .service_principal_lock_configuration import ServicePrincipalLockConfiguration
    from .spa_application import SpaApplication
    from .synchronization import Synchronization
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .verified_publisher import VerifiedPublisher
    from .web_application import WebApplication

from .directory_object import DirectoryObject

@dataclass
class Application(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.application"
    # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.
    add_ins: Optional[list[AddIn]] = None
    # Specifies settings for an application that implements a web API.
    api: Optional[ApiApplication] = None
    # The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).
    app_id: Optional[str] = None
    # The appManagementPolicy applied to this application.
    app_management_policies: Optional[list[AppManagementPolicy]] = None
    # The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
    app_roles: Optional[list[AppRole]] = None
    # Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.
    application_template_id: Optional[str] = None
    # The authenticationBehaviors property
    authentication_behaviors: Optional[AuthenticationBehaviors] = None
    # Specifies the certification status of the application.
    certification: Optional[Certification] = None
    # The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # Supports $filter (/$count eq 0, /$count ne 0). Read-only.
    created_on_behalf_of: Optional[DirectoryObject] = None
    # The defaultRedirectUri property
    default_redirect_uri: Optional[str] = None
    # Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    description: Optional[str] = None
    # Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    disabled_by_microsoft_status: Optional[str] = None
    # The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
    extension_properties: Optional[list[ExtensionProperty]] = None
    # Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
    federated_identity_credentials: Optional[list[FederatedIdentityCredential]] = None
    # Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).
    group_membership_claims: Optional[str] = None
    # The homeRealmDiscoveryPolicies property
    home_realm_discovery_policies: Optional[list[HomeRealmDiscoveryPolicy]] = None
    # Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
    identifier_uris: Optional[list[str]] = None
    # Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    info: Optional[InformationalUrl] = None
    # Specifies whether this application supports device authentication without a user. The default is false.
    is_device_only_auth_supported: Optional[bool] = None
    # Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.
    is_fallback_public_client: Optional[bool] = None
    # The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
    key_credentials: Optional[list[KeyCredential]] = None
    # The main logo for the application. Not nullable.
    logo: Optional[bytes] = None
    # Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.
    native_authentication_apis_enabled: Optional[NativeAuthenticationApisEnabled] = None
    # Notes relevant for the management of the application.
    notes: Optional[str] = None
    # The oauth2RequirePostResponse property
    oauth2_require_post_response: Optional[bool] = None
    # Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
    optional_claims: Optional[OptionalClaims] = None
    # Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.
    owners: Optional[list[DirectoryObject]] = None
    # Specifies parental control settings for an application.
    parental_control_settings: Optional[ParentalControlSettings] = None
    # The collection of password credentials associated with the application. Not nullable.
    password_credentials: Optional[list[PasswordCredential]] = None
    # Specifies settings for installed clients such as desktop or mobile devices.
    public_client: Optional[PublicClientApplication] = None
    # The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
    publisher_domain: Optional[str] = None
    # Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.
    request_signature_verification: Optional[RequestSignatureVerification] = None
    # Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
    required_resource_access: Optional[list[RequiredResourceAccess]] = None
    # The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
    saml_metadata_url: Optional[str] = None
    # References application or service contact information from a Service or Asset Management database. Nullable.
    service_management_reference: Optional[str] = None
    # Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.
    service_principal_lock_configuration: Optional[ServicePrincipalLockConfiguration] = None
    # Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
    sign_in_audience: Optional[str] = None
    # Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
    spa: Optional[SpaApplication] = None
    # Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
    synchronization: Optional[Synchronization] = None
    # Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
    tags: Optional[list[str]] = None
    # Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    token_encryption_key_id: Optional[UUID] = None
    # The tokenIssuancePolicies property
    token_issuance_policies: Optional[list[TokenIssuancePolicy]] = None
    # The tokenLifetimePolicies property
    token_lifetime_policies: Optional[list[TokenLifetimePolicy]] = None
    # The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.
    unique_name: Optional[str] = None
    # Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
    verified_publisher: Optional[VerifiedPublisher] = None
    # Specifies settings for a web application.
    web: Optional[WebApplication] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Application:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Application
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Application()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .add_in import AddIn
        from .api_application import ApiApplication
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .authentication_behaviors import AuthenticationBehaviors
        from .certification import Certification
        from .directory_object import DirectoryObject
        from .extension_property import ExtensionProperty
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .native_authentication_apis_enabled import NativeAuthenticationApisEnabled
        from .optional_claims import OptionalClaims
        from .parental_control_settings import ParentalControlSettings
        from .password_credential import PasswordCredential
        from .public_client_application import PublicClientApplication
        from .request_signature_verification import RequestSignatureVerification
        from .required_resource_access import RequiredResourceAccess
        from .service_principal_lock_configuration import ServicePrincipalLockConfiguration
        from .spa_application import SpaApplication
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher
        from .web_application import WebApplication

        from .add_in import AddIn
        from .api_application import ApiApplication
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .authentication_behaviors import AuthenticationBehaviors
        from .certification import Certification
        from .directory_object import DirectoryObject
        from .extension_property import ExtensionProperty
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .native_authentication_apis_enabled import NativeAuthenticationApisEnabled
        from .optional_claims import OptionalClaims
        from .parental_control_settings import ParentalControlSettings
        from .password_credential import PasswordCredential
        from .public_client_application import PublicClientApplication
        from .request_signature_verification import RequestSignatureVerification
        from .required_resource_access import RequiredResourceAccess
        from .service_principal_lock_configuration import ServicePrincipalLockConfiguration
        from .spa_application import SpaApplication
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher
        from .web_application import WebApplication

        fields: dict[str, Callable[[Any], None]] = {
            "addIns": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(AddIn)),
            "api": lambda n : setattr(self, 'api', n.get_object_value(ApiApplication)),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "appRoles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(AppRole)),
            "applicationTemplateId": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "authenticationBehaviors": lambda n : setattr(self, 'authentication_behaviors', n.get_object_value(AuthenticationBehaviors)),
            "certification": lambda n : setattr(self, 'certification', n.get_object_value(Certification)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdOnBehalfOf": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(DirectoryObject)),
            "defaultRedirectUri": lambda n : setattr(self, 'default_redirect_uri', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabledByMicrosoftStatus": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensionProperties": lambda n : setattr(self, 'extension_properties', n.get_collection_of_object_values(ExtensionProperty)),
            "federatedIdentityCredentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(FederatedIdentityCredential)),
            "groupMembershipClaims": lambda n : setattr(self, 'group_membership_claims', n.get_str_value()),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "identifierUris": lambda n : setattr(self, 'identifier_uris', n.get_collection_of_primitive_values(str)),
            "info": lambda n : setattr(self, 'info', n.get_object_value(InformationalUrl)),
            "isDeviceOnlyAuthSupported": lambda n : setattr(self, 'is_device_only_auth_supported', n.get_bool_value()),
            "isFallbackPublicClient": lambda n : setattr(self, 'is_fallback_public_client', n.get_bool_value()),
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(KeyCredential)),
            "logo": lambda n : setattr(self, 'logo', n.get_bytes_value()),
            "nativeAuthenticationApisEnabled": lambda n : setattr(self, 'native_authentication_apis_enabled', n.get_collection_of_enum_values(NativeAuthenticationApisEnabled)),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "oauth2RequirePostResponse": lambda n : setattr(self, 'oauth2_require_post_response', n.get_bool_value()),
            "optionalClaims": lambda n : setattr(self, 'optional_claims', n.get_object_value(OptionalClaims)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(DirectoryObject)),
            "parentalControlSettings": lambda n : setattr(self, 'parental_control_settings', n.get_object_value(ParentalControlSettings)),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(PasswordCredential)),
            "publicClient": lambda n : setattr(self, 'public_client', n.get_object_value(PublicClientApplication)),
            "publisherDomain": lambda n : setattr(self, 'publisher_domain', n.get_str_value()),
            "requestSignatureVerification": lambda n : setattr(self, 'request_signature_verification', n.get_object_value(RequestSignatureVerification)),
            "requiredResourceAccess": lambda n : setattr(self, 'required_resource_access', n.get_collection_of_object_values(RequiredResourceAccess)),
            "samlMetadataUrl": lambda n : setattr(self, 'saml_metadata_url', n.get_str_value()),
            "serviceManagementReference": lambda n : setattr(self, 'service_management_reference', n.get_str_value()),
            "servicePrincipalLockConfiguration": lambda n : setattr(self, 'service_principal_lock_configuration', n.get_object_value(ServicePrincipalLockConfiguration)),
            "signInAudience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(SpaApplication)),
            "synchronization": lambda n : setattr(self, 'synchronization', n.get_object_value(Synchronization)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_uuid_value()),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
            "verifiedPublisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(VerifiedPublisher)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(WebApplication)),
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
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_object_value("api", self.api)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
        writer.write_object_value("authenticationBehaviors", self.authentication_behaviors)
        writer.write_object_value("certification", self.certification)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("createdOnBehalfOf", self.created_on_behalf_of)
        writer.write_str_value("defaultRedirectUri", self.default_redirect_uri)
        writer.write_str_value("description", self.description)
        writer.write_str_value("disabledByMicrosoftStatus", self.disabled_by_microsoft_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensionProperties", self.extension_properties)
        writer.write_collection_of_object_values("federatedIdentityCredentials", self.federated_identity_credentials)
        writer.write_str_value("groupMembershipClaims", self.group_membership_claims)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_collection_of_primitive_values("identifierUris", self.identifier_uris)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isDeviceOnlyAuthSupported", self.is_device_only_auth_supported)
        writer.write_bool_value("isFallbackPublicClient", self.is_fallback_public_client)
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_bytes_value("logo", self.logo)
        writer.write_enum_value("nativeAuthenticationApisEnabled", self.native_authentication_apis_enabled)
        writer.write_str_value("notes", self.notes)
        writer.write_bool_value("oauth2RequirePostResponse", self.oauth2_require_post_response)
        writer.write_object_value("optionalClaims", self.optional_claims)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_object_value("parentalControlSettings", self.parental_control_settings)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_object_value("publicClient", self.public_client)
        writer.write_str_value("publisherDomain", self.publisher_domain)
        writer.write_object_value("requestSignatureVerification", self.request_signature_verification)
        writer.write_collection_of_object_values("requiredResourceAccess", self.required_resource_access)
        writer.write_str_value("samlMetadataUrl", self.saml_metadata_url)
        writer.write_str_value("serviceManagementReference", self.service_management_reference)
        writer.write_object_value("servicePrincipalLockConfiguration", self.service_principal_lock_configuration)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("spa", self.spa)
        writer.write_object_value("synchronization", self.synchronization)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_uuid_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_str_value("uniqueName", self.unique_name)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
        writer.write_object_value("web", self.web)
    

