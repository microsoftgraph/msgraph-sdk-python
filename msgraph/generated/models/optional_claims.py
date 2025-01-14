from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .optional_claim import OptionalClaim

@dataclass
class OptionalClaims(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The optional claims returned in the JWT access token.
    access_token: Optional[list[OptionalClaim]] = None
    # The optional claims returned in the JWT ID token.
    id_token: Optional[list[OptionalClaim]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The optional claims returned in the SAML token.
    saml2_token: Optional[list[OptionalClaim]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OptionalClaims:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OptionalClaims
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OptionalClaims()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .optional_claim import OptionalClaim

        from .optional_claim import OptionalClaim

        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_collection_of_object_values(OptionalClaim)),
            "idToken": lambda n : setattr(self, 'id_token', n.get_collection_of_object_values(OptionalClaim)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "saml2Token": lambda n : setattr(self, 'saml2_token', n.get_collection_of_object_values(OptionalClaim)),
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
        writer.write_collection_of_object_values("accessToken", self.access_token)
        writer.write_collection_of_object_values("idToken", self.id_token)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("saml2Token", self.saml2_token)
        writer.write_additional_data_value(self.additional_data)
    

