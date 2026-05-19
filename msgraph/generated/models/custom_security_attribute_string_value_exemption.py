from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_security_attribute_exemption import CustomSecurityAttributeExemption

from .custom_security_attribute_exemption import CustomSecurityAttributeExemption

@dataclass
class CustomSecurityAttributeStringValueExemption(CustomSecurityAttributeExemption, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customSecurityAttributeStringValueExemption"
    # Value representing custom security attribute value to compare against while evaluating the exemption.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomSecurityAttributeStringValueExemption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeStringValueExemption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomSecurityAttributeStringValueExemption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_security_attribute_exemption import CustomSecurityAttributeExemption

        from .custom_security_attribute_exemption import CustomSecurityAttributeExemption

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("value", self.value)
    

