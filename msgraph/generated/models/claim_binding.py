from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .match_confidence_level import MatchConfidenceLevel

@dataclass
class ClaimBinding(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The matchConfidenceLevel property
    match_confidence_level: Optional[MatchConfidenceLevel] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Source attribute name from the source system, for example a directory attribute.
    source_attribute: Optional[str] = None
    # Verified ID claim name or path, for example vc.credentialSubject.firstName.
    verified_id_claim: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClaimBinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClaimBinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClaimBinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .match_confidence_level import MatchConfidenceLevel

        from .match_confidence_level import MatchConfidenceLevel

        fields: dict[str, Callable[[Any], None]] = {
            "matchConfidenceLevel": lambda n : setattr(self, 'match_confidence_level', n.get_enum_value(MatchConfidenceLevel)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceAttribute": lambda n : setattr(self, 'source_attribute', n.get_str_value()),
            "verifiedIdClaim": lambda n : setattr(self, 'verified_id_claim', n.get_str_value()),
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
        writer.write_enum_value("matchConfidenceLevel", self.match_confidence_level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceAttribute", self.source_attribute)
        writer.write_str_value("verifiedIdClaim", self.verified_id_claim)
        writer.write_additional_data_value(self.additional_data)
    

