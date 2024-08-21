from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fido2_restriction_enforcement_type import Fido2RestrictionEnforcementType

@dataclass
class Fido2KeyRestrictions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A collection of Authenticator Attestation GUIDs. AADGUIDs define key types and manufacturers.
    aa_guids: Optional[List[str]] = None
    # Enforcement type. Possible values are: allow, block.
    enforcement_type: Optional[Fido2RestrictionEnforcementType] = None
    # Determines if the configured key enforcement is enabled.
    is_enforced: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Fido2KeyRestrictions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Fido2KeyRestrictions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Fido2KeyRestrictions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .fido2_restriction_enforcement_type import Fido2RestrictionEnforcementType

        from .fido2_restriction_enforcement_type import Fido2RestrictionEnforcementType

        fields: Dict[str, Callable[[Any], None]] = {
            "aaGuids": lambda n : setattr(self, 'aa_guids', n.get_collection_of_primitive_values(str)),
            "enforcementType": lambda n : setattr(self, 'enforcement_type', n.get_enum_value(Fido2RestrictionEnforcementType)),
            "isEnforced": lambda n : setattr(self, 'is_enforced', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("aaGuids", self.aa_guids)
        writer.write_enum_value("enforcementType", self.enforcement_type)
        writer.write_bool_value("isEnforced", self.is_enforced)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

