from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

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
class Event(OutlookItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.event"
    # true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
    allow_new_time_proposals: Optional[bool] = None
    # The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
    attachments: Optional[list[Attachment]] = None
    # The collection of attendees for the event.
    attendees: Optional[list[Attendee]] = None
    # The body of the message associated with the event. It can be in HTML or text format.
    body: Optional[ItemBody] = None
    # The preview of the message associated with the event. It's in text format.
    body_preview: Optional[str] = None
    # The calendar that contains the event. Navigation property. Read-only.
    calendar: Optional[Calendar] = None
    # Contains occurrenceId property values of canceled instances in a recurring series, if the event is the series master. Instances in a recurring series that are canceled are called canceled occurences.Returned only on $select in a Get operation which specifies the ID (seriesMasterId property value) of a series master event.
    cancelled_occurrences: Optional[list[str]] = None
    # The date, time, and time zone that the event ends. By default, the end time is in UTC.
    end: Optional[DateTimeTimeZone] = None
    # Contains the id property values of the event instances that are exceptions in a recurring series.Exceptions can differ from other occurrences in a recurring series, such as the subject, start or end times, or attendees. Exceptions don't include canceled occurrences.Returned only on $select and $expand in a GET operation that specifies the ID (seriesMasterId property value) of a series master event.
    exception_occurrences: Optional[list[Event]] = None
    # The collection of open extensions defined for the event. Nullable.
    extensions: Optional[list[Extension]] = None
    # Set to true if the event has attachments.
    has_attachments: Optional[bool] = None
    # When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
    hide_attendees: Optional[bool] = None
    # A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
    i_cal_u_id: Optional[str] = None
    # The importance of the event. The possible values are: low, normal, high.
    importance: Optional[Importance] = None
    # The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences canceled from the series. Navigation property. Read-only. Nullable.
    instances: Optional[list[Event]] = None
    # Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
    is_all_day: Optional[bool] = None
    # Set to true if the event has been canceled.
    is_cancelled: Optional[bool] = None
    # Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
    is_draft: Optional[bool] = None
    # True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
    is_online_meeting: Optional[bool] = None
    # Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
    is_organizer: Optional[bool] = None
    # Set to true if an alert is set to remind the user of the event.
    is_reminder_on: Optional[bool] = None
    # The location of the event.
    location: Optional[Location] = None
    # The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
    locations: Optional[list[Location]] = None
    # The collection of multi-value extended properties defined for the event. Read-only. Nullable.
    multi_value_extended_properties: Optional[list[MultiValueLegacyExtendedProperty]] = None
    # Details for an attendee to join the meeting online. The default is null. Read-only. After you set the isOnlineMeeting and onlineMeetingProvider properties to enable a meeting online, Microsoft Graph initializes onlineMeeting. When set, the meeting remains available online, and you can't change the isOnlineMeeting, onlineMeetingProvider, and onlneMeeting properties again.
    online_meeting: Optional[OnlineMeetingInfo] = None
    # Represents the online meeting service provider. By default, onlineMeetingProvider is unknown. The possible values are unknown, teamsForBusiness, skypeForBusiness, and skypeForConsumer. Optional.  After you set onlineMeetingProvider, Microsoft Graph initializes onlineMeeting. Subsequently, you can't change onlineMeetingProvider again, and the meeting remains available online.
    online_meeting_provider: Optional[OnlineMeetingProviderType] = None
    # A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
    online_meeting_url: Optional[str] = None
    # The organizer of the event.
    organizer: Optional[Recipient] = None
    # The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
    original_end_time_zone: Optional[str] = None
    # Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    original_start: Optional[datetime.datetime] = None
    # The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
    original_start_time_zone: Optional[str] = None
    # The recurrence pattern for the event.
    recurrence: Optional[PatternedRecurrence] = None
    # The number of minutes before the event start time that the reminder alert occurs.
    reminder_minutes_before_start: Optional[int] = None
    # Default is true, which represents the organizer would like an invitee to send a response to the event.
    response_requested: Optional[bool] = None
    # Indicates the type of response sent in response to an event message.
    response_status: Optional[ResponseStatus] = None
    # The possible values are: normal, personal, private, and confidential.
    sensitivity: Optional[Sensitivity] = None
    # The ID for the recurring series master item, if this event is part of a recurring series.
    series_master_id: Optional[str] = None
    # The status to show. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
    show_as: Optional[FreeBusyStatus] = None
    # The collection of single-value extended properties defined for the event. Read-only. Nullable.
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    # The start date, time, and time zone of the event. By default, the start time is in UTC.
    start: Optional[DateTimeTimeZone] = None
    # The text of the event's subject line.
    subject: Optional[str] = None
    # A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
    transaction_id: Optional[str] = None
    # The event type. The possible values are: singleInstance, occurrence, exception, seriesMaster. Read-only
    type: Optional[EventType] = None
    # The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
    web_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Event:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Event
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Event()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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

        fields: dict[str, Callable[[Any], None]] = {
            "allowNewTimeProposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(Attendee)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "bodyPreview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(Calendar)),
            "cancelledOccurrences": lambda n : setattr(self, 'cancelled_occurrences', n.get_collection_of_primitive_values(str)),
            "end": lambda n : setattr(self, 'end', n.get_object_value(DateTimeTimeZone)),
            "exceptionOccurrences": lambda n : setattr(self, 'exception_occurrences', n.get_collection_of_object_values(Event)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allowNewTimeProposals", self.allow_new_time_proposals)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_object_value("body", self.body)
        writer.write_str_value("bodyPreview", self.body_preview)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_primitive_values("cancelledOccurrences", self.cancelled_occurrences)
        writer.write_object_value("end", self.end)
        writer.write_collection_of_object_values("exceptionOccurrences", self.exception_occurrences)
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
    

