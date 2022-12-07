from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
offer_shift_request = lazy_import('msgraph.generated.models.offer_shift_request')
open_shift = lazy_import('msgraph.generated.models.open_shift')
open_shift_change_request = lazy_import('msgraph.generated.models.open_shift_change_request')
operation_status = lazy_import('msgraph.generated.models.operation_status')
scheduling_group = lazy_import('msgraph.generated.models.scheduling_group')
shift = lazy_import('msgraph.generated.models.shift')
swap_shifts_change_request = lazy_import('msgraph.generated.models.swap_shifts_change_request')
time_off = lazy_import('msgraph.generated.models.time_off')
time_off_reason = lazy_import('msgraph.generated.models.time_off_reason')
time_off_request = lazy_import('msgraph.generated.models.time_off_request')

class Schedule(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new schedule and sets the default values.
        """
        super().__init__()
        # Indicates whether the schedule is enabled for the team. Required.
        self._enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The offerShiftRequests property
        self._offer_shift_requests: Optional[List[offer_shift_request.OfferShiftRequest]] = None
        # Indicates whether offer shift requests are enabled for the schedule.
        self._offer_shift_requests_enabled: Optional[bool] = None
        # The openShiftChangeRequests property
        self._open_shift_change_requests: Optional[List[open_shift_change_request.OpenShiftChangeRequest]] = None
        # The openShifts property
        self._open_shifts: Optional[List[open_shift.OpenShift]] = None
        # Indicates whether open shifts are enabled for the schedule.
        self._open_shifts_enabled: Optional[bool] = None
        # The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        self._provision_status: Optional[operation_status.OperationStatus] = None
        # Additional information about why schedule provisioning failed.
        self._provision_status_code: Optional[str] = None
        # The logical grouping of users in the schedule (usually by role).
        self._scheduling_groups: Optional[List[scheduling_group.SchedulingGroup]] = None
        # The shifts in the schedule.
        self._shifts: Optional[List[shift.Shift]] = None
        # The swapShiftsChangeRequests property
        self._swap_shifts_change_requests: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]] = None
        # Indicates whether swap shifts requests are enabled for the schedule.
        self._swap_shifts_requests_enabled: Optional[bool] = None
        # Indicates whether time clock is enabled for the schedule.
        self._time_clock_enabled: Optional[bool] = None
        # The set of reasons for a time off in the schedule.
        self._time_off_reasons: Optional[List[time_off_reason.TimeOffReason]] = None
        # The timeOffRequests property
        self._time_off_requests: Optional[List[time_off_request.TimeOffRequest]] = None
        # Indicates whether time off requests are enabled for the schedule.
        self._time_off_requests_enabled: Optional[bool] = None
        # The instances of times off in the schedule.
        self._times_off: Optional[List[time_off.TimeOff]] = None
        # Indicates the time zone of the schedule team using tz database format. Required.
        self._time_zone: Optional[str] = None
        # The workforceIntegrationIds property
        self._workforce_integration_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Schedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Schedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Schedule()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Indicates whether the schedule is enabled for the team. Required.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Indicates whether the schedule is enabled for the team. Required.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "offer_shift_requests": lambda n : setattr(self, 'offer_shift_requests', n.get_collection_of_object_values(offer_shift_request.OfferShiftRequest)),
            "offer_shift_requests_enabled": lambda n : setattr(self, 'offer_shift_requests_enabled', n.get_bool_value()),
            "open_shift_change_requests": lambda n : setattr(self, 'open_shift_change_requests', n.get_collection_of_object_values(open_shift_change_request.OpenShiftChangeRequest)),
            "open_shifts": lambda n : setattr(self, 'open_shifts', n.get_collection_of_object_values(open_shift.OpenShift)),
            "open_shifts_enabled": lambda n : setattr(self, 'open_shifts_enabled', n.get_bool_value()),
            "provision_status": lambda n : setattr(self, 'provision_status', n.get_enum_value(operation_status.OperationStatus)),
            "provision_status_code": lambda n : setattr(self, 'provision_status_code', n.get_str_value()),
            "scheduling_groups": lambda n : setattr(self, 'scheduling_groups', n.get_collection_of_object_values(scheduling_group.SchedulingGroup)),
            "shifts": lambda n : setattr(self, 'shifts', n.get_collection_of_object_values(shift.Shift)),
            "swap_shifts_change_requests": lambda n : setattr(self, 'swap_shifts_change_requests', n.get_collection_of_object_values(swap_shifts_change_request.SwapShiftsChangeRequest)),
            "swap_shifts_requests_enabled": lambda n : setattr(self, 'swap_shifts_requests_enabled', n.get_bool_value()),
            "time_clock_enabled": lambda n : setattr(self, 'time_clock_enabled', n.get_bool_value()),
            "time_off_reasons": lambda n : setattr(self, 'time_off_reasons', n.get_collection_of_object_values(time_off_reason.TimeOffReason)),
            "time_off_requests": lambda n : setattr(self, 'time_off_requests', n.get_collection_of_object_values(time_off_request.TimeOffRequest)),
            "time_off_requests_enabled": lambda n : setattr(self, 'time_off_requests_enabled', n.get_bool_value()),
            "times_off": lambda n : setattr(self, 'times_off', n.get_collection_of_object_values(time_off.TimeOff)),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "workforce_integration_ids": lambda n : setattr(self, 'workforce_integration_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def offer_shift_requests(self,) -> Optional[List[offer_shift_request.OfferShiftRequest]]:
        """
        Gets the offerShiftRequests property value. The offerShiftRequests property
        Returns: Optional[List[offer_shift_request.OfferShiftRequest]]
        """
        return self._offer_shift_requests
    
    @offer_shift_requests.setter
    def offer_shift_requests(self,value: Optional[List[offer_shift_request.OfferShiftRequest]] = None) -> None:
        """
        Sets the offerShiftRequests property value. The offerShiftRequests property
        Args:
            value: Value to set for the offerShiftRequests property.
        """
        self._offer_shift_requests = value
    
    @property
    def offer_shift_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the offerShiftRequestsEnabled property value. Indicates whether offer shift requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._offer_shift_requests_enabled
    
    @offer_shift_requests_enabled.setter
    def offer_shift_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the offerShiftRequestsEnabled property value. Indicates whether offer shift requests are enabled for the schedule.
        Args:
            value: Value to set for the offerShiftRequestsEnabled property.
        """
        self._offer_shift_requests_enabled = value
    
    @property
    def open_shift_change_requests(self,) -> Optional[List[open_shift_change_request.OpenShiftChangeRequest]]:
        """
        Gets the openShiftChangeRequests property value. The openShiftChangeRequests property
        Returns: Optional[List[open_shift_change_request.OpenShiftChangeRequest]]
        """
        return self._open_shift_change_requests
    
    @open_shift_change_requests.setter
    def open_shift_change_requests(self,value: Optional[List[open_shift_change_request.OpenShiftChangeRequest]] = None) -> None:
        """
        Sets the openShiftChangeRequests property value. The openShiftChangeRequests property
        Args:
            value: Value to set for the openShiftChangeRequests property.
        """
        self._open_shift_change_requests = value
    
    @property
    def open_shifts(self,) -> Optional[List[open_shift.OpenShift]]:
        """
        Gets the openShifts property value. The openShifts property
        Returns: Optional[List[open_shift.OpenShift]]
        """
        return self._open_shifts
    
    @open_shifts.setter
    def open_shifts(self,value: Optional[List[open_shift.OpenShift]] = None) -> None:
        """
        Sets the openShifts property value. The openShifts property
        Args:
            value: Value to set for the openShifts property.
        """
        self._open_shifts = value
    
    @property
    def open_shifts_enabled(self,) -> Optional[bool]:
        """
        Gets the openShiftsEnabled property value. Indicates whether open shifts are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._open_shifts_enabled
    
    @open_shifts_enabled.setter
    def open_shifts_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the openShiftsEnabled property value. Indicates whether open shifts are enabled for the schedule.
        Args:
            value: Value to set for the openShiftsEnabled property.
        """
        self._open_shifts_enabled = value
    
    @property
    def provision_status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the provisionStatus property value. The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._provision_status
    
    @provision_status.setter
    def provision_status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the provisionStatus property value. The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        Args:
            value: Value to set for the provisionStatus property.
        """
        self._provision_status = value
    
    @property
    def provision_status_code(self,) -> Optional[str]:
        """
        Gets the provisionStatusCode property value. Additional information about why schedule provisioning failed.
        Returns: Optional[str]
        """
        return self._provision_status_code
    
    @provision_status_code.setter
    def provision_status_code(self,value: Optional[str] = None) -> None:
        """
        Sets the provisionStatusCode property value. Additional information about why schedule provisioning failed.
        Args:
            value: Value to set for the provisionStatusCode property.
        """
        self._provision_status_code = value
    
    @property
    def scheduling_groups(self,) -> Optional[List[scheduling_group.SchedulingGroup]]:
        """
        Gets the schedulingGroups property value. The logical grouping of users in the schedule (usually by role).
        Returns: Optional[List[scheduling_group.SchedulingGroup]]
        """
        return self._scheduling_groups
    
    @scheduling_groups.setter
    def scheduling_groups(self,value: Optional[List[scheduling_group.SchedulingGroup]] = None) -> None:
        """
        Sets the schedulingGroups property value. The logical grouping of users in the schedule (usually by role).
        Args:
            value: Value to set for the schedulingGroups property.
        """
        self._scheduling_groups = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_object_values("offerShiftRequests", self.offer_shift_requests)
        writer.write_bool_value("offerShiftRequestsEnabled", self.offer_shift_requests_enabled)
        writer.write_collection_of_object_values("openShiftChangeRequests", self.open_shift_change_requests)
        writer.write_collection_of_object_values("openShifts", self.open_shifts)
        writer.write_bool_value("openShiftsEnabled", self.open_shifts_enabled)
        writer.write_collection_of_object_values("schedulingGroups", self.scheduling_groups)
        writer.write_collection_of_object_values("shifts", self.shifts)
        writer.write_collection_of_object_values("swapShiftsChangeRequests", self.swap_shifts_change_requests)
        writer.write_bool_value("swapShiftsRequestsEnabled", self.swap_shifts_requests_enabled)
        writer.write_bool_value("timeClockEnabled", self.time_clock_enabled)
        writer.write_collection_of_object_values("timeOffReasons", self.time_off_reasons)
        writer.write_collection_of_object_values("timeOffRequests", self.time_off_requests)
        writer.write_bool_value("timeOffRequestsEnabled", self.time_off_requests_enabled)
        writer.write_collection_of_object_values("timesOff", self.times_off)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_collection_of_primitive_values("workforceIntegrationIds", self.workforce_integration_ids)
    
    @property
    def shifts(self,) -> Optional[List[shift.Shift]]:
        """
        Gets the shifts property value. The shifts in the schedule.
        Returns: Optional[List[shift.Shift]]
        """
        return self._shifts
    
    @shifts.setter
    def shifts(self,value: Optional[List[shift.Shift]] = None) -> None:
        """
        Sets the shifts property value. The shifts in the schedule.
        Args:
            value: Value to set for the shifts property.
        """
        self._shifts = value
    
    @property
    def swap_shifts_change_requests(self,) -> Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]]:
        """
        Gets the swapShiftsChangeRequests property value. The swapShiftsChangeRequests property
        Returns: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]]
        """
        return self._swap_shifts_change_requests
    
    @swap_shifts_change_requests.setter
    def swap_shifts_change_requests(self,value: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]] = None) -> None:
        """
        Sets the swapShiftsChangeRequests property value. The swapShiftsChangeRequests property
        Args:
            value: Value to set for the swapShiftsChangeRequests property.
        """
        self._swap_shifts_change_requests = value
    
    @property
    def swap_shifts_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the swapShiftsRequestsEnabled property value. Indicates whether swap shifts requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._swap_shifts_requests_enabled
    
    @swap_shifts_requests_enabled.setter
    def swap_shifts_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the swapShiftsRequestsEnabled property value. Indicates whether swap shifts requests are enabled for the schedule.
        Args:
            value: Value to set for the swapShiftsRequestsEnabled property.
        """
        self._swap_shifts_requests_enabled = value
    
    @property
    def time_clock_enabled(self,) -> Optional[bool]:
        """
        Gets the timeClockEnabled property value. Indicates whether time clock is enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._time_clock_enabled
    
    @time_clock_enabled.setter
    def time_clock_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the timeClockEnabled property value. Indicates whether time clock is enabled for the schedule.
        Args:
            value: Value to set for the timeClockEnabled property.
        """
        self._time_clock_enabled = value
    
    @property
    def time_off_reasons(self,) -> Optional[List[time_off_reason.TimeOffReason]]:
        """
        Gets the timeOffReasons property value. The set of reasons for a time off in the schedule.
        Returns: Optional[List[time_off_reason.TimeOffReason]]
        """
        return self._time_off_reasons
    
    @time_off_reasons.setter
    def time_off_reasons(self,value: Optional[List[time_off_reason.TimeOffReason]] = None) -> None:
        """
        Sets the timeOffReasons property value. The set of reasons for a time off in the schedule.
        Args:
            value: Value to set for the timeOffReasons property.
        """
        self._time_off_reasons = value
    
    @property
    def time_off_requests(self,) -> Optional[List[time_off_request.TimeOffRequest]]:
        """
        Gets the timeOffRequests property value. The timeOffRequests property
        Returns: Optional[List[time_off_request.TimeOffRequest]]
        """
        return self._time_off_requests
    
    @time_off_requests.setter
    def time_off_requests(self,value: Optional[List[time_off_request.TimeOffRequest]] = None) -> None:
        """
        Sets the timeOffRequests property value. The timeOffRequests property
        Args:
            value: Value to set for the timeOffRequests property.
        """
        self._time_off_requests = value
    
    @property
    def time_off_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the timeOffRequestsEnabled property value. Indicates whether time off requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._time_off_requests_enabled
    
    @time_off_requests_enabled.setter
    def time_off_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the timeOffRequestsEnabled property value. Indicates whether time off requests are enabled for the schedule.
        Args:
            value: Value to set for the timeOffRequestsEnabled property.
        """
        self._time_off_requests_enabled = value
    
    @property
    def times_off(self,) -> Optional[List[time_off.TimeOff]]:
        """
        Gets the timesOff property value. The instances of times off in the schedule.
        Returns: Optional[List[time_off.TimeOff]]
        """
        return self._times_off
    
    @times_off.setter
    def times_off(self,value: Optional[List[time_off.TimeOff]] = None) -> None:
        """
        Sets the timesOff property value. The instances of times off in the schedule.
        Args:
            value: Value to set for the timesOff property.
        """
        self._times_off = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. Indicates the time zone of the schedule team using tz database format. Required.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. Indicates the time zone of the schedule team using tz database format. Required.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    
    @property
    def workforce_integration_ids(self,) -> Optional[List[str]]:
        """
        Gets the workforceIntegrationIds property value. The workforceIntegrationIds property
        Returns: Optional[List[str]]
        """
        return self._workforce_integration_ids
    
    @workforce_integration_ids.setter
    def workforce_integration_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the workforceIntegrationIds property value. The workforceIntegrationIds property
        Args:
            value: Value to set for the workforceIntegrationIds property.
        """
        self._workforce_integration_ids = value
    

