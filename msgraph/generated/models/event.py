from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .attendee import Attendee
    from .calendar import Calendar
    from .date_time_time_zone import DateTimeTimeZone
    from .event_type import EventType
    from .extension import Extension
    from .free_busy_status import FreeBusyStatus
    from .importance import Importance
    from .item_body import ItemBody
    from .location import Location
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .online_meeting_info import OnlineMeetingInfo
    from .online_meeting_provider_type import OnlineMeetingProviderType
    from .outlook_item import OutlookItem
    from .patterned_recurrence import PatternedRecurrence
    from .recipient import Recipient
    from .response_status import ResponseStatus
    from .sensitivity import Sensitivity
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class Event(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.event"
    # true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. Default is true.
    allow_new_time_proposals: Optional[bool] = None
    # The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
    attachments: Optional[List[Attachment]] = None
    # The collection of attendees for the event.
    attendees: Optional[List[Attendee]] = None
    # The body of the message associated with the event. It can be in HTML or text format.
    body: Optional[ItemBody] = None
    # The preview of the message associated with the event. It is in text format.
    body_preview: Optional[str] = None
    # The calendar that contains the event. Navigation property. Read-only.
    calendar: Optional[Calendar] = None
    # The date, time, and time zone that the event ends. By default, the end time is in UTC.
    end: Optional[DateTimeTimeZone] = None
    # The collection of open extensions defined for the event. Nullable.
    extensions: Optional[List[Extension]] = None
    # Set to true if the event has attachments.
    has_attachments: Optional[bool] = None
    # When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. Default is false.
    hide_attendees: Optional[bool] = None
    # A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
    i_cal_u_id: Optional[str] = None
    # The importance property
    importance: Optional[Importance] = None
    # The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
    instances: Optional[List[Event]] = None
    # The isAllDay property
    is_all_day: Optional[bool] = None
    # The isCancelled property
    is_cancelled: Optional[bool] = None
    # The isDraft property
    is_draft: Optional[bool] = None
    # The isOnlineMeeting property
    is_online_meeting: Optional[bool] = None
    # The isOrganizer property
    is_organizer: Optional[bool] = None
    # The isReminderOn property
    is_reminder_on: Optional[bool] = None
    # The location property
    location: Optional[Location] = None
    # The locations property
    locations: Optional[List[Location]] = None
    # The collection of multi-value extended properties defined for the event. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The onlineMeeting property
    online_meeting: Optional[OnlineMeetingInfo] = None
    # The onlineMeetingProvider property
    online_meeting_provider: Optional[OnlineMeetingProviderType] = None
    # The onlineMeetingUrl property
    online_meeting_url: Optional[str] = None
    # The organizer property
    organizer: Optional[Recipient] = None
    # The originalEndTimeZone property
    original_end_time_zone: Optional[str] = None
    # The originalStart property
    original_start: Optional[datetime.datetime] = None
    # The originalStartTimeZone property
    original_start_time_zone: Optional[str] = None
    # The recurrence property
    recurrence: Optional[PatternedRecurrence] = None
    # The reminderMinutesBeforeStart property
    reminder_minutes_before_start: Optional[int] = None
    # The responseRequested property
    response_requested: Optional[bool] = None
    # The responseStatus property
    response_status: Optional[ResponseStatus] = None
    # The sensitivity property
    sensitivity: Optional[Sensitivity] = None
    # The seriesMasterId property
    series_master_id: Optional[str] = None
    # The showAs property
    show_as: Optional[FreeBusyStatus] = None
    # The collection of single-value extended properties defined for the event. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    # The start property
    start: Optional[DateTimeTimeZone] = None
    # The subject property
    subject: Optional[str] = None
    # The transactionId property
    transaction_id: Optional[str] = None
    # The type property
    type: Optional[EventType] = None
    # The webLink property
    web_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Event:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Event
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Event()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .attendee import Attendee
        from .calendar import Calendar
        from .date_time_time_zone import DateTimeTimeZone
        from .event_type import EventType
        from .extension import Extension
        from .free_busy_status import FreeBusyStatus
        from .importance import Importance
        from .item_body import ItemBody
        from .location import Location
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .online_meeting_info import OnlineMeetingInfo
        from .online_meeting_provider_type import OnlineMeetingProviderType
        from .outlook_item import OutlookItem
        from .patterned_recurrence import PatternedRecurrence
        from .recipient import Recipient
        from .response_status import ResponseStatus
        from .sensitivity import Sensitivity
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .attachment import Attachment
        from .attendee import Attendee
        from .calendar import Calendar
        from .date_time_time_zone import DateTimeTimeZone
        from .event_type import EventType
        from .extension import Extension
        from .free_busy_status import FreeBusyStatus
        from .importance import Importance
        from .item_body import ItemBody
        from .location import Location
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .online_meeting_info import OnlineMeetingInfo
        from .online_meeting_provider_type import OnlineMeetingProviderType
        from .outlook_item import OutlookItem
        from .patterned_recurrence import PatternedRecurrence
        from .recipient import Recipient
        from .response_status import ResponseStatus
        from .sensitivity import Sensitivity
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "allowNewTimeProposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(Attendee)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "bodyPreview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(Calendar)),
            "end": lambda n : setattr(self, 'end', n.get_object_value(DateTimeTimeZone)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "hideAttendees": lambda n : setattr(self, 'hide_attendees', n.get_bool_value()),
            "iCalUId": lambda n : setattr(self, 'i_cal_u_id', n.get_str_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(Importance)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(Event)),
            "isAllDay": lambda n : setattr(self, 'is_all_day', n.get_bool_value()),
            "isCancelled": lambda n : setattr(self, 'is_cancelled', n.get_bool_value()),
            "isDraft": lambda n : setattr(self, 'is_draft', n.get_bool_value()),
            "isOnlineMeeting": lambda n : setattr(self, 'is_online_meeting', n.get_bool_value()),
            "isOrganizer": lambda n : setattr(self, 'is_organizer', n.get_bool_value()),
            "isReminderOn": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(Location)),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(Location)),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "onlineMeeting": lambda n : setattr(self, 'online_meeting', n.get_object_value(OnlineMeetingInfo)),
            "onlineMeetingProvider": lambda n : setattr(self, 'online_meeting_provider', n.get_enum_value(OnlineMeetingProviderType)),
            "onlineMeetingUrl": lambda n : setattr(self, 'online_meeting_url', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(Recipient)),
            "originalEndTimeZone": lambda n : setattr(self, 'original_end_time_zone', n.get_str_value()),
            "originalStart": lambda n : setattr(self, 'original_start', n.get_datetime_value()),
            "originalStartTimeZone": lambda n : setattr(self, 'original_start_time_zone', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "reminderMinutesBeforeStart": lambda n : setattr(self, 'reminder_minutes_before_start', n.get_int_value()),
            "responseRequested": lambda n : setattr(self, 'response_requested', n.get_bool_value()),
            "responseStatus": lambda n : setattr(self, 'response_status', n.get_object_value(ResponseStatus)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(Sensitivity)),
            "seriesMasterId": lambda n : setattr(self, 'series_master_id', n.get_str_value()),
            "showAs": lambda n : setattr(self, 'show_as', n.get_enum_value(FreeBusyStatus)),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "start": lambda n : setattr(self, 'start', n.get_object_value(DateTimeTimeZone)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "transactionId": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(EventType)),
            "webLink": lambda n : setattr(self, 'web_link', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allowNewTimeProposals", self.allow_new_time_proposals)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_object_value("body", self.body)
        writer.write_str_value("bodyPreview", self.body_preview)
        writer.write_object_value("calendar", self.calendar)
        writer.write_object_value("end", self.end)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("hideAttendees", self.hide_attendees)
        writer.write_str_value("iCalUId", self.i_cal_u_id)
        writer.write_enum_value("importance", self.importance)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_bool_value("isAllDay", self.is_all_day)
        writer.write_bool_value("isCancelled", self.is_cancelled)
        writer.write_bool_value("isDraft", self.is_draft)
        writer.write_bool_value("isOnlineMeeting", self.is_online_meeting)
        writer.write_bool_value("isOrganizer", self.is_organizer)
        writer.write_bool_value("isReminderOn", self.is_reminder_on)
        writer.write_object_value("location", self.location)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_object_value("onlineMeeting", self.online_meeting)
        writer.write_enum_value("onlineMeetingProvider", self.online_meeting_provider)
        writer.write_str_value("onlineMeetingUrl", self.online_meeting_url)
        writer.write_object_value("organizer", self.organizer)
        writer.write_str_value("originalEndTimeZone", self.original_end_time_zone)
        writer.write_datetime_value("originalStart", self.original_start)
        writer.write_str_value("originalStartTimeZone", self.original_start_time_zone)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_int_value("reminderMinutesBeforeStart", self.reminder_minutes_before_start)
        writer.write_bool_value("responseRequested", self.response_requested)
        writer.write_object_value("responseStatus", self.response_status)
        writer.write_enum_value("sensitivity", self.sensitivity)
        writer.write_str_value("seriesMasterId", self.series_master_id)
        writer.write_enum_value("showAs", self.show_as)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_object_value("start", self.start)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("transactionId", self.transaction_id)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("webLink", self.web_link)
    

