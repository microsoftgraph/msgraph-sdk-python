from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

add_in = lazy_import('msgraph.generated.models.add_in')
api_application = lazy_import('msgraph.generated.models.api_application')
app_role = lazy_import('msgraph.generated.models.app_role')
certification = lazy_import('msgraph.generated.models.certification')
directory_object = lazy_import('msgraph.generated.models.directory_object')
extension_property = lazy_import('msgraph.generated.models.extension_property')
federated_identity_credential = lazy_import('msgraph.generated.models.federated_identity_credential')
home_realm_discovery_policy = lazy_import('msgraph.generated.models.home_realm_discovery_policy')
informational_url = lazy_import('msgraph.generated.models.informational_url')
key_credential = lazy_import('msgraph.generated.models.key_credential')
optional_claims = lazy_import('msgraph.generated.models.optional_claims')
parental_control_settings = lazy_import('msgraph.generated.models.parental_control_settings')
password_credential = lazy_import('msgraph.generated.models.password_credential')
public_client_application = lazy_import('msgraph.generated.models.public_client_application')
required_resource_access = lazy_import('msgraph.generated.models.required_resource_access')
spa_application = lazy_import('msgraph.generated.models.spa_application')
token_issuance_policy = lazy_import('msgraph.generated.models.token_issuance_policy')
token_lifetime_policy = lazy_import('msgraph.generated.models.token_lifetime_policy')
verified_publisher = lazy_import('msgraph.generated.models.verified_publisher')
web_application = lazy_import('msgraph.generated.models.web_application')

class Application(directory_object.DirectoryObject):
    """
    Provides operations to manage the collection of application entities.
    """
    @property
    def add_ins(self,) -> Optional[List[add_in.AddIn]]:
        """
        Gets the addIns property value. Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Office 365 call the application in the context of a document the user is working on.
        Returns: Optional[List[add_in.AddIn]]
        """
        return self._add_ins
    
    @add_ins.setter
    def add_ins(self,value: Optional[List[add_in.AddIn]] = None) -> None:
        """
        Sets the addIns property value. Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Office 365 call the application in the context of a document the user is working on.
        Args:
            value: Value to set for the addIns property.
        """
        self._add_ins = value
    
    @property
    def api(self,) -> Optional[api_application.ApiApplication]:
        """
        Gets the api property value. Specifies settings for an application that implements a web API.
        Returns: Optional[api_application.ApiApplication]
        """
        return self._api
    
    @api.setter
    def api(self,value: Optional[api_application.ApiApplication] = None) -> None:
        """
        Sets the api property value. Specifies settings for an application that implements a web API.
        Args:
            value: Value to set for the api property.
        """
        self._api = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The unique identifier for the application that is assigned to an application by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The unique identifier for the application that is assigned to an application by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def application_template_id(self,) -> Optional[str]:
        """
        Gets the applicationTemplateId property value. Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne).
        Returns: Optional[str]
        """
        return self._application_template_id
    
    @application_template_id.setter
    def application_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationTemplateId property value. Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne).
        Args:
            value: Value to set for the applicationTemplateId property.
        """
        self._application_template_id = value
    
    @property
    def app_roles(self,) -> Optional[List[app_role.AppRole]]:
        """
        Gets the appRoles property value. The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        Returns: Optional[List[app_role.AppRole]]
        """
        return self._app_roles
    
    @app_roles.setter
    def app_roles(self,value: Optional[List[app_role.AppRole]] = None) -> None:
        """
        Sets the appRoles property value. The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        Args:
            value: Value to set for the appRoles property.
        """
        self._app_roles = value
    
    @property
    def certification(self,) -> Optional[certification.Certification]:
        """
        Gets the certification property value. Specifies the certification status of the application.
        Returns: Optional[certification.Certification]
        """
        return self._certification
    
    @certification.setter
    def certification(self,value: Optional[certification.Certification] = None) -> None:
        """
        Sets the certification property value. Specifies the certification status of the application.
        Args:
            value: Value to set for the certification property.
        """
        self._certification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new application and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.application"
        # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Office 365 call the application in the context of a document the user is working on.
        self._add_ins: Optional[List[add_in.AddIn]] = None
        # Specifies settings for an application that implements a web API.
        self._api: Optional[api_application.ApiApplication] = None
        # The unique identifier for the application that is assigned to an application by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        self._app_id: Optional[str] = None
        # Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne).
        self._application_template_id: Optional[str] = None
        # The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        self._app_roles: Optional[List[app_role.AppRole]] = None
        # Specifies the certification status of the application.
        self._certification: Optional[certification.Certification] = None
        # The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        self._created_date_time: Optional[datetime] = None
        # Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        self._created_on_behalf_of: Optional[directory_object.DirectoryObject] = None
        # The defaultRedirectUri property
        self._default_redirect_uri: Optional[str] = None
        # Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        self._description: Optional[str] = None
        # Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        self._disabled_by_microsoft_status: Optional[str] = None
        # The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        self._extension_properties: Optional[List[extension_property.ExtensionProperty]] = None
        # Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
        self._federated_identity_credentials: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None
        # Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all of the security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        self._group_membership_claims: Optional[str] = None
        # The homeRealmDiscoveryPolicies property
        self._home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
        # Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        self._identifier_uris: Optional[List[str]] = None
        # Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        self._info: Optional[informational_url.InformationalUrl] = None
        # Specifies whether this application supports device authentication without a user. The default is false.
        self._is_device_only_auth_supported: Optional[bool] = None
        # Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where it is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        self._is_fallback_public_client: Optional[bool] = None
        # The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        self._key_credentials: Optional[List[key_credential.KeyCredential]] = None
        # The main logo for the application. Not nullable.
        self._logo: Optional[bytes] = None
        # Notes relevant for the management of the application.
        self._notes: Optional[str] = None
        # The oauth2RequirePostResponse property
        self._oauth2_require_post_response: Optional[bool] = None
        # Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        self._optional_claims: Optional[optional_claims.OptionalClaims] = None
        # Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        self._owners: Optional[List[directory_object.DirectoryObject]] = None
        # Specifies parental control settings for an application.
        self._parental_control_settings: Optional[parental_control_settings.ParentalControlSettings] = None
        # The collection of password credentials associated with the application. Not nullable.
        self._password_credentials: Optional[List[password_credential.PasswordCredential]] = None
        # Specifies settings for installed clients such as desktop or mobile devices.
        self._public_client: Optional[public_client_application.PublicClientApplication] = None
        # The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
        self._publisher_domain: Optional[str] = None
        # Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        self._required_resource_access: Optional[List[required_resource_access.RequiredResourceAccess]] = None
        # The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        self._saml_metadata_url: Optional[str] = None
        # References application or service contact information from a Service or Asset Management database. Nullable.
        self._service_management_reference: Optional[str] = None
        # Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        self._sign_in_audience: Optional[str] = None
        # Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        self._spa: Optional[spa_application.SpaApplication] = None
        # Custom strings that can be used to categorize and identify the application. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        self._tags: Optional[List[str]] = None
        # Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        self._token_encryption_key_id: Optional[str] = None
        # The tokenIssuancePolicies property
        self._token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
        # The tokenLifetimePolicies property
        self._token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
        # Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        self._verified_publisher: Optional[verified_publisher.VerifiedPublisher] = None
        # Specifies settings for a web application.
        self._web: Optional[web_application.WebApplication] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @property
    def created_on_behalf_of(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the createdOnBehalfOf property value. Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._created_on_behalf_of
    
    @created_on_behalf_of.setter
    def created_on_behalf_of(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the createdOnBehalfOf property value. Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        Args:
            value: Value to set for the createdOnBehalfOf property.
        """
        self._created_on_behalf_of = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Application:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Application
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Application()
    
    @property
    def default_redirect_uri(self,) -> Optional[str]:
        """
        Gets the defaultRedirectUri property value. The defaultRedirectUri property
        Returns: Optional[str]
        """
        return self._default_redirect_uri
    
    @default_redirect_uri.setter
    def default_redirect_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultRedirectUri property value. The defaultRedirectUri property
        Args:
            value: Value to set for the defaultRedirectUri property.
        """
        self._default_redirect_uri = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
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
        Gets the displayName property value. The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def extension_properties(self,) -> Optional[List[extension_property.ExtensionProperty]]:
        """
        Gets the extensionProperties property value. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Returns: Optional[List[extension_property.ExtensionProperty]]
        """
        return self._extension_properties
    
    @extension_properties.setter
    def extension_properties(self,value: Optional[List[extension_property.ExtensionProperty]] = None) -> None:
        """
        Sets the extensionProperties property value. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the extensionProperties property.
        """
        self._extension_properties = value
    
    @property
    def federated_identity_credentials(self,) -> Optional[List[federated_identity_credential.FederatedIdentityCredential]]:
        """
        Gets the federatedIdentityCredentials property value. Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
        Returns: Optional[List[federated_identity_credential.FederatedIdentityCredential]]
        """
        return self._federated_identity_credentials
    
    @federated_identity_credentials.setter
    def federated_identity_credentials(self,value: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None) -> None:
        """
        Sets the federatedIdentityCredentials property value. Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
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
            "add_ins": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(add_in.AddIn)),
            "api": lambda n : setattr(self, 'api', n.get_object_value(api_application.ApiApplication)),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "application_template_id": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "app_roles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(app_role.AppRole)),
            "certification": lambda n : setattr(self, 'certification', n.get_object_value(certification.Certification)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "created_on_behalf_of": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(directory_object.DirectoryObject)),
            "default_redirect_uri": lambda n : setattr(self, 'default_redirect_uri', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabled_by_microsoft_status": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extension_properties": lambda n : setattr(self, 'extension_properties', n.get_collection_of_object_values(extension_property.ExtensionProperty)),
            "federated_identity_credentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(federated_identity_credential.FederatedIdentityCredential)),
            "group_membership_claims": lambda n : setattr(self, 'group_membership_claims', n.get_str_value()),
            "home_realm_discovery_policies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identifier_uris": lambda n : setattr(self, 'identifier_uris', n.get_collection_of_primitive_values(str)),
            "info": lambda n : setattr(self, 'info', n.get_object_value(informational_url.InformationalUrl)),
            "is_device_only_auth_supported": lambda n : setattr(self, 'is_device_only_auth_supported', n.get_bool_value()),
            "is_fallback_public_client": lambda n : setattr(self, 'is_fallback_public_client', n.get_bool_value()),
            "key_credentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(key_credential.KeyCredential)),
            "logo": lambda n : setattr(self, 'logo', n.get_bytes_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "oauth2_require_post_response": lambda n : setattr(self, 'oauth2_require_post_response', n.get_bool_value()),
            "optional_claims": lambda n : setattr(self, 'optional_claims', n.get_object_value(optional_claims.OptionalClaims)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "parental_control_settings": lambda n : setattr(self, 'parental_control_settings', n.get_object_value(parental_control_settings.ParentalControlSettings)),
            "password_credentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(password_credential.PasswordCredential)),
            "public_client": lambda n : setattr(self, 'public_client', n.get_object_value(public_client_application.PublicClientApplication)),
            "publisher_domain": lambda n : setattr(self, 'publisher_domain', n.get_str_value()),
            "required_resource_access": lambda n : setattr(self, 'required_resource_access', n.get_collection_of_object_values(required_resource_access.RequiredResourceAccess)),
            "saml_metadata_url": lambda n : setattr(self, 'saml_metadata_url', n.get_str_value()),
            "service_management_reference": lambda n : setattr(self, 'service_management_reference', n.get_str_value()),
            "sign_in_audience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(spa_application.SpaApplication)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "token_encryption_key_id": lambda n : setattr(self, 'token_encryption_key_id', n.get_str_value()),
            "token_issuance_policies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "token_lifetime_policies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
            "verified_publisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(verified_publisher.VerifiedPublisher)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(web_application.WebApplication)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_membership_claims(self,) -> Optional[str]:
        """
        Gets the groupMembershipClaims property value. Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all of the security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        Returns: Optional[str]
        """
        return self._group_membership_claims
    
    @group_membership_claims.setter
    def group_membership_claims(self,value: Optional[str] = None) -> None:
        """
        Sets the groupMembershipClaims property value. Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all of the security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        Args:
            value: Value to set for the groupMembershipClaims property.
        """
        self._group_membership_claims = value
    
    @property
    def home_realm_discovery_policies(self,) -> Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]:
        """
        Gets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies property
        Returns: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]
        """
        return self._home_realm_discovery_policies
    
    @home_realm_discovery_policies.setter
    def home_realm_discovery_policies(self,value: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None) -> None:
        """
        Sets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies property
        Args:
            value: Value to set for the homeRealmDiscoveryPolicies property.
        """
        self._home_realm_discovery_policies = value
    
    @property
    def identifier_uris(self,) -> Optional[List[str]]:
        """
        Gets the identifierUris property value. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._identifier_uris
    
    @identifier_uris.setter
    def identifier_uris(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the identifierUris property value. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        Args:
            value: Value to set for the identifierUris property.
        """
        self._identifier_uris = value
    
    @property
    def info(self,) -> Optional[informational_url.InformationalUrl]:
        """
        Gets the info property value. Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Returns: Optional[informational_url.InformationalUrl]
        """
        return self._info
    
    @info.setter
    def info(self,value: Optional[informational_url.InformationalUrl] = None) -> None:
        """
        Sets the info property value. Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Args:
            value: Value to set for the info property.
        """
        self._info = value
    
    @property
    def is_device_only_auth_supported(self,) -> Optional[bool]:
        """
        Gets the isDeviceOnlyAuthSupported property value. Specifies whether this application supports device authentication without a user. The default is false.
        Returns: Optional[bool]
        """
        return self._is_device_only_auth_supported
    
    @is_device_only_auth_supported.setter
    def is_device_only_auth_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeviceOnlyAuthSupported property value. Specifies whether this application supports device authentication without a user. The default is false.
        Args:
            value: Value to set for the isDeviceOnlyAuthSupported property.
        """
        self._is_device_only_auth_supported = value
    
    @property
    def is_fallback_public_client(self,) -> Optional[bool]:
        """
        Gets the isFallbackPublicClient property value. Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where it is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        Returns: Optional[bool]
        """
        return self._is_fallback_public_client
    
    @is_fallback_public_client.setter
    def is_fallback_public_client(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFallbackPublicClient property value. Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where it is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        Args:
            value: Value to set for the isFallbackPublicClient property.
        """
        self._is_fallback_public_client = value
    
    @property
    def key_credentials(self,) -> Optional[List[key_credential.KeyCredential]]:
        """
        Gets the keyCredentials property value. The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[key_credential.KeyCredential]]
        """
        return self._key_credentials
    
    @key_credentials.setter
    def key_credentials(self,value: Optional[List[key_credential.KeyCredential]] = None) -> None:
        """
        Sets the keyCredentials property value. The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the keyCredentials property.
        """
        self._key_credentials = value
    
    @property
    def logo(self,) -> Optional[bytes]:
        """
        Gets the logo property value. The main logo for the application. Not nullable.
        Returns: Optional[bytes]
        """
        return self._logo
    
    @logo.setter
    def logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the logo property value. The main logo for the application. Not nullable.
        Args:
            value: Value to set for the logo property.
        """
        self._logo = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes relevant for the management of the application.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes relevant for the management of the application.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def oauth2_require_post_response(self,) -> Optional[bool]:
        """
        Gets the oauth2RequirePostResponse property value. The oauth2RequirePostResponse property
        Returns: Optional[bool]
        """
        return self._oauth2_require_post_response
    
    @oauth2_require_post_response.setter
    def oauth2_require_post_response(self,value: Optional[bool] = None) -> None:
        """
        Sets the oauth2RequirePostResponse property value. The oauth2RequirePostResponse property
        Args:
            value: Value to set for the oauth2RequirePostResponse property.
        """
        self._oauth2_require_post_response = value
    
    @property
    def optional_claims(self,) -> Optional[optional_claims.OptionalClaims]:
        """
        Gets the optionalClaims property value. Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        Returns: Optional[optional_claims.OptionalClaims]
        """
        return self._optional_claims
    
    @optional_claims.setter
    def optional_claims(self,value: Optional[optional_claims.OptionalClaims] = None) -> None:
        """
        Sets the optionalClaims property value. Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        Args:
            value: Value to set for the optionalClaims property.
        """
        self._optional_claims = value
    
    @property
    def owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the owners property value. Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the owners property value. Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    @property
    def parental_control_settings(self,) -> Optional[parental_control_settings.ParentalControlSettings]:
        """
        Gets the parentalControlSettings property value. Specifies parental control settings for an application.
        Returns: Optional[parental_control_settings.ParentalControlSettings]
        """
        return self._parental_control_settings
    
    @parental_control_settings.setter
    def parental_control_settings(self,value: Optional[parental_control_settings.ParentalControlSettings] = None) -> None:
        """
        Sets the parentalControlSettings property value. Specifies parental control settings for an application.
        Args:
            value: Value to set for the parentalControlSettings property.
        """
        self._parental_control_settings = value
    
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
    def public_client(self,) -> Optional[public_client_application.PublicClientApplication]:
        """
        Gets the publicClient property value. Specifies settings for installed clients such as desktop or mobile devices.
        Returns: Optional[public_client_application.PublicClientApplication]
        """
        return self._public_client
    
    @public_client.setter
    def public_client(self,value: Optional[public_client_application.PublicClientApplication] = None) -> None:
        """
        Sets the publicClient property value. Specifies settings for installed clients such as desktop or mobile devices.
        Args:
            value: Value to set for the publicClient property.
        """
        self._public_client = value
    
    @property
    def publisher_domain(self,) -> Optional[str]:
        """
        Gets the publisherDomain property value. The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
        Returns: Optional[str]
        """
        return self._publisher_domain
    
    @publisher_domain.setter
    def publisher_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the publisherDomain property value. The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
        Args:
            value: Value to set for the publisherDomain property.
        """
        self._publisher_domain = value
    
    @property
    def required_resource_access(self,) -> Optional[List[required_resource_access.RequiredResourceAccess]]:
        """
        Gets the requiredResourceAccess property value. Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[required_resource_access.RequiredResourceAccess]]
        """
        return self._required_resource_access
    
    @required_resource_access.setter
    def required_resource_access(self,value: Optional[List[required_resource_access.RequiredResourceAccess]] = None) -> None:
        """
        Sets the requiredResourceAccess property value. Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the requiredResourceAccess property.
        """
        self._required_resource_access = value
    
    @property
    def saml_metadata_url(self,) -> Optional[str]:
        """
        Gets the samlMetadataUrl property value. The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        Returns: Optional[str]
        """
        return self._saml_metadata_url
    
    @saml_metadata_url.setter
    def saml_metadata_url(self,value: Optional[str] = None) -> None:
        """
        Sets the samlMetadataUrl property value. The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        Args:
            value: Value to set for the samlMetadataUrl property.
        """
        self._saml_metadata_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_object_value("api", self.api)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
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
        writer.write_collection_of_object_values("requiredResourceAccess", self.required_resource_access)
        writer.write_str_value("samlMetadataUrl", self.saml_metadata_url)
        writer.write_str_value("serviceManagementReference", self.service_management_reference)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("spa", self.spa)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
        writer.write_object_value("web", self.web)
    
    @property
    def service_management_reference(self,) -> Optional[str]:
        """
        Gets the serviceManagementReference property value. References application or service contact information from a Service or Asset Management database. Nullable.
        Returns: Optional[str]
        """
        return self._service_management_reference
    
    @service_management_reference.setter
    def service_management_reference(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceManagementReference property value. References application or service contact information from a Service or Asset Management database. Nullable.
        Args:
            value: Value to set for the serviceManagementReference property.
        """
        self._service_management_reference = value
    
    @property
    def sign_in_audience(self,) -> Optional[str]:
        """
        Gets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        Returns: Optional[str]
        """
        return self._sign_in_audience
    
    @sign_in_audience.setter
    def sign_in_audience(self,value: Optional[str] = None) -> None:
        """
        Sets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the signInAudience property.
        """
        self._sign_in_audience = value
    
    @property
    def spa(self,) -> Optional[spa_application.SpaApplication]:
        """
        Gets the spa property value. Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        Returns: Optional[spa_application.SpaApplication]
        """
        return self._spa
    
    @spa.setter
    def spa(self,value: Optional[spa_application.SpaApplication] = None) -> None:
        """
        Sets the spa property value. Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        Args:
            value: Value to set for the spa property.
        """
        self._spa = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Custom strings that can be used to categorize and identify the application. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Custom strings that can be used to categorize and identify the application. Not nullable. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def token_encryption_key_id(self,) -> Optional[str]:
        """
        Gets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Returns: Optional[str]
        """
        return self._token_encryption_key_id
    
    @token_encryption_key_id.setter
    def token_encryption_key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Args:
            value: Value to set for the tokenEncryptionKeyId property.
        """
        self._token_encryption_key_id = value
    
    @property
    def token_issuance_policies(self,) -> Optional[List[token_issuance_policy.TokenIssuancePolicy]]:
        """
        Gets the tokenIssuancePolicies property value. The tokenIssuancePolicies property
        Returns: Optional[List[token_issuance_policy.TokenIssuancePolicy]]
        """
        return self._token_issuance_policies
    
    @token_issuance_policies.setter
    def token_issuance_policies(self,value: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None) -> None:
        """
        Sets the tokenIssuancePolicies property value. The tokenIssuancePolicies property
        Args:
            value: Value to set for the tokenIssuancePolicies property.
        """
        self._token_issuance_policies = value
    
    @property
    def token_lifetime_policies(self,) -> Optional[List[token_lifetime_policy.TokenLifetimePolicy]]:
        """
        Gets the tokenLifetimePolicies property value. The tokenLifetimePolicies property
        Returns: Optional[List[token_lifetime_policy.TokenLifetimePolicy]]
        """
        return self._token_lifetime_policies
    
    @token_lifetime_policies.setter
    def token_lifetime_policies(self,value: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None) -> None:
        """
        Sets the tokenLifetimePolicies property value. The tokenLifetimePolicies property
        Args:
            value: Value to set for the tokenLifetimePolicies property.
        """
        self._token_lifetime_policies = value
    
    @property
    def verified_publisher(self,) -> Optional[verified_publisher.VerifiedPublisher]:
        """
        Gets the verifiedPublisher property value. Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        Returns: Optional[verified_publisher.VerifiedPublisher]
        """
        return self._verified_publisher
    
    @verified_publisher.setter
    def verified_publisher(self,value: Optional[verified_publisher.VerifiedPublisher] = None) -> None:
        """
        Sets the verifiedPublisher property value. Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        Args:
            value: Value to set for the verifiedPublisher property.
        """
        self._verified_publisher = value
    
    @property
    def web(self,) -> Optional[web_application.WebApplication]:
        """
        Gets the web property value. Specifies settings for a web application.
        Returns: Optional[web_application.WebApplication]
        """
        return self._web
    
    @web.setter
    def web(self,value: Optional[web_application.WebApplication] = None) -> None:
        """
        Sets the web property value. Specifies settings for a web application.
        Args:
            value: Value to set for the web property.
        """
        self._web = value
    

