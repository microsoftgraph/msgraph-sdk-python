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
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.offerShiftRequest":
                from . import offer_shift_request

                return offer_shift_request.OfferShiftRequest()
            if mapping_value == "#microsoft.graph.openShift":
                from . import open_shift

                return open_shift.OpenShift()
            if mapping_value == "#microsoft.graph.openShiftChangeRequest":
                from . import open_shift_change_request

                return open_shift_change_request.OpenShiftChangeRequest()
            if mapping_value == "#microsoft.graph.scheduleChangeRequest":
                from . import schedule_change_request

                return schedule_change_request.ScheduleChangeRequest()
            if mapping_value == "#microsoft.graph.schedulingGroup":
                from . import scheduling_group

                return scheduling_group.SchedulingGroup()
            if mapping_value == "#microsoft.graph.shift":
                from . import shift

                return shift.Shift()
            if mapping_value == "#microsoft.graph.shiftPreferences":
                from . import shift_preferences

                return shift_preferences.ShiftPreferences()
            if mapping_value == "#microsoft.graph.swapShiftsChangeRequest":
                from . import swap_shifts_change_request

                return swap_shifts_change_request.SwapShiftsChangeRequest()
            if mapping_value == "#microsoft.graph.timeOff":
                from . import time_off

                return time_off.TimeOff()
            if mapping_value == "#microsoft.graph.timeOffReason":
                from . import time_off_reason

                return time_off_reason.TimeOffReason()
            if mapping_value == "#microsoft.graph.timeOffRequest":
                from . import time_off_request

                return time_off_request.TimeOffRequest()
            if mapping_value == "#microsoft.graph.workforceIntegration":
                from . import workforce_integration

                return workforce_integration.WorkforceIntegration()
        return ChangeTrackedEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

