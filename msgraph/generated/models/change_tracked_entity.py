from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_note import DayNote
    from .entity import Entity
    from .identity_set import IdentitySet
    from .offer_shift_request import OfferShiftRequest
    from .open_shift import OpenShift
    from .open_shift_change_request import OpenShiftChangeRequest
    from .schedule_change_request import ScheduleChangeRequest
    from .scheduling_group import SchedulingGroup
    from .shift import Shift
    from .shift_preferences import ShiftPreferences
    from .swap_shifts_change_request import SwapShiftsChangeRequest
    from .time_card import TimeCard
    from .time_off import TimeOff
    from .time_off_reason import TimeOffReason
    from .time_off_request import TimeOffRequest
    from .workforce_integration import WorkforceIntegration

from .entity import Entity

@dataclass
class ChangeTrackedEntity(Entity, Parsable):
    # Identity of the creator of the entity.
    created_by: Optional[IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Identity of the person who last modified the entity.
    last_modified_by: Optional[IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeTrackedEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeTrackedEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dayNote".casefold():
            from .day_note import DayNote

            return DayNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from .offer_shift_request import OfferShiftRequest

            return OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShift".casefold():
            from .open_shift import OpenShift

            return OpenShift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from .open_shift_change_request import OpenShiftChangeRequest

            return OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduleChangeRequest".casefold():
            from .schedule_change_request import ScheduleChangeRequest

            return ScheduleChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedulingGroup".casefold():
            from .scheduling_group import SchedulingGroup

            return SchedulingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shift".casefold():
            from .shift import Shift

            return Shift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftPreferences".casefold():
            from .shift_preferences import ShiftPreferences

            return ShiftPreferences()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeCard".casefold():
            from .time_card import TimeCard

            return TimeCard()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOff".casefold():
            from .time_off import TimeOff

            return TimeOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffReason".casefold():
            from .time_off_reason import TimeOffReason

            return TimeOffReason()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from .time_off_request import TimeOffRequest

            return TimeOffRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workforceIntegration".casefold():
            from .workforce_integration import WorkforceIntegration

            return WorkforceIntegration()
        return ChangeTrackedEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .day_note import DayNote
        from .entity import Entity
        from .identity_set import IdentitySet
        from .offer_shift_request import OfferShiftRequest
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .shift import Shift
        from .shift_preferences import ShiftPreferences
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .workforce_integration import WorkforceIntegration

        from .day_note import DayNote
        from .entity import Entity
        from .identity_set import IdentitySet
        from .offer_shift_request import OfferShiftRequest
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .shift import Shift
        from .shift_preferences import ShiftPreferences
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .workforce_integration import WorkforceIntegration

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("createdBy", self.created_by)
    

