from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .schedule_change_request import ScheduleChangeRequest

from .schedule_change_request import ScheduleChangeRequest

@dataclass
class OpenShiftChangeRequest(ScheduleChangeRequest, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.openShiftChangeRequest"
    # ID for the open shift.
    open_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenShiftChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenShiftChangeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenShiftChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .schedule_change_request import ScheduleChangeRequest

        from .schedule_change_request import ScheduleChangeRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "openShiftId": lambda n : setattr(self, 'open_shift_id', n.get_str_value()),
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
        from .schedule_change_request import ScheduleChangeRequest

        writer.write_str_value("openShiftId", self.open_shift_id)
    

