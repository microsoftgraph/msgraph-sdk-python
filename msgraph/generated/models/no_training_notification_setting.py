from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .end_user_notification_setting import EndUserNotificationSetting
    from .simulation_notification import SimulationNotification

from .end_user_notification_setting import EndUserNotificationSetting

@dataclass
class NoTrainingNotificationSetting(EndUserNotificationSetting):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.noTrainingNotificationSetting"
    # The notification for the user who is part of the simulation.
    simulation_notification: Optional[SimulationNotification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NoTrainingNotificationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NoTrainingNotificationSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NoTrainingNotificationSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .end_user_notification_setting import EndUserNotificationSetting
        from .simulation_notification import SimulationNotification

        from .end_user_notification_setting import EndUserNotificationSetting
        from .simulation_notification import SimulationNotification

        fields: Dict[str, Callable[[Any], None]] = {
            "simulationNotification": lambda n : setattr(self, 'simulation_notification', n.get_object_value(SimulationNotification)),
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
        writer.write_object_value("simulationNotification", self.simulation_notification)
    

