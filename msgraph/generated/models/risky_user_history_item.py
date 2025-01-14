from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risky_user import RiskyUser
    from .risk_user_activity import RiskUserActivity

from .risky_user import RiskyUser

@dataclass
class RiskyUserHistoryItem(RiskyUser, Parsable):
    # The activity related to user risk level change.
    activity: Optional[RiskUserActivity] = None
    # The ID of actor that does the operation.
    initiated_by: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyUserHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyUserHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskyUserHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .risky_user import RiskyUser
        from .risk_user_activity import RiskUserActivity

        from .risky_user import RiskyUser
        from .risk_user_activity import RiskUserActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(RiskUserActivity)),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("activity", self.activity)
        writer.write_str_value("initiatedBy", self.initiated_by)
        writer.write_str_value("userId", self.user_id)
    

