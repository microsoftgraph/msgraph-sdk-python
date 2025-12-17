from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .risky_user_history_item import RiskyUserHistoryItem
    from .risk_detail import RiskDetail
    from .risk_level import RiskLevel
    from .risk_state import RiskState

from .entity import Entity

@dataclass
class RiskyUser(Entity, Parsable):
    # The activity related to user risk level change
    history: Optional[list[RiskyUserHistoryItem]] = None
    # Indicates whether the user is deleted. The possible values are: true, false.
    is_deleted: Optional[bool] = None
    # Indicates whether the backend is processing a user's risky state.
    is_processing: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of the detected risk.
    risk_detail: Optional[RiskDetail] = None
    # The date and time that the risky user was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    risk_last_updated_date_time: Optional[datetime.datetime] = None
    # Level of the detected risky user. The possible values are: low, medium, high, hidden, none, unknownFutureValue.
    risk_level: Optional[RiskLevel] = None
    # State of the user's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    risk_state: Optional[RiskState] = None
    # Risky user display name.
    user_display_name: Optional[str] = None
    # Risky user principal name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUserHistoryItem".casefold():
            from .risky_user_history_item import RiskyUserHistoryItem

            return RiskyUserHistoryItem()
        return RiskyUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        from .entity import Entity
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        fields: dict[str, Callable[[Any], None]] = {
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(RiskyUserHistoryItem)),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "isProcessing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskLastUpdatedDateTime": lambda n : setattr(self, 'risk_last_updated_date_time', n.get_datetime_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isProcessing", self.is_processing)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_datetime_value("riskLastUpdatedDateTime", self.risk_last_updated_date_time)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

