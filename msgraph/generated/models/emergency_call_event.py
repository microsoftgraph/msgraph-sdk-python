from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_event import CallEvent
    from .emergency_caller_info import EmergencyCallerInfo

from .call_event import CallEvent

@dataclass
class EmergencyCallEvent(CallEvent, Parsable):
    # The information of the emergency caller.
    caller_info: Optional[EmergencyCallerInfo] = None
    # The emergency number dialed.
    emergency_number_dialed: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy name for the emergency call event.
    policy_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmergencyCallEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmergencyCallEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmergencyCallEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .call_event import CallEvent
        from .emergency_caller_info import EmergencyCallerInfo

        from .call_event import CallEvent
        from .emergency_caller_info import EmergencyCallerInfo

        fields: dict[str, Callable[[Any], None]] = {
            "callerInfo": lambda n : setattr(self, 'caller_info', n.get_object_value(EmergencyCallerInfo)),
            "emergencyNumberDialed": lambda n : setattr(self, 'emergency_number_dialed', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
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
        writer.write_object_value("callerInfo", self.caller_info)
        writer.write_str_value("emergencyNumberDialed", self.emergency_number_dialed)
        writer.write_str_value("policyName", self.policy_name)
    

