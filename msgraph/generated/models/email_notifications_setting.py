from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .notification_events_type import NotificationEventsType
    from .notification_recipients import NotificationRecipients

from .entity import Entity

@dataclass
class EmailNotificationsSetting(Entity, Parsable):
    # The additionalEvents property
    additional_events: Optional[NotificationEventsType] = None
    # Indicates whether notifications are enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recipients property
    recipients: Optional[NotificationRecipients] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailNotificationsSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailNotificationsSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailNotificationsSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .notification_events_type import NotificationEventsType
        from .notification_recipients import NotificationRecipients

        from .entity import Entity
        from .notification_events_type import NotificationEventsType
        from .notification_recipients import NotificationRecipients

        fields: dict[str, Callable[[Any], None]] = {
            "additionalEvents": lambda n : setattr(self, 'additional_events', n.get_collection_of_enum_values(NotificationEventsType)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_object_value(NotificationRecipients)),
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
        writer.write_enum_value("additionalEvents", self.additional_events)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("recipients", self.recipients)
    

