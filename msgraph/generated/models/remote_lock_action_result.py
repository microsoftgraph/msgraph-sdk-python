from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult

from .device_action_result import DeviceActionResult

@dataclass
class RemoteLockActionResult(DeviceActionResult):
    """
    Lock action result with a pin to unlock
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Pin to unlock the client
    unlock_pin: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteLockActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteLockActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteLockActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult

        from .device_action_result import DeviceActionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "unlockPin": lambda n : setattr(self, 'unlock_pin', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("unlockPin", self.unlock_pin)
    

