from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import schedule_change_request

from . import schedule_change_request

class OpenShiftChangeRequest(schedule_change_request.ScheduleChangeRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new OpenShiftChangeRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.openShiftChangeRequest"
        # ID for the open shift.
        self._open_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenShiftChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenShiftChangeRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OpenShiftChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import schedule_change_request

        fields: Dict[str, Callable[[Any], None]] = {
            "openShiftId": lambda n : setattr(self, 'open_shift_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def open_shift_id(self,) -> Optional[str]:
        """
        Gets the openShiftId property value. ID for the open shift.
        Returns: Optional[str]
        """
        return self._open_shift_id
    
    @open_shift_id.setter
    def open_shift_id(self,value: Optional[str] = None) -> None:
        """
        Sets the openShiftId property value. ID for the open shift.
        Args:
            value: Value to set for the open_shift_id property.
        """
        self._open_shift_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("openShiftId", self.open_shift_id)
    

