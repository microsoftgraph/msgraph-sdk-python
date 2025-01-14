from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .location import Location

@dataclass
class Reminder(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Identifies the version of the reminder. Every time the reminder is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object.
    change_key: Optional[str] = None
    # The date, time and time zone that the event ends.
    event_end_time: Optional[DateTimeTimeZone] = None
    # The unique ID of the event. Read only.
    event_id: Optional[str] = None
    # The location of the event.
    event_location: Optional[Location] = None
    # The date, time, and time zone that the event starts.
    event_start_time: Optional[DateTimeTimeZone] = None
    # The text of the event's subject line.
    event_subject: Optional[str] = None
    # The URL to open the event in Outlook on the web.The event opens in the browser if you're logged in to your mailbox via Outlook on the web. You're prompted to log in if you aren't already logged in with the browser.This URL can't be accessed from within an iFrame.
    event_web_link: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date, time, and time zone that the reminder is set to occur.
    reminder_fire_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Reminder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Reminder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Reminder()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .location import Location

        from .date_time_time_zone import DateTimeTimeZone
        from .location import Location

        fields: dict[str, Callable[[Any], None]] = {
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "eventEndTime": lambda n : setattr(self, 'event_end_time', n.get_object_value(DateTimeTimeZone)),
            "eventId": lambda n : setattr(self, 'event_id', n.get_str_value()),
            "eventLocation": lambda n : setattr(self, 'event_location', n.get_object_value(Location)),
            "eventStartTime": lambda n : setattr(self, 'event_start_time', n.get_object_value(DateTimeTimeZone)),
            "eventSubject": lambda n : setattr(self, 'event_subject', n.get_str_value()),
            "eventWebLink": lambda n : setattr(self, 'event_web_link', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reminderFireTime": lambda n : setattr(self, 'reminder_fire_time', n.get_object_value(DateTimeTimeZone)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("changeKey", self.change_key)
        writer.write_object_value("eventEndTime", self.event_end_time)
        writer.write_str_value("eventId", self.event_id)
        writer.write_object_value("eventLocation", self.event_location)
        writer.write_object_value("eventStartTime", self.event_start_time)
        writer.write_str_value("eventSubject", self.event_subject)
        writer.write_str_value("eventWebLink", self.event_web_link)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reminderFireTime", self.reminder_fire_time)
        writer.write_additional_data_value(self.additional_data)
    

