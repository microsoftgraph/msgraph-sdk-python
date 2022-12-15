from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

permission_scope = lazy_import('msgraph.generated.models.permission_scope')
pre_authorized_application = lazy_import('msgraph.generated.models.pre_authorized_application')

class ApiApplication(AdditionalDataHolder, Parsable):
    @property
    def accept_mapped_claims(self,) -> Optional[bool]:
        """
        Gets the acceptMappedClaims property value. When true, allows an application to use claims mapping without specifying a custom signing key.
        Returns: Optional[bool]
        """
        return self._accept_mapped_claims
    
    @accept_mapped_claims.setter
    def accept_mapped_claims(self,value: Optional[bool] = None) -> None:
        """
        Sets the acceptMappedClaims property value. When true, allows an application to use claims mapping without specifying a custom signing key.
        Args:
            value: Value to set for the acceptMappedClaims property.
        """
        self._accept_mapped_claims = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new apiApplication and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # When true, allows an application to use claims mapping without specifying a custom signing key.
        self._accept_mapped_claims: Optional[bool] = None
        # Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.
        self._known_client_applications: Optional[List[Guid]] = None
        # The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.
        self._oauth2_permission_scopes: Optional[List[permission_scope.PermissionScope]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.
        self._pre_authorized_applications: Optional[List[pre_authorized_application.PreAuthorizedApplication]] = None
        # Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2
        self._requested_access_token_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApiApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApiApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApiApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accept_mapped_claims": lambda n : setattr(self, 'accept_mapped_claims', n.get_bool_value()),
            "known_client_applications": lambda n : setattr(self, 'known_client_applications', n.get_collection_of_primitive_values(guid)),
            "oauth2_permission_scopes": lambda n : setattr(self, 'oauth2_permission_scopes', n.get_collection_of_object_values(permission_scope.PermissionScope)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pre_authorized_applications": lambda n : setattr(self, 'pre_authorized_applications', n.get_collection_of_object_values(pre_authorized_application.PreAuthorizedApplication)),
            "requested_access_token_version": lambda n : setattr(self, 'requested_access_token_version', n.get_int_value()),
        }
        return fields
    
    @property
    def known_client_applications(self,) -> Optional[List[Guid]]:
        """
        Gets the knownClientApplications property value. Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.
        Returns: Optional[List[Guid]]
        """
        return self._known_client_applications
    
    @known_client_applications.setter
    def known_client_applications(self,value: Optional[List[Guid]] = None) -> None:
        """
        Sets the knownClientApplications property value. Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.
        Args:
            value: Value to set for the knownClientApplications property.
        """
        self._known_client_applications = value
    
    @property
    def oauth2_permission_scopes(self,) -> Optional[List[permission_scope.PermissionScope]]:
        """
        Gets the oauth2PermissionScopes property value. The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.
        Returns: Optional[List[permission_scope.PermissionScope]]
        """
        return self._oauth2_permission_scopes
    
    @oauth2_permission_scopes.setter
    def oauth2_permission_scopes(self,value: Optional[List[permission_scope.PermissionScope]] = None) -> None:
        """
        Sets the oauth2PermissionScopes property value. The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.
        Args:
            value: Value to set for the oauth2PermissionScopes property.
        """
        self._oauth2_permission_scopes = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def pre_authorized_applications(self,) -> Optional[List[pre_authorized_application.PreAuthorizedApplication]]:
        """
        Gets the preAuthorizedApplications property value. Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.
        Returns: Optional[List[pre_authorized_application.PreAuthorizedApplication]]
        """
        return self._pre_authorized_applications
    
    @pre_authorized_applications.setter
    def pre_authorized_applications(self,value: Optional[List[pre_authorized_application.PreAuthorizedApplication]] = None) -> None:
        """
        Sets the preAuthorizedApplications property value. Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.
        Args:
            value: Value to set for the preAuthorizedApplications property.
        """
        self._pre_authorized_applications = value
    
    @property
    def requested_access_token_version(self,) -> Optional[int]:
        """
        Gets the requestedAccessTokenVersion property value. Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2
        Returns: Optional[int]
        """
        return self._requested_access_token_version
    
    @requested_access_token_version.setter
    def requested_access_token_version(self,value: Optional[int] = None) -> None:
        """
        Sets the requestedAccessTokenVersion property value. Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2
        Args:
            value: Value to set for the requestedAccessTokenVersion property.
        """
        self._requested_access_token_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("acceptMappedClaims", self.accept_mapped_claims)
        writer.write_collection_of_primitive_values("knownClientApplications", self.known_client_applications)
        writer.write_collection_of_object_values("oauth2PermissionScopes", self.oauth2_permission_scopes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("preAuthorizedApplications", self.pre_authorized_applications)
        writer.write_int_value("requestedAccessTokenVersion", self.requested_access_token_version)
        writer.write_additional_data_value(self.additional_data)
    

