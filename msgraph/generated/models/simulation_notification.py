from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_end_user_notification import BaseEndUserNotification
    from .targetted_user_type import TargettedUserType

from .base_end_user_notification import BaseEndUserNotification

@dataclass
class SimulationNotification(BaseEndUserNotification):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.simulationNotification"
    # Target user type. Possible values are: unknown, clicked, compromised, allUsers, unknownFutureValue.
    targetted_user_type: Optional[TargettedUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimulationNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SimulationNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_end_user_notification import BaseEndUserNotification
        from .targetted_user_type import TargettedUserType

        from .base_end_user_notification import BaseEndUserNotification
        from .targetted_user_type import TargettedUserType

        fields: Dict[str, Callable[[Any], None]] = {
            "targettedUserType": lambda n : setattr(self, 'targetted_user_type', n.get_enum_value(TargettedUserType)),
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
        writer.write_enum_value("targettedUserType", self.targetted_user_type)
    

