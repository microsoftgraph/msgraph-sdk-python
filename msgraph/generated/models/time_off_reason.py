from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .time_off_reason_icon_type import TimeOffReasonIconType

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class TimeOffReason(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.timeOffReason"
    # The code of the timeOffReason to represent an external identifier. This field must be unique within the team in Microsoft Teams and uses an alphanumeric format, with a maximum of 100 characters.
    code: Optional[str] = None
    # The name of the timeOffReason. Required.
    display_name: Optional[str] = None
    # Supported icon types are: none, car, calendar, running, plane, firstAid, doctor, notWorking, clock, juryDuty, globe, cup, phone, weather, umbrella, piggyBank, dog, cake, trafficCone, pin, sunny. Required.
    icon_type: Optional[TimeOffReasonIconType] = None
    # Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.
    is_active: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeOffReason:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeOffReason
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeOffReason()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .time_off_reason_icon_type import TimeOffReasonIconType

        from .change_tracked_entity import ChangeTrackedEntity
        from .time_off_reason_icon_type import TimeOffReasonIconType

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iconType": lambda n : setattr(self, 'icon_type', n.get_enum_value(TimeOffReasonIconType)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("iconType", self.icon_type)
        writer.write_bool_value("isActive", self.is_active)
    

