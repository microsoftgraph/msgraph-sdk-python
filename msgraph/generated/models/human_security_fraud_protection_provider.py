from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fraud_protection_provider import FraudProtectionProvider

from .fraud_protection_provider import FraudProtectionProvider

@dataclass
class HumanSecurityFraudProtectionProvider(FraudProtectionProvider, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.humanSecurityFraudProtectionProvider"
    # Unique identifier for an individual application. You can retrieve this from the HUMAN Security Admin Console or request it from your HUMAN Security Customer Success Manager.
    app_id: Optional[str] = None
    # Unique identifier used to authenticate API calls between the Server side integration and the HUMAN platform. You can retrieve this from the HUMAN Security Admin Console or request it from your HUMAN Security Customer Success Manager.
    server_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HumanSecurityFraudProtectionProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HumanSecurityFraudProtectionProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HumanSecurityFraudProtectionProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fraud_protection_provider import FraudProtectionProvider

        from .fraud_protection_provider import FraudProtectionProvider

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "serverToken": lambda n : setattr(self, 'server_token', n.get_str_value()),
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
        writer.write_str_value("serverToken", self.server_token)
    

