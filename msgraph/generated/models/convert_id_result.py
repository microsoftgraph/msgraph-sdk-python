from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .generic_error import GenericError

@dataclass
class ConvertIdResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # An error object indicating the reason for the conversion failure. This value isn't present if the conversion succeeded.
    error_details: Optional[GenericError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier that was converted. This value is the original, un-converted identifier.
    source_id: Optional[str] = None
    # The converted identifier. This value isn't present if the conversion failed.
    target_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConvertIdResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConvertIdResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConvertIdResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .generic_error import GenericError

        from .generic_error import GenericError

        fields: Dict[str, Callable[[Any], None]] = {
            "errorDetails": lambda n : setattr(self, 'error_details', n.get_object_value(GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
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
        from .generic_error import GenericError

        writer.write_object_value("errorDetails", self.error_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("targetId", self.target_id)
        writer.write_additional_data_value(self.additional_data)
    

