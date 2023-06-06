from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import optional_claim

@dataclass
class OptionalClaims(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The optional claims returned in the JWT access token.
    access_token: Optional[List[optional_claim.OptionalClaim]] = None
    # The optional claims returned in the JWT ID token.
    id_token: Optional[List[optional_claim.OptionalClaim]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The optional claims returned in the SAML token.
    saml2_token: Optional[List[optional_claim.OptionalClaim]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OptionalClaims:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OptionalClaims
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OptionalClaims()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import optional_claim

        fields: Dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
            "idToken": lambda n : setattr(self, 'id_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "saml2Token": lambda n : setattr(self, 'saml2_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("accessToken", self.access_token)
        writer.write_collection_of_object_values("idToken", self.id_token)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("saml2Token", self.saml2_token)
        writer.write_additional_data_value(self.additional_data)
    

