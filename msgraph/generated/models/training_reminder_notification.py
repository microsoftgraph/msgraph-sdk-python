from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_end_user_notification import BaseEndUserNotification
    from .notification_delivery_frequency import NotificationDeliveryFrequency

from .base_end_user_notification import BaseEndUserNotification

@dataclass
class TrainingReminderNotification(BaseEndUserNotification):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.trainingReminderNotification"
    # Configurable frequency for the reminder email introduced during simulation creation. Possible values are: unknown, weekly, biWeekly, unknownFutureValue.
    delivery_frequency: Optional[NotificationDeliveryFrequency] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrainingReminderNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingReminderNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrainingReminderNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_end_user_notification import BaseEndUserNotification
        from .notification_delivery_frequency import NotificationDeliveryFrequency

        from .base_end_user_notification import BaseEndUserNotification
        from .notification_delivery_frequency import NotificationDeliveryFrequency

        fields: Dict[str, Callable[[Any], None]] = {
            "deliveryFrequency": lambda n : setattr(self, 'delivery_frequency', n.get_enum_value(NotificationDeliveryFrequency)),
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
        writer.write_enum_value("deliveryFrequency", self.delivery_frequency)
    

