from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risky_service_principal import RiskyServicePrincipal
    from .risk_service_principal_activity import RiskServicePrincipalActivity

from .risky_service_principal import RiskyServicePrincipal

@dataclass
class RiskyServicePrincipalHistoryItem(RiskyServicePrincipal, Parsable):
    # The activity related to service principal risk level change.
    activity: Optional[RiskServicePrincipalActivity] = None
    # The identifier of the actor of the operation.
    initiated_by: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyServicePrincipalHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyServicePrincipalHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskyServicePrincipalHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .risky_service_principal import RiskyServicePrincipal
        from .risk_service_principal_activity import RiskServicePrincipalActivity

        from .risky_service_principal import RiskyServicePrincipal
        from .risk_service_principal_activity import RiskServicePrincipalActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(RiskServicePrincipalActivity)),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_str_value()),
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
    

