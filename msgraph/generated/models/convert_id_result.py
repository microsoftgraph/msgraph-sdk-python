from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import generic_error

@dataclass
class ConvertIdResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # An error object indicating the reason for the conversion failure. This value is not present if the conversion succeeded.
    error_details: Optional[generic_error.GenericError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier that was converted. This value is the original, un-converted identifier.
    source_id: Optional[str] = None
    # The converted identifier. This value is not present if the conversion failed.
    target_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConvertIdResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConvertIdResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConvertIdResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import generic_error

        fields: Dict[str, Callable[[Any], None]] = {
            "errorDetails": lambda n : setattr(self, 'error_details', n.get_object_value(generic_error.GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
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
        writer.write_object_value("errorDetails", self.error_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("targetId", self.target_id)
        writer.write_additional_data_value(self.additional_data)
    

