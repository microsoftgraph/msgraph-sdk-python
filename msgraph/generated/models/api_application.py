from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .permission_scope import PermissionScope
    from .pre_authorized_application import PreAuthorizedApplication

@dataclass
class ApiApplication(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # When true, allows an application to use claims mapping without specifying a custom signing key.
    accept_mapped_claims: Optional[bool] = None
    # Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Microsoft Entra ID knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.
    known_client_applications: Optional[List[UUID]] = None
    # The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.
    oauth2_permission_scopes: Optional[List[PermissionScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Lists the client applications that are preauthorized with the specified delegated permissions to access this application's APIs. Users aren't required to consent to any preauthorized application (for the permissions specified). However, any other permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.
    pre_authorized_applications: Optional[List[PreAuthorizedApplication]] = None
    # Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount or PersonalMicrosoftAccount, the value for this property must be 2.
    requested_access_token_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApiApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApiApplication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApiApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .permission_scope import PermissionScope
        from .pre_authorized_application import PreAuthorizedApplication

        from .permission_scope import PermissionScope
        from .pre_authorized_application import PreAuthorizedApplication

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptMappedClaims": lambda n : setattr(self, 'accept_mapped_claims', n.get_bool_value()),
            "knownClientApplications": lambda n : setattr(self, 'known_client_applications', n.get_collection_of_primitive_values(UUID)),
            "oauth2PermissionScopes": lambda n : setattr(self, 'oauth2_permission_scopes', n.get_collection_of_object_values(PermissionScope)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preAuthorizedApplications": lambda n : setattr(self, 'pre_authorized_applications', n.get_collection_of_object_values(PreAuthorizedApplication)),
            "requestedAccessTokenVersion": lambda n : setattr(self, 'requested_access_token_version', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("acceptMappedClaims", self.accept_mapped_claims)
        writer.write_collection_of_primitive_values("knownClientApplications", self.known_client_applications)
        writer.write_collection_of_object_values("oauth2PermissionScopes", self.oauth2_permission_scopes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("preAuthorizedApplications", self.pre_authorized_applications)
        writer.write_int_value("requestedAccessTokenVersion", self.requested_access_token_version)
        writer.write_additional_data_value(self.additional_data)
    

