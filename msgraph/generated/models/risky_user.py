from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, risky_user_history_item, risk_detail, risk_level, risk_state

from . import entity

@dataclass
class RiskyUser(entity.Entity):
    # The activity related to user risk level change
    history: Optional[List[risky_user_history_item.RiskyUserHistoryItem]] = None
    # Indicates whether the user is deleted. Possible values are: true, false.
    is_deleted: Optional[bool] = None
    # Indicates whether a user's risky state is being processed by the backend.
    is_processing: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of the detected risk. Possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
    risk_detail: Optional[risk_detail.RiskDetail] = None
    # The date and time that the risky user was last updated.  The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    risk_last_updated_date_time: Optional[datetime] = None
    # Level of the detected risky user. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
    risk_level: Optional[risk_level.RiskLevel] = None
    # State of the user's risk. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    risk_state: Optional[risk_state.RiskState] = None
    # Risky user display name.
    user_display_name: Optional[str] = None
    # Risky user principal name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskyUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskyUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.riskyUserHistoryItem":
                from . import risky_user_history_item

                return risky_user_history_item.RiskyUserHistoryItem()
        return RiskyUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, risky_user_history_item, risk_detail, risk_level, risk_state

        fields: Dict[str, Callable[[Any], None]] = {
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(risky_user_history_item.RiskyUserHistoryItem)),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "isProcessing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "riskLastUpdatedDateTime": lambda n : setattr(self, 'risk_last_updated_date_time', n.get_datetime_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(risk_level.RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

