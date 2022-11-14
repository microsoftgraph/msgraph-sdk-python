from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import device_action_result

class ResetPasscodeActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new ResetPasscodeActionResult and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.resetPasscodeActionResult"
        # Newly generated passcode for the device
        self._passcode: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResetPasscodeActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResetPasscodeActionResult
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return ResetPasscodeActionResult()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def passcode(self,) -> Optional[str]:
        """
        Gets the passcode property value. Newly generated passcode for the device
        Returns: Optional[str]
        """
        return self._passcode

    @passcode.setter
    def passcode(self,value: Optional[str] = None) -> None:
        """
        Sets the passcode property value. Newly generated passcode for the device
        Args:
            value: Value to set for the passcode property.
        """
        self._passcode = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("passcode", self.passcode)


