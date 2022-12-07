from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

schedule_entity = lazy_import('msgraph.generated.models.schedule_entity')

class TimeOffItem(schedule_entity.ScheduleEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new TimeOffItem and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # ID of the timeOffReason for this timeOffItem. Required.
        self._time_off_reason_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeOffItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeOffItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeOffItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "time_off_reason_id": lambda n : setattr(self, 'time_off_reason_id', n.get_str_value()),
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
        writer.write_str_value("timeOffReasonId", self.time_off_reason_id)
    
    @property
    def time_off_reason_id(self,) -> Optional[str]:
        """
        Gets the timeOffReasonId property value. ID of the timeOffReason for this timeOffItem. Required.
        Returns: Optional[str]
        """
        return self._time_off_reason_id
    
    @time_off_reason_id.setter
    def time_off_reason_id(self,value: Optional[str] = None) -> None:
        """
        Sets the timeOffReasonId property value. ID of the timeOffReason for this timeOffItem. Required.
        Args:
            value: Value to set for the timeOffReasonId property.
        """
        self._time_off_reason_id = value
    

