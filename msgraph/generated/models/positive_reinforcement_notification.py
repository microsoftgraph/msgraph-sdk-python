from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_end_user_notification import BaseEndUserNotification
    from .notification_delivery_preference import NotificationDeliveryPreference

from .base_end_user_notification import BaseEndUserNotification

@dataclass
class PositiveReinforcementNotification(BaseEndUserNotification):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.positiveReinforcementNotification"
    # Delivery preference. Possible values are: unknown, deliverImmedietly, deliverAfterCampaignEnd, unknownFutureValue.
    delivery_preference: Optional[NotificationDeliveryPreference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PositiveReinforcementNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PositiveReinforcementNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PositiveReinforcementNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_end_user_notification import BaseEndUserNotification
        from .notification_delivery_preference import NotificationDeliveryPreference

        from .base_end_user_notification import BaseEndUserNotification
        from .notification_delivery_preference import NotificationDeliveryPreference

        fields: Dict[str, Callable[[Any], None]] = {
            "deliveryPreference": lambda n : setattr(self, 'delivery_preference', n.get_enum_value(NotificationDeliveryPreference)),
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
        writer.write_enum_value("deliveryPreference", self.delivery_preference)
    

