from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
time_off_reason_icon_type = lazy_import('msgraph.generated.models.time_off_reason_icon_type')

class TimeOffReason(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new TimeOffReason and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.timeOffReason"
        # The name of the timeOffReason. Required.
        self._display_name: Optional[str] = None
        # Supported icon types are: none, car, calendar, running, plane, firstAid, doctor, notWorking, clock, juryDuty, globe, cup, phone, weather, umbrella, piggyBank, dog, cake, trafficCone, pin, sunny. Required.
        self._icon_type: Optional[time_off_reason_icon_type.TimeOffReasonIconType] = None
        # Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.
        self._is_active: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeOffReason:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeOffReason
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeOffReason()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the timeOffReason. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the timeOffReason. Required.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "icon_type": lambda n : setattr(self, 'icon_type', n.get_enum_value(time_off_reason_icon_type.TimeOffReasonIconType)),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def icon_type(self,) -> Optional[time_off_reason_icon_type.TimeOffReasonIconType]:
        """
        Gets the iconType property value. Supported icon types are: none, car, calendar, running, plane, firstAid, doctor, notWorking, clock, juryDuty, globe, cup, phone, weather, umbrella, piggyBank, dog, cake, trafficCone, pin, sunny. Required.
        Returns: Optional[time_off_reason_icon_type.TimeOffReasonIconType]
        """
        return self._icon_type
    
    @icon_type.setter
    def icon_type(self,value: Optional[time_off_reason_icon_type.TimeOffReasonIconType] = None) -> None:
        """
        Sets the iconType property value. Supported icon types are: none, car, calendar, running, plane, firstAid, doctor, notWorking, clock, juryDuty, globe, cup, phone, weather, umbrella, piggyBank, dog, cake, trafficCone, pin, sunny. Required.
        Args:
            value: Value to set for the iconType property.
        """
        self._icon_type = value
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("iconType", self.icon_type)
        writer.write_bool_value("isActive", self.is_active)
    

