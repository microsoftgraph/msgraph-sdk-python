from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import add_in, api_application, app_management_policy, app_role, certification, directory_object, extension_property, federated_identity_credential, home_realm_discovery_policy, informational_url, key_credential, optional_claims, parental_control_settings, password_credential, public_client_application, request_signature_verification, required_resource_access, spa_application, synchronization, token_issuance_policy, token_lifetime_policy, verified_publisher, web_application

from . import directory_object

@dataclass
class Application(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.application"
    # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Office 365 call the application in the context of a document the user is working on.
    add_ins: Optional[List[add_in.AddIn]] = None
    # Specifies settings for an application that implements a web API.
    api: Optional[api_application.ApiApplication] = None
    # The unique identifier for the application that is assigned to an application by Azure AD. Not nullable. Read-only. Supports $filter (eq).
    app_id: Optional[str] = None
    # The appManagementPolicy applied to this application.
    app_management_policies: Optional[List[app_management_policy.AppManagementPolicy]] = None
    # The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
    app_roles: Optional[List[app_role.AppRole]] = None
    # Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne).
    application_template_id: Optional[str] = None
    # Specifies the certification status of the application.
    certification: Optional[certification.Certification] = None
    # The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
    created_date_time: Optional[datetime] = None
    # Supports $filter (/$count eq 0, /$count ne 0). Read-only.
    created_on_behalf_of: Optional[directory_object.DirectoryObject] = None
    # The defaultRedirectUri property
    default_redirect_uri: Optional[str] = None
    # Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    description: Optional[str] = None
    # Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    disabled_by_microsoft_status: Optional[str] = None
    # The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
    display_name: Optional[str] = None
    # Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
    extension_properties: Optional[List[extension_property.ExtensionProperty]] = None
    # Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
    federated_identity_credentials: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None
    # Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all of the security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
    group_membership_claims: Optional[str] = None
    # The homeRealmDiscoveryPolicies property
    home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
    # Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
    identifier_uris: Optional[List[str]] = None
    # Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    info: Optional[informational_url.InformationalUrl] = None
    # Specifies whether this application supports device authentication without a user. The default is false.
    is_device_only_auth_supported: Optional[bool] = None
    # Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where it is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
    is_fallback_public_client: Optional[bool] = None
    # The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
    key_credentials: Optional[List[key_credential.KeyCredential]] = None
    # The main logo for the application. Not nullable.
    logo: Optional[bytes] = None
    # Notes relevant for the management of the application.
    notes: Optional[str] = None
    # The oauth2RequirePostResponse property
    oauth2_require_post_response: Optional[bool] = None
    # Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
    optional_claims: Optional[optional_claims.OptionalClaims] = None
    # Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owners: Optional[List[directory_object.DirectoryObject]] = None
    # Specifies parental control settings for an application.
    parental_control_settings: Optional[parental_control_settings.ParentalControlSettings] = None
    # The collection of password credentials associated with the application. Not nullable.
    password_credentials: Optional[List[password_credential.PasswordCredential]] = None
    # Specifies settings for installed clients such as desktop or mobile devices.
    public_client: Optional[public_client_application.PublicClientApplication] = None
    # The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
    publisher_domain: Optional[str] = None
    # Specifies whether this application requires Azure AD to verify the signed authentication requests.
    request_signature_verification: Optional[request_signature_verification.RequestSignatureVerification] = None
    # Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
    required_resource_access: Optional[List[required_resource_access.RequiredResourceAccess]] = None
    # The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
    saml_metadata_url: Optional[str] = None
    # References application or service contact information from a Service or Asset Management database. Nullable.
    service_management_reference: Optional[str] = None
    # Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
    sign_in_audience: Optional[str] = None
    # Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
    spa: Optional[spa_application.SpaApplication] = None
    # The synchronization property
    synchronization: Optional[synchronization.Synchronization] = None
    # Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
    tags: Optional[List[str]] = None
    # Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    token_encryption_key_id: Optional[UUID] = None
    # The tokenIssuancePolicies property
    token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
    # The tokenLifetimePolicies property
    token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
    # Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
    verified_publisher: Optional[verified_publisher.VerifiedPublisher] = None
    # Specifies settings for a web application.
    web: Optional[web_application.WebApplication] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Application:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Application
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Application()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_in, api_application, app_management_policy, app_role, certification, directory_object, extension_property, federated_identity_credential, home_realm_discovery_policy, informational_url, key_credential, optional_claims, parental_control_settings, password_credential, public_client_application, request_signature_verification, required_resource_access, spa_application, synchronization, token_issuance_policy, token_lifetime_policy, verified_publisher, web_application

        from . import add_in, api_application, app_management_policy, app_role, certification, directory_object, extension_property, federated_identity_credential, home_realm_discovery_policy, informational_url, key_credential, optional_claims, parental_control_settings, password_credential, public_client_application, request_signature_verification, required_resource_access, spa_application, synchronization, token_issuance_policy, token_lifetime_policy, verified_publisher, web_application

        fields: Dict[str, Callable[[Any], None]] = {
            "addIns": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(add_in.AddIn)),
            "api": lambda n : setattr(self, 'api', n.get_object_value(api_application.ApiApplication)),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(app_management_policy.AppManagementPolicy)),
            "appRoles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(app_role.AppRole)),
            "applicationTemplateId": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "certification": lambda n : setattr(self, 'certification', n.get_object_value(certification.Certification)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdOnBehalfOf": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(directory_object.DirectoryObject)),
            "defaultRedirectUri": lambda n : setattr(self, 'default_redirect_uri', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabledByMicrosoftStatus": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensionProperties": lambda n : setattr(self, 'extension_properties', n.get_collection_of_object_values(extension_property.ExtensionProperty)),
            "federatedIdentityCredentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(federated_identity_credential.FederatedIdentityCredential)),
            "groupMembershipClaims": lambda n : setattr(self, 'group_membership_claims', n.get_str_value()),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identifierUris": lambda n : setattr(self, 'identifier_uris', n.get_collection_of_primitive_values(str)),
            "info": lambda n : setattr(self, 'info', n.get_object_value(informational_url.InformationalUrl)),
            "isDeviceOnlyAuthSupported": lambda n : setattr(self, 'is_device_only_auth_supported', n.get_bool_value()),
            "isFallbackPublicClient": lambda n : setattr(self, 'is_fallback_public_client', n.get_bool_value()),
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(key_credential.KeyCredential)),
            "logo": lambda n : setattr(self, 'logo', n.get_bytes_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "oauth2RequirePostResponse": lambda n : setattr(self, 'oauth2_require_post_response', n.get_bool_value()),
            "optionalClaims": lambda n : setattr(self, 'optional_claims', n.get_object_value(optional_claims.OptionalClaims)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "parentalControlSettings": lambda n : setattr(self, 'parental_control_settings', n.get_object_value(parental_control_settings.ParentalControlSettings)),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(password_credential.PasswordCredential)),
            "publicClient": lambda n : setattr(self, 'public_client', n.get_object_value(public_client_application.PublicClientApplication)),
            "publisherDomain": lambda n : setattr(self, 'publisher_domain', n.get_str_value()),
            "requestSignatureVerification": lambda n : setattr(self, 'request_signature_verification', n.get_object_value(request_signature_verification.RequestSignatureVerification)),
            "requiredResourceAccess": lambda n : setattr(self, 'required_resource_access', n.get_collection_of_object_values(required_resource_access.RequiredResourceAccess)),
            "samlMetadataUrl": lambda n : setattr(self, 'saml_metadata_url', n.get_str_value()),
            "serviceManagementReference": lambda n : setattr(self, 'service_management_reference', n.get_str_value()),
            "signInAudience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(spa_application.SpaApplication)),
            "synchronization": lambda n : setattr(self, 'synchronization', n.get_object_value(synchronization.Synchronization)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_uuid_value()),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
            "verifiedPublisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(verified_publisher.VerifiedPublisher)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(web_application.WebApplication)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_object_value("api", self.api)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
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
        writer.write_object_value("logo", self.logo)
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
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("spa", self.spa)
        writer.write_object_value("synchronization", self.synchronization)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_uuid_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
        writer.write_object_value("web", self.web)
    

