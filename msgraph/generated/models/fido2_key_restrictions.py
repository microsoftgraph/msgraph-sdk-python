from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import fido2_restriction_enforcement_type

@dataclass
class Fido2KeyRestrictions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A collection of Authenticator Attestation GUIDs. AADGUIDs define key types and manufacturers.
    aa_guids: Optional[List[str]] = None
    # Enforcement type. Possible values are: allow, block.
    enforcement_type: Optional[fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType] = None
    # Determines if the configured key enforcement is enabled.
    is_enforced: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Fido2KeyRestrictions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Fido2KeyRestrictions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Fido2KeyRestrictions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import fido2_restriction_enforcement_type

        from . import fido2_restriction_enforcement_type

        fields: Dict[str, Callable[[Any], None]] = {
            "aaGuids": lambda n : setattr(self, 'aa_guids', n.get_collection_of_primitive_values(str)),
            "enforcementType": lambda n : setattr(self, 'enforcement_type', n.get_enum_value(fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType)),
            "isEnforced": lambda n : setattr(self, 'is_enforced', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("aaGuids", self.aa_guids)
        writer.write_enum_value("enforcementType", self.enforcement_type)
        writer.write_bool_value("isEnforced", self.is_enforced)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

