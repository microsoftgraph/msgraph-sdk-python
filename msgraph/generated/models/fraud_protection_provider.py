from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
    from .entity import Entity
    from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider

from .entity import Entity

@dataclass
class FraudProtectionProvider(Entity, Parsable):
    # The display name of the fraud protection provider configuration.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FraudProtectionProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FraudProtectionProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.arkoseFraudProtectionProvider".casefold():
            from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider

            return ArkoseFraudProtectionProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.humanSecurityFraudProtectionProvider".casefold():
            from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider

            return HumanSecurityFraudProtectionProvider()
        return FraudProtectionProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
        from .entity import Entity
        from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider

        from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
        from .entity import Entity
        from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

