from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ManagedAppDiagnosticStatus(AdditionalDataHolder, Parsable):
    """
    Represents diagnostics status.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Instruction on how to mitigate a failed validation
    mitigation_instruction: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the operation
    state: Optional[str] = None
    # The validation friendly name
    validation_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppDiagnosticStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppDiagnosticStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppDiagnosticStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "mitigationInstruction": lambda n : setattr(self, 'mitigation_instruction', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "validationName": lambda n : setattr(self, 'validation_name', n.get_str_value()),
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
        writer.write_str_value("mitigationInstruction", self.mitigation_instruction)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("validationName", self.validation_name)
        writer.write_additional_data_value(self.additional_data)
    

