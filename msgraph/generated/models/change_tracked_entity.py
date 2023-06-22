from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, offer_shift_request, open_shift, open_shift_change_request, schedule_change_request, scheduling_group, shift, shift_preferences, swap_shifts_change_request, time_off, time_off_reason, time_off_request, workforce_integration

from . import entity

@dataclass
class ChangeTrackedEntity(entity.Entity):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # Identity of the person who last modified the entity.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeTrackedEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeTrackedEntity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from . import offer_shift_request

            return offer_shift_request.OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShift".casefold():
            from . import open_shift

            return open_shift.OpenShift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from . import open_shift_change_request

            return open_shift_change_request.OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduleChangeRequest".casefold():
            from . import schedule_change_request

            return schedule_change_request.ScheduleChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedulingGroup".casefold():
            from . import scheduling_group

            return scheduling_group.SchedulingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shift".casefold():
            from . import shift

            return shift.Shift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftPreferences".casefold():
            from . import shift_preferences

            return shift_preferences.ShiftPreferences()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from . import swap_shifts_change_request

            return swap_shifts_change_request.SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOff".casefold():
            from . import time_off

            return time_off.TimeOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffReason".casefold():
            from . import time_off_reason

            return time_off_reason.TimeOffReason()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from . import time_off_request

            return time_off_request.TimeOffRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workforceIntegration".casefold():
            from . import workforce_integration

            return workforce_integration.WorkforceIntegration()
        return ChangeTrackedEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, offer_shift_request, open_shift, open_shift_change_request, schedule_change_request, scheduling_group, shift, shift_preferences, swap_shifts_change_request, time_off, time_off_reason, time_off_request, workforce_integration

        from . import entity, identity_set, offer_shift_request, open_shift, open_shift_change_request, schedule_change_request, scheduling_group, shift, shift_preferences, swap_shifts_change_request, time_off, time_off_reason, time_off_request, workforce_integration

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

