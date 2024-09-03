from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class LocalizedNotificationMessage(Entity):
    """
    The text content of a Notification Message Template for the specified locale.
    """
    # Flag to indicate whether or not this is the default locale for language fallback. This flag can only be set. To unset, set this property to true on another Localized Notification Message.
    is_default: Optional[bool] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The Locale for which this message is destined.
    locale: Optional[str] = None
    # The Message Template content.
    message_template: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Message Template Subject.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocalizedNotificationMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocalizedNotificationMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LocalizedNotificationMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "messageTemplate": lambda n : setattr(self, 'message_template', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("messageTemplate", self.message_template)
        writer.write_str_value("subject", self.subject)
    

