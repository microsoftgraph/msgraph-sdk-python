from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_time_time_zone, location

class Reminder(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new reminder and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifies the version of the reminder. Every time the reminder is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object.
        self._change_key: Optional[str] = None
        # The date, time and time zone that the event ends.
        self._event_end_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The unique ID of the event. Read only.
        self._event_id: Optional[str] = None
        # The location of the event.
        self._event_location: Optional[location.Location] = None
        # The date, time, and time zone that the event starts.
        self._event_start_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The text of the event's subject line.
        self._event_subject: Optional[str] = None
        # The URL to open the event in Outlook on the web.The event will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.
        self._event_web_link: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date, time, and time zone that the reminder is set to occur.
        self._reminder_fire_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def change_key(self,) -> Optional[str]:
        """
        Gets the changeKey property value. Identifies the version of the reminder. Every time the reminder is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object.
        Returns: Optional[str]
        """
        return self._change_key
    
    @change_key.setter
    def change_key(self,value: Optional[str] = None) -> None:
        """
        Sets the changeKey property value. Identifies the version of the reminder. Every time the reminder is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object.
        Args:
            value: Value to set for the change_key property.
        """
        self._change_key = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Reminder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Reminder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Reminder()
    
    @property
    def event_end_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the eventEndTime property value. The date, time and time zone that the event ends.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._event_end_time
    
    @event_end_time.setter
    def event_end_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the eventEndTime property value. The date, time and time zone that the event ends.
        Args:
            value: Value to set for the event_end_time property.
        """
        self._event_end_time = value
    
    @property
    def event_id(self,) -> Optional[str]:
        """
        Gets the eventId property value. The unique ID of the event. Read only.
        Returns: Optional[str]
        """
        return self._event_id
    
    @event_id.setter
    def event_id(self,value: Optional[str] = None) -> None:
        """
        Sets the eventId property value. The unique ID of the event. Read only.
        Args:
            value: Value to set for the event_id property.
        """
        self._event_id = value
    
    @property
    def event_location(self,) -> Optional[location.Location]:
        """
        Gets the eventLocation property value. The location of the event.
        Returns: Optional[location.Location]
        """
        return self._event_location
    
    @event_location.setter
    def event_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the eventLocation property value. The location of the event.
        Args:
            value: Value to set for the event_location property.
        """
        self._event_location = value
    
    @property
    def event_start_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the eventStartTime property value. The date, time, and time zone that the event starts.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._event_start_time
    
    @event_start_time.setter
    def event_start_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the eventStartTime property value. The date, time, and time zone that the event starts.
        Args:
            value: Value to set for the event_start_time property.
        """
        self._event_start_time = value
    
    @property
    def event_subject(self,) -> Optional[str]:
        """
        Gets the eventSubject property value. The text of the event's subject line.
        Returns: Optional[str]
        """
        return self._event_subject
    
    @event_subject.setter
    def event_subject(self,value: Optional[str] = None) -> None:
        """
        Sets the eventSubject property value. The text of the event's subject line.
        Args:
            value: Value to set for the event_subject property.
        """
        self._event_subject = value
    
    @property
    def event_web_link(self,) -> Optional[str]:
        """
        Gets the eventWebLink property value. The URL to open the event in Outlook on the web.The event will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.
        Returns: Optional[str]
        """
        return self._event_web_link
    
    @event_web_link.setter
    def event_web_link(self,value: Optional[str] = None) -> None:
        """
        Sets the eventWebLink property value. The URL to open the event in Outlook on the web.The event will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.
        Args:
            value: Value to set for the event_web_link property.
        """
        self._event_web_link = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import date_time_time_zone, location

        fields: Dict[str, Callable[[Any], None]] = {
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "eventEndTime": lambda n : setattr(self, 'event_end_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "eventId": lambda n : setattr(self, 'event_id', n.get_str_value()),
            "eventLocation": lambda n : setattr(self, 'event_location', n.get_object_value(location.Location)),
            "eventStartTime": lambda n : setattr(self, 'event_start_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "eventSubject": lambda n : setattr(self, 'event_subject', n.get_str_value()),
            "eventWebLink": lambda n : setattr(self, 'event_web_link', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reminderFireTime": lambda n : setattr(self, 'reminder_fire_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def reminder_fire_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the reminderFireTime property value. The date, time, and time zone that the reminder is set to occur.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._reminder_fire_time
    
    @reminder_fire_time.setter
    def reminder_fire_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the reminderFireTime property value. The date, time, and time zone that the reminder is set to occur.
        Args:
            value: Value to set for the reminder_fire_time property.
        """
        self._reminder_fire_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

