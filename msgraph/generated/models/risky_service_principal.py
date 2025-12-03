from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
    from .risk_detail import RiskDetail
    from .risk_level import RiskLevel
    from .risk_state import RiskState

from .entity import Entity

@dataclass
class RiskyServicePrincipal(Entity, Parsable):
    # The globally unique identifier for the associated application (its appId property), if any.
    app_id: Optional[str] = None
    # The display name for the service principal.
    display_name: Optional[str] = None
    # Represents the risk history of Microsoft Entra service principals.
    history: Optional[list[RiskyServicePrincipalHistoryItem]] = None
    # true if the service principal account is enabled; otherwise, false.
    is_enabled: Optional[bool] = None
    # Indicates whether Microsoft Entra ID is currently processing the service principal's risky state.
    is_processing: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.
    risk_detail: Optional[RiskDetail] = None
    # The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq).
    risk_last_updated_date_time: Optional[datetime.datetime] = None
    # Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).
    risk_level: Optional[RiskLevel] = None
    # State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    risk_state: Optional[RiskState] = None
    # Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Microsoft Entra ID internally and is inherited from servicePrincipal.
    service_principal_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyServicePrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipalHistoryItem".casefold():
            from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem

            return RiskyServicePrincipalHistoryItem()
        return RiskyServicePrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        from .entity import Entity
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(RiskyServicePrincipalHistoryItem)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isProcessing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskLastUpdatedDateTime": lambda n : setattr(self, 'risk_last_updated_date_time', n.get_datetime_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "servicePrincipalType": lambda n : setattr(self, 'service_principal_type', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isProcessing", self.is_processing)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_datetime_value("riskLastUpdatedDateTime", self.risk_last_updated_date_time)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("servicePrincipalType", self.service_principal_type)
    

