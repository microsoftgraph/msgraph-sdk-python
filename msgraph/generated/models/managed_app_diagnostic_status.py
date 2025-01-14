from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ManagedAppDiagnosticStatus(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents diagnostics status.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Instruction on how to mitigate a failed validation
    mitigation_instruction: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the operation
    state: Optional[str] = None
    # The validation friendly name
    validation_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppDiagnosticStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppDiagnosticStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppDiagnosticStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "mitigationInstruction": lambda n : setattr(self, 'mitigation_instruction', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "validationName": lambda n : setattr(self, 'validation_name', n.get_str_value()),
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
        writer.write_str_value("mitigationInstruction", self.mitigation_instruction)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("validationName", self.validation_name)
        writer.write_additional_data_value(self.additional_data)
    

