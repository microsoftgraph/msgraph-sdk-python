from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_reminder_recipients = lazy_import('msgraph.generated.models.booking_reminder_recipients')

class BookingReminder(AdditionalDataHolder, Parsable):
    """
    This type represents when and to whom to send an e-mail reminder.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingReminder and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The message in the reminder.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The amount of time before the start of an appointment that the reminder should be sent. It's denoted in ISO 8601 format.
        self._offset: Optional[Timedelta] = None
        # The recipients property
        self._recipients: Optional[booking_reminder_recipients.BookingReminderRecipients] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingReminder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingReminder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingReminder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_object_value(Timedelta)),
            "recipients": lambda n : setattr(self, 'recipients', n.get_enum_value(booking_reminder_recipients.BookingReminderRecipients)),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message in the reminder.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message in the reminder.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def offset(self,) -> Optional[Timedelta]:
        """
        Gets the offset property value. The amount of time before the start of an appointment that the reminder should be sent. It's denoted in ISO 8601 format.
        Returns: Optional[Timedelta]
        """
        return self._offset
    
    @offset.setter
    def offset(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the offset property value. The amount of time before the start of an appointment that the reminder should be sent. It's denoted in ISO 8601 format.
        Args:
            value: Value to set for the offset property.
        """
        self._offset = value
    
    @property
    def recipients(self,) -> Optional[booking_reminder_recipients.BookingReminderRecipients]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[booking_reminder_recipients.BookingReminderRecipients]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[booking_reminder_recipients.BookingReminderRecipients] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("offset", self.offset)
        writer.write_enum_value("recipients", self.recipients)
        writer.write_additional_data_value(self.additional_data)
    

