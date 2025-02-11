from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_note import DayNote
    from .day_of_week import DayOfWeek
    from .entity import Entity
    from .offer_shift_request import OfferShiftRequest
    from .open_shift import OpenShift
    from .open_shift_change_request import OpenShiftChangeRequest
    from .operation_status import OperationStatus
    from .scheduling_group import SchedulingGroup
    from .shift import Shift
    from .swap_shifts_change_request import SwapShiftsChangeRequest
    from .time_card import TimeCard
    from .time_clock_settings import TimeClockSettings
    from .time_off import TimeOff
    from .time_off_reason import TimeOffReason
    from .time_off_request import TimeOffRequest

from .entity import Entity

@dataclass
class Schedule(Entity, Parsable):
    # The day notes in the schedule.
    day_notes: Optional[list[DayNote]] = None
    # Indicates whether the schedule is enabled for the team. Required.
    enabled: Optional[bool] = None
    # Indicates whether copied shifts include activities from the original shift.
    is_activities_included_when_copying_shifts_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offer requests for shifts in the schedule.
    offer_shift_requests: Optional[list[OfferShiftRequest]] = None
    # Indicates whether offer shift requests are enabled for the schedule.
    offer_shift_requests_enabled: Optional[bool] = None
    # The open shift requests in the schedule.
    open_shift_change_requests: Optional[list[OpenShiftChangeRequest]] = None
    # The set of open shifts in a scheduling group in the schedule.
    open_shifts: Optional[list[OpenShift]] = None
    # Indicates whether open shifts are enabled for the schedule.
    open_shifts_enabled: Optional[bool] = None
    # The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
    provision_status: Optional[OperationStatus] = None
    # Additional information about why schedule provisioning failed.
    provision_status_code: Optional[str] = None
    # The logical grouping of users in the schedule (usually by role).
    scheduling_groups: Optional[list[SchedulingGroup]] = None
    # The shifts in the schedule.
    shifts: Optional[list[Shift]] = None
    # Indicates the start day of the week. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday.
    start_day_of_week: Optional[DayOfWeek] = None
    # The swap requests for shifts in the schedule.
    swap_shifts_change_requests: Optional[list[SwapShiftsChangeRequest]] = None
    # Indicates whether swap shifts requests are enabled for the schedule.
    swap_shifts_requests_enabled: Optional[bool] = None
    # The time cards in the schedule.
    time_cards: Optional[list[TimeCard]] = None
    # Indicates whether time clock is enabled for the schedule.
    time_clock_enabled: Optional[bool] = None
    # The time clock location settings for this schedule.
    time_clock_settings: Optional[TimeClockSettings] = None
    # The set of reasons for a time off in the schedule.
    time_off_reasons: Optional[list[TimeOffReason]] = None
    # The time off requests in the schedule.
    time_off_requests: Optional[list[TimeOffRequest]] = None
    # Indicates whether time off requests are enabled for the schedule.
    time_off_requests_enabled: Optional[bool] = None
    # Indicates the time zone of the schedule team using tz database format. Required.
    time_zone: Optional[str] = None
    # The instances of times off in the schedule.
    times_off: Optional[list[TimeOff]] = None
    # The IDs for the workforce integrations associated with this schedule.
    workforce_integration_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Schedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Schedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Schedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .day_note import DayNote
        from .day_of_week import DayOfWeek
        from .entity import Entity
        from .offer_shift_request import OfferShiftRequest
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .operation_status import OperationStatus
        from .scheduling_group import SchedulingGroup
        from .shift import Shift
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_card import TimeCard
        from .time_clock_settings import TimeClockSettings
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest

        from .day_note import DayNote
        from .day_of_week import DayOfWeek
        from .entity import Entity
        from .offer_shift_request import OfferShiftRequest
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .operation_status import OperationStatus
        from .scheduling_group import SchedulingGroup
        from .shift import Shift
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_card import TimeCard
        from .time_clock_settings import TimeClockSettings
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest

        fields: dict[str, Callable[[Any], None]] = {
            "dayNotes": lambda n : setattr(self, 'day_notes', n.get_collection_of_object_values(DayNote)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "isActivitiesIncludedWhenCopyingShiftsEnabled": lambda n : setattr(self, 'is_activities_included_when_copying_shifts_enabled', n.get_bool_value()),
            "offerShiftRequests": lambda n : setattr(self, 'offer_shift_requests', n.get_collection_of_object_values(OfferShiftRequest)),
            "offerShiftRequestsEnabled": lambda n : setattr(self, 'offer_shift_requests_enabled', n.get_bool_value()),
            "openShiftChangeRequests": lambda n : setattr(self, 'open_shift_change_requests', n.get_collection_of_object_values(OpenShiftChangeRequest)),
            "openShifts": lambda n : setattr(self, 'open_shifts', n.get_collection_of_object_values(OpenShift)),
            "openShiftsEnabled": lambda n : setattr(self, 'open_shifts_enabled', n.get_bool_value()),
            "provisionStatus": lambda n : setattr(self, 'provision_status', n.get_enum_value(OperationStatus)),
            "provisionStatusCode": lambda n : setattr(self, 'provision_status_code', n.get_str_value()),
            "schedulingGroups": lambda n : setattr(self, 'scheduling_groups', n.get_collection_of_object_values(SchedulingGroup)),
            "shifts": lambda n : setattr(self, 'shifts', n.get_collection_of_object_values(Shift)),
            "startDayOfWeek": lambda n : setattr(self, 'start_day_of_week', n.get_enum_value(DayOfWeek)),
            "swapShiftsChangeRequests": lambda n : setattr(self, 'swap_shifts_change_requests', n.get_collection_of_object_values(SwapShiftsChangeRequest)),
            "swapShiftsRequestsEnabled": lambda n : setattr(self, 'swap_shifts_requests_enabled', n.get_bool_value()),
            "timeCards": lambda n : setattr(self, 'time_cards', n.get_collection_of_object_values(TimeCard)),
            "timeClockEnabled": lambda n : setattr(self, 'time_clock_enabled', n.get_bool_value()),
            "timeClockSettings": lambda n : setattr(self, 'time_clock_settings', n.get_object_value(TimeClockSettings)),
            "timeOffReasons": lambda n : setattr(self, 'time_off_reasons', n.get_collection_of_object_values(TimeOffReason)),
            "timeOffRequests": lambda n : setattr(self, 'time_off_requests', n.get_collection_of_object_values(TimeOffRequest)),
            "timeOffRequestsEnabled": lambda n : setattr(self, 'time_off_requests_enabled', n.get_bool_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "timesOff": lambda n : setattr(self, 'times_off', n.get_collection_of_object_values(TimeOff)),
            "workforceIntegrationIds": lambda n : setattr(self, 'workforce_integration_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("dayNotes", self.day_notes)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("isActivitiesIncludedWhenCopyingShiftsEnabled", self.is_activities_included_when_copying_shifts_enabled)
        writer.write_collection_of_object_values("offerShiftRequests", self.offer_shift_requests)
        writer.write_bool_value("offerShiftRequestsEnabled", self.offer_shift_requests_enabled)
        writer.write_collection_of_object_values("openShiftChangeRequests", self.open_shift_change_requests)
        writer.write_collection_of_object_values("openShifts", self.open_shifts)
        writer.write_bool_value("openShiftsEnabled", self.open_shifts_enabled)
        writer.write_collection_of_object_values("schedulingGroups", self.scheduling_groups)
        writer.write_collection_of_object_values("shifts", self.shifts)
        writer.write_enum_value("startDayOfWeek", self.start_day_of_week)
        writer.write_collection_of_object_values("swapShiftsChangeRequests", self.swap_shifts_change_requests)
        writer.write_bool_value("swapShiftsRequestsEnabled", self.swap_shifts_requests_enabled)
        writer.write_collection_of_object_values("timeCards", self.time_cards)
        writer.write_bool_value("timeClockEnabled", self.time_clock_enabled)
        writer.write_object_value("timeClockSettings", self.time_clock_settings)
        writer.write_collection_of_object_values("timeOffReasons", self.time_off_reasons)
        writer.write_collection_of_object_values("timeOffRequests", self.time_off_requests)
        writer.write_bool_value("timeOffRequestsEnabled", self.time_off_requests_enabled)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_collection_of_object_values("timesOff", self.times_off)
        writer.write_collection_of_primitive_values("workforceIntegrationIds", self.workforce_integration_ids)
    

