from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_action_result = lazy_import('msgraph.generated.models.device_action_result')

class RemoteLockActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new RemoteLockActionResult and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Pin to unlock the client
        self._unlock_pin: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteLockActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteLockActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteLockActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "unlock_pin": lambda n : setattr(self, 'unlock_pin', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("unlockPin", self.unlock_pin)
    
    @property
    def unlock_pin(self,) -> Optional[str]:
        """
        Gets the unlockPin property value. Pin to unlock the client
        Returns: Optional[str]
        """
        return self._unlock_pin
    
    @unlock_pin.setter
    def unlock_pin(self,value: Optional[str] = None) -> None:
        """
        Sets the unlockPin property value. Pin to unlock the client
        Args:
            value: Value to set for the unlockPin property.
        """
        self._unlock_pin = value
    

