from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
attendee = lazy_import('msgraph.generated.models.attendee')
calendar = lazy_import('msgraph.generated.models.calendar')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
event_type = lazy_import('msgraph.generated.models.event_type')
extension = lazy_import('msgraph.generated.models.extension')
free_busy_status = lazy_import('msgraph.generated.models.free_busy_status')
importance = lazy_import('msgraph.generated.models.importance')
item_body = lazy_import('msgraph.generated.models.item_body')
location = lazy_import('msgraph.generated.models.location')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
online_meeting_info = lazy_import('msgraph.generated.models.online_meeting_info')
online_meeting_provider_type = lazy_import('msgraph.generated.models.online_meeting_provider_type')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
patterned_recurrence = lazy_import('msgraph.generated.models.patterned_recurrence')
recipient = lazy_import('msgraph.generated.models.recipient')
response_status = lazy_import('msgraph.generated.models.response_status')
sensitivity = lazy_import('msgraph.generated.models.sensitivity')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class Event(outlook_item.OutlookItem):
    @property
    def allow_new_time_proposals(self,) -> Optional[bool]:
        """
        Gets the allowNewTimeProposals property value. true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. Default is true.
        Returns: Optional[bool]
        """
        return self._allow_new_time_proposals
    
    @allow_new_time_proposals.setter
    def allow_new_time_proposals(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNewTimeProposals property value. true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. Default is true.
        Args:
            value: Value to set for the allowNewTimeProposals property.
        """
        self._allow_new_time_proposals = value
    
    @property
    def attachments(self,) -> Optional[List[attachment.Attachment]]:
        """
        Gets the attachments property value. The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
        Returns: Optional[List[attachment.Attachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment.Attachment]] = None) -> None:
        """
        Sets the attachments property value. The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def attendees(self,) -> Optional[List[attendee.Attendee]]:
        """
        Gets the attendees property value. The collection of attendees for the event.
        Returns: Optional[List[attendee.Attendee]]
        """
        return self._attendees
    
    @attendees.setter
    def attendees(self,value: Optional[List[attendee.Attendee]] = None) -> None:
        """
        Sets the attendees property value. The collection of attendees for the event.
        Args:
            value: Value to set for the attendees property.
        """
        self._attendees = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The body of the message associated with the event. It can be in HTML or text format.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The body of the message associated with the event. It can be in HTML or text format.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def body_preview(self,) -> Optional[str]:
        """
        Gets the bodyPreview property value. The preview of the message associated with the event. It is in text format.
        Returns: Optional[str]
        """
        return self._body_preview
    
    @body_preview.setter
    def body_preview(self,value: Optional[str] = None) -> None:
        """
        Sets the bodyPreview property value. The preview of the message associated with the event. It is in text format.
        Args:
            value: Value to set for the bodyPreview property.
        """
        self._body_preview = value
    
    @property
    def calendar(self,) -> Optional[calendar.Calendar]:
        """
        Gets the calendar property value. The calendar that contains the event. Navigation property. Read-only.
        Returns: Optional[calendar.Calendar]
        """
        return self._calendar
    
    @calendar.setter
    def calendar(self,value: Optional[calendar.Calendar] = None) -> None:
        """
        Sets the calendar property value. The calendar that contains the event. Navigation property. Read-only.
        Args:
            value: Value to set for the calendar property.
        """
        self._calendar = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Event and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.event"
        # true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. Default is true.
        self._allow_new_time_proposals: Optional[bool] = None
        # The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
        self._attachments: Optional[List[attachment.Attachment]] = None
        # The collection of attendees for the event.
        self._attendees: Optional[List[attendee.Attendee]] = None
        # The body of the message associated with the event. It can be in HTML or text format.
        self._body: Optional[item_body.ItemBody] = None
        # The preview of the message associated with the event. It is in text format.
        self._body_preview: Optional[str] = None
        # The calendar that contains the event. Navigation property. Read-only.
        self._calendar: Optional[calendar.Calendar] = None
        # The date, time, and time zone that the event ends. By default, the end time is in UTC.
        self._end: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The collection of open extensions defined for the event. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # Set to true if the event has attachments.
        self._has_attachments: Optional[bool] = None
        # When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. Default is false.
        self._hide_attendees: Optional[bool] = None
        # A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
        self._i_cal_u_id: Optional[str] = None
        # The importance property
        self._importance: Optional[importance.Importance] = None
        # The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        self._instances: Optional[List[event.Event]] = None
        # The isAllDay property
        self._is_all_day: Optional[bool] = None
        # The isCancelled property
        self._is_cancelled: Optional[bool] = None
        # The isDraft property
        self._is_draft: Optional[bool] = None
        # The isOnlineMeeting property
        self._is_online_meeting: Optional[bool] = None
        # The isOrganizer property
        self._is_organizer: Optional[bool] = None
        # The isReminderOn property
        self._is_reminder_on: Optional[bool] = None
        # The location property
        self._location: Optional[location.Location] = None
        # The locations property
        self._locations: Optional[List[location.Location]] = None
        # The collection of multi-value extended properties defined for the event. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The onlineMeeting property
        self._online_meeting: Optional[online_meeting_info.OnlineMeetingInfo] = None
        # The onlineMeetingProvider property
        self._online_meeting_provider: Optional[online_meeting_provider_type.OnlineMeetingProviderType] = None
        # The onlineMeetingUrl property
        self._online_meeting_url: Optional[str] = None
        # The organizer property
        self._organizer: Optional[recipient.Recipient] = None
        # The originalEndTimeZone property
        self._original_end_time_zone: Optional[str] = None
        # The originalStart property
        self._original_start: Optional[datetime] = None
        # The originalStartTimeZone property
        self._original_start_time_zone: Optional[str] = None
        # The recurrence property
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The reminderMinutesBeforeStart property
        self._reminder_minutes_before_start: Optional[int] = None
        # The responseRequested property
        self._response_requested: Optional[bool] = None
        # The responseStatus property
        self._response_status: Optional[response_status.ResponseStatus] = None
        # The sensitivity property
        self._sensitivity: Optional[sensitivity.Sensitivity] = None
        # The seriesMasterId property
        self._series_master_id: Optional[str] = None
        # The showAs property
        self._show_as: Optional[free_busy_status.FreeBusyStatus] = None
        # The collection of single-value extended properties defined for the event. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        # The start property
        self._start: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The subject property
        self._subject: Optional[str] = None
        # The transactionId property
        self._transaction_id: Optional[str] = None
        # The type property
        self._type: Optional[event_type.EventType] = None
        # The webLink property
        self._web_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Event:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Event
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Event()
    
    @property
    def end(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the end property value. The date, time, and time zone that the event ends. By default, the end time is in UTC.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end
    
    @end.setter
    def end(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the end property value. The date, time, and time zone that the event ends. By default, the end time is in UTC.
        Args:
            value: Value to set for the end property.
        """
        self._end = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the event. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the event. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_new_time_proposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(attachment.Attachment)),
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(attendee.Attendee)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "body_preview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(calendar.Calendar)),
            "end": lambda n : setattr(self, 'end', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "hide_attendees": lambda n : setattr(self, 'hide_attendees', n.get_bool_value()),
            "i_cal_u_id": lambda n : setattr(self, 'i_cal_u_id', n.get_str_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(importance.Importance)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(event.Event)),
            "is_all_day": lambda n : setattr(self, 'is_all_day', n.get_bool_value()),
            "is_cancelled": lambda n : setattr(self, 'is_cancelled', n.get_bool_value()),
            "is_draft": lambda n : setattr(self, 'is_draft', n.get_bool_value()),
            "is_online_meeting": lambda n : setattr(self, 'is_online_meeting', n.get_bool_value()),
            "is_organizer": lambda n : setattr(self, 'is_organizer', n.get_bool_value()),
            "is_reminder_on": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(location.Location)),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(location.Location)),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "online_meeting": lambda n : setattr(self, 'online_meeting', n.get_object_value(online_meeting_info.OnlineMeetingInfo)),
            "online_meeting_provider": lambda n : setattr(self, 'online_meeting_provider', n.get_enum_value(online_meeting_provider_type.OnlineMeetingProviderType)),
            "online_meeting_url": lambda n : setattr(self, 'online_meeting_url', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(recipient.Recipient)),
            "original_end_time_zone": lambda n : setattr(self, 'original_end_time_zone', n.get_str_value()),
            "original_start": lambda n : setattr(self, 'original_start', n.get_datetime_value()),
            "original_start_time_zone": lambda n : setattr(self, 'original_start_time_zone', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "reminder_minutes_before_start": lambda n : setattr(self, 'reminder_minutes_before_start', n.get_int_value()),
            "response_requested": lambda n : setattr(self, 'response_requested', n.get_bool_value()),
            "response_status": lambda n : setattr(self, 'response_status', n.get_object_value(response_status.ResponseStatus)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(sensitivity.Sensitivity)),
            "series_master_id": lambda n : setattr(self, 'series_master_id', n.get_str_value()),
            "show_as": lambda n : setattr(self, 'show_as', n.get_enum_value(free_busy_status.FreeBusyStatus)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "start": lambda n : setattr(self, 'start', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "transaction_id": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(event_type.EventType)),
            "web_link": lambda n : setattr(self, 'web_link', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Set to true if the event has attachments.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Set to true if the event has attachments.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def hide_attendees(self,) -> Optional[bool]:
        """
        Gets the hideAttendees property value. When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. Default is false.
        Returns: Optional[bool]
        """
        return self._hide_attendees
    
    @hide_attendees.setter
    def hide_attendees(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideAttendees property value. When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. Default is false.
        Args:
            value: Value to set for the hideAttendees property.
        """
        self._hide_attendees = value
    
    @property
    def i_cal_u_id(self,) -> Optional[str]:
        """
        Gets the iCalUId property value. A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
        Returns: Optional[str]
        """
        return self._i_cal_u_id
    
    @i_cal_u_id.setter
    def i_cal_u_id(self,value: Optional[str] = None) -> None:
        """
        Sets the iCalUId property value. A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
        Args:
            value: Value to set for the iCalUId property.
        """
        self._i_cal_u_id = value
    
    @property
    def importance(self,) -> Optional[importance.Importance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[importance.Importance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def instances(self,) -> Optional[List[event.Event]]:
        """
        Gets the instances property value. The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        Returns: Optional[List[event.Event]]
        """
        return self._instances
    
    @instances.setter
    def instances(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the instances property value. The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the instances property.
        """
        self._instances = value
    
    @property
    def is_all_day(self,) -> Optional[bool]:
        """
        Gets the isAllDay property value. The isAllDay property
        Returns: Optional[bool]
        """
        return self._is_all_day
    
    @is_all_day.setter
    def is_all_day(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAllDay property value. The isAllDay property
        Args:
            value: Value to set for the isAllDay property.
        """
        self._is_all_day = value
    
    @property
    def is_cancelled(self,) -> Optional[bool]:
        """
        Gets the isCancelled property value. The isCancelled property
        Returns: Optional[bool]
        """
        return self._is_cancelled
    
    @is_cancelled.setter
    def is_cancelled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCancelled property value. The isCancelled property
        Args:
            value: Value to set for the isCancelled property.
        """
        self._is_cancelled = value
    
    @property
    def is_draft(self,) -> Optional[bool]:
        """
        Gets the isDraft property value. The isDraft property
        Returns: Optional[bool]
        """
        return self._is_draft
    
    @is_draft.setter
    def is_draft(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDraft property value. The isDraft property
        Args:
            value: Value to set for the isDraft property.
        """
        self._is_draft = value
    
    @property
    def is_online_meeting(self,) -> Optional[bool]:
        """
        Gets the isOnlineMeeting property value. The isOnlineMeeting property
        Returns: Optional[bool]
        """
        return self._is_online_meeting
    
    @is_online_meeting.setter
    def is_online_meeting(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOnlineMeeting property value. The isOnlineMeeting property
        Args:
            value: Value to set for the isOnlineMeeting property.
        """
        self._is_online_meeting = value
    
    @property
    def is_organizer(self,) -> Optional[bool]:
        """
        Gets the isOrganizer property value. The isOrganizer property
        Returns: Optional[bool]
        """
        return self._is_organizer
    
    @is_organizer.setter
    def is_organizer(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOrganizer property value. The isOrganizer property
        Args:
            value: Value to set for the isOrganizer property.
        """
        self._is_organizer = value
    
    @property
    def is_reminder_on(self,) -> Optional[bool]:
        """
        Gets the isReminderOn property value. The isReminderOn property
        Returns: Optional[bool]
        """
        return self._is_reminder_on
    
    @is_reminder_on.setter
    def is_reminder_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReminderOn property value. The isReminderOn property
        Args:
            value: Value to set for the isReminderOn property.
        """
        self._is_reminder_on = value
    
    @property
    def location(self,) -> Optional[location.Location]:
        """
        Gets the location property value. The location property
        Returns: Optional[location.Location]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the location property value. The location property
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def locations(self,) -> Optional[List[location.Location]]:
        """
        Gets the locations property value. The locations property
        Returns: Optional[List[location.Location]]
        """
        return self._locations
    
    @locations.setter
    def locations(self,value: Optional[List[location.Location]] = None) -> None:
        """
        Sets the locations property value. The locations property
        Args:
            value: Value to set for the locations property.
        """
        self._locations = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the event. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the event. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def online_meeting(self,) -> Optional[online_meeting_info.OnlineMeetingInfo]:
        """
        Gets the onlineMeeting property value. The onlineMeeting property
        Returns: Optional[online_meeting_info.OnlineMeetingInfo]
        """
        return self._online_meeting
    
    @online_meeting.setter
    def online_meeting(self,value: Optional[online_meeting_info.OnlineMeetingInfo] = None) -> None:
        """
        Sets the onlineMeeting property value. The onlineMeeting property
        Args:
            value: Value to set for the onlineMeeting property.
        """
        self._online_meeting = value
    
    @property
    def online_meeting_provider(self,) -> Optional[online_meeting_provider_type.OnlineMeetingProviderType]:
        """
        Gets the onlineMeetingProvider property value. The onlineMeetingProvider property
        Returns: Optional[online_meeting_provider_type.OnlineMeetingProviderType]
        """
        return self._online_meeting_provider
    
    @online_meeting_provider.setter
    def online_meeting_provider(self,value: Optional[online_meeting_provider_type.OnlineMeetingProviderType] = None) -> None:
        """
        Sets the onlineMeetingProvider property value. The onlineMeetingProvider property
        Args:
            value: Value to set for the onlineMeetingProvider property.
        """
        self._online_meeting_provider = value
    
    @property
    def online_meeting_url(self,) -> Optional[str]:
        """
        Gets the onlineMeetingUrl property value. The onlineMeetingUrl property
        Returns: Optional[str]
        """
        return self._online_meeting_url
    
    @online_meeting_url.setter
    def online_meeting_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineMeetingUrl property value. The onlineMeetingUrl property
        Args:
            value: Value to set for the onlineMeetingUrl property.
        """
        self._online_meeting_url = value
    
    @property
    def organizer(self,) -> Optional[recipient.Recipient]:
        """
        Gets the organizer property value. The organizer property
        Returns: Optional[recipient.Recipient]
        """
        return self._organizer
    
    @organizer.setter
    def organizer(self,value: Optional[recipient.Recipient] = None) -> None:
        """
        Sets the organizer property value. The organizer property
        Args:
            value: Value to set for the organizer property.
        """
        self._organizer = value
    
    @property
    def original_end_time_zone(self,) -> Optional[str]:
        """
        Gets the originalEndTimeZone property value. The originalEndTimeZone property
        Returns: Optional[str]
        """
        return self._original_end_time_zone
    
    @original_end_time_zone.setter
    def original_end_time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the originalEndTimeZone property value. The originalEndTimeZone property
        Args:
            value: Value to set for the originalEndTimeZone property.
        """
        self._original_end_time_zone = value
    
    @property
    def original_start(self,) -> Optional[datetime]:
        """
        Gets the originalStart property value. The originalStart property
        Returns: Optional[datetime]
        """
        return self._original_start
    
    @original_start.setter
    def original_start(self,value: Optional[datetime] = None) -> None:
        """
        Sets the originalStart property value. The originalStart property
        Args:
            value: Value to set for the originalStart property.
        """
        self._original_start = value
    
    @property
    def original_start_time_zone(self,) -> Optional[str]:
        """
        Gets the originalStartTimeZone property value. The originalStartTimeZone property
        Returns: Optional[str]
        """
        return self._original_start_time_zone
    
    @original_start_time_zone.setter
    def original_start_time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the originalStartTimeZone property value. The originalStartTimeZone property
        Args:
            value: Value to set for the originalStartTimeZone property.
        """
        self._original_start_time_zone = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. The recurrence property
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. The recurrence property
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    @property
    def reminder_minutes_before_start(self,) -> Optional[int]:
        """
        Gets the reminderMinutesBeforeStart property value. The reminderMinutesBeforeStart property
        Returns: Optional[int]
        """
        return self._reminder_minutes_before_start
    
    @reminder_minutes_before_start.setter
    def reminder_minutes_before_start(self,value: Optional[int] = None) -> None:
        """
        Sets the reminderMinutesBeforeStart property value. The reminderMinutesBeforeStart property
        Args:
            value: Value to set for the reminderMinutesBeforeStart property.
        """
        self._reminder_minutes_before_start = value
    
    @property
    def response_requested(self,) -> Optional[bool]:
        """
        Gets the responseRequested property value. The responseRequested property
        Returns: Optional[bool]
        """
        return self._response_requested
    
    @response_requested.setter
    def response_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the responseRequested property value. The responseRequested property
        Args:
            value: Value to set for the responseRequested property.
        """
        self._response_requested = value
    
    @property
    def response_status(self,) -> Optional[response_status.ResponseStatus]:
        """
        Gets the responseStatus property value. The responseStatus property
        Returns: Optional[response_status.ResponseStatus]
        """
        return self._response_status
    
    @response_status.setter
    def response_status(self,value: Optional[response_status.ResponseStatus] = None) -> None:
        """
        Sets the responseStatus property value. The responseStatus property
        Args:
            value: Value to set for the responseStatus property.
        """
        self._response_status = value
    
    @property
    def sensitivity(self,) -> Optional[sensitivity.Sensitivity]:
        """
        Gets the sensitivity property value. The sensitivity property
        Returns: Optional[sensitivity.Sensitivity]
        """
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self,value: Optional[sensitivity.Sensitivity] = None) -> None:
        """
        Sets the sensitivity property value. The sensitivity property
        Args:
            value: Value to set for the sensitivity property.
        """
        self._sensitivity = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def series_master_id(self,) -> Optional[str]:
        """
        Gets the seriesMasterId property value. The seriesMasterId property
        Returns: Optional[str]
        """
        return self._series_master_id
    
    @series_master_id.setter
    def series_master_id(self,value: Optional[str] = None) -> None:
        """
        Sets the seriesMasterId property value. The seriesMasterId property
        Args:
            value: Value to set for the seriesMasterId property.
        """
        self._series_master_id = value
    
    @property
    def show_as(self,) -> Optional[free_busy_status.FreeBusyStatus]:
        """
        Gets the showAs property value. The showAs property
        Returns: Optional[free_busy_status.FreeBusyStatus]
        """
        return self._show_as
    
    @show_as.setter
    def show_as(self,value: Optional[free_busy_status.FreeBusyStatus] = None) -> None:
        """
        Sets the showAs property value. The showAs property
        Args:
            value: Value to set for the showAs property.
        """
        self._show_as = value
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the event. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the event. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def start(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the start property value. The start property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start
    
    @start.setter
    def start(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the start property value. The start property
        Args:
            value: Value to set for the start property.
        """
        self._start = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def transaction_id(self,) -> Optional[str]:
        """
        Gets the transactionId property value. The transactionId property
        Returns: Optional[str]
        """
        return self._transaction_id
    
    @transaction_id.setter
    def transaction_id(self,value: Optional[str] = None) -> None:
        """
        Sets the transactionId property value. The transactionId property
        Args:
            value: Value to set for the transactionId property.
        """
        self._transaction_id = value
    
    @property
    def type(self,) -> Optional[event_type.EventType]:
        """
        Gets the type property value. The type property
        Returns: Optional[event_type.EventType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[event_type.EventType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def web_link(self,) -> Optional[str]:
        """
        Gets the webLink property value. The webLink property
        Returns: Optional[str]
        """
        return self._web_link
    
    @web_link.setter
    def web_link(self,value: Optional[str] = None) -> None:
        """
        Sets the webLink property value. The webLink property
        Args:
            value: Value to set for the webLink property.
        """
        self._web_link = value
    

